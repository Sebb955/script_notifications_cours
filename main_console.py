from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

gecko_driver_path = '/Users/.../Dowloads/geckodriver' # Remplacer par votre propre chemin
driver = webdriver.Firefox()

def login(url, code):
    driver.get(url)
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/input[1]").clear()
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/input[1]").send_keys(code)
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/input[5]").click()
    WebDriverWait(driver, 10).until(EC.title_contains('Emploi du temps'))
    time.sleep(1)

    # Attendre que le bouton des jours soit visible
    days_button = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="horiz3"]')))
    days_button.click()
    time.sleep(1)
    
    # Attendre que le bouton "Skip" soit visible
    skip_button = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/form[1]/a[3]')))
    skip_button.click()
    time.sleep(1)
    
    # Sélectionner tous les éléments <area> en utilisant XPath
    area_elements = driver.find_elements(By.XPATH, '/html/body/div/map/area')

    # Chaîne pour stocker tous les résultats imprimés
    notification_text = ""

    # Cliquez sur chaque élément <area>
    for area_element in area_elements:
        area_title = area_element.get_attribute("title")

        # Supprimer "PRESENTIEL"
        area_title = area_title.replace("- PRESENTIEL", "")

        match = re.search(r' - (.*?)Salle :', area_title)
        if match:
            extracted_part = match.group(1)
            # Ajouter "Salle" à la partie extraite
            extracted_part = f"{extracted_part} "
            # Remplacer la partie originale par la partie modifiée
            area_title = area_title.replace(match.group(1), extracted_part)
            # Ajouter la modification à la chaîne de notification
            notification_text += f"{area_title}\n"

            # Ouvrir un nouvel onglet avec le lien de l'area
            link = area_element.get_attribute("href")
            driver.execute_script(f"window.open('{link}', '_blank');")

            # Attendre que le nouvel onglet soit complètement chargé
            time.sleep(2)  # Ajout d'un temps d'attente de 2 secondes
            driver.switch_to.window(driver.window_handles[1])

            # ..............................

            # Trouver tous les éléments <tr> à l'intérieur du tableau
            rows = WebDriverWait(driver, 30).until(
                EC.presence_of_all_elements_located((By.XPATH, '//table/tbody/tr'))
            )

            # Parcourir chaque élément <tr>
            for row in rows:
                # Rechercher tous les <td> avec le <span> ayant l'attribut de style spécifié
                spans = row.find_elements(By.XPATH, './/td/span[@style="font-size:12px;color:blue; font-weight:bold;"]')

                # Vérifier si la liste spans n'est pas vide et a suffisamment d'éléments
                if spans and len(spans) >= 9:
                    # Accéder au 9e élément dans la liste (heure de début)
                    ninth_span = spans[7]
                    notification_text += f"---- Heure début : {ninth_span.text} ----\n"

            # ..............................

            # Fermer le nouvel onglet
            driver.close()

            # Revenir à l'onglet d'origine
            driver.switch_to.window(driver.window_handles[0])
            
    
    # Si aucun élément <area> n'est trouvé, grasse matinée !
    if not area_elements:
        notification_text = "Grasse matinée aujourd'hui !"
    
    # Ajouter tous les résultats imprimés dans la chaîne de notification
    driver.close()

    body = notification_text
    print("Cours de demain : ", body)

    
login('https://edt.univ-evry.fr/index.php?disconnect=true', 'Code Etudiant')

