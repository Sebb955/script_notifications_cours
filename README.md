# README : Script qui envoie une notification des cours de l'UEVE.

Ce script Python utilise Selenium, BeautifulSoup, et Pushbullet pour automatiser la récupération de l'emploi du temps universitaire depuis le site Web de l'Université d'Évry. L'emploi du temps est extrait, et une notification est envoyée via Pushbullet pour informer l'utilisateur des cours du lendemain. 

## Prérequis

Avant d'utiliser ce script, assurez-vous d'avoir les modules Python nécessaires installés. Vous pouvez les installer en utilisant la commande suivante :

```bash
pip install selenium beautifulsoup4 pushbullet.py schedule
```
ou
```bash
pip install -r requirements.txt
```


De plus, assurez-vous d'avoir le navigateur Firefox installé sur votre système, car le script utilise le pilote Gecko pour contrôler le navigateur.

## Fichiers Principaux

- **console_version.py** : Exécute le script dans la console, affichant les informations de cours dans la sortie standard.

- **pushbullet_version.py** : Exécute le script et envoie les informations de cours via Pushbullet.


## Configuration du script

1. **Téléchargement du pilote Gecko (geckodriver) :**
   - Assurez-vous de télécharger le pilote Gecko depuis [GeckoDriver Downloads](https://github.com/mozilla/geckodriver/releases).
   - Spécifiez le chemin du pilote Gecko en remplaçant la variable `gecko_driver_path` dans le script.

2. **Configuration du compte Pushbullet :**
   - Obtenez une clé API Pushbullet depuis [Pushbullet](https://www.pushbullet.com/#settings).
   - Remplacez la clé API dans le script à la place de `'MY_KEY_API'`.

3. **Identifiants du compte étudiant :**
   - Remplacez les paramètres de la fonction `login` avec l'URL du site de l'Université d'Évry et le `code étudiant`.

## Utilisation

- Exécutez le script en utilisant la commande suivante :

```bash
python script.py
```

**Dans la version Pushbullet** le script s'exécutera automatiquement à 20h50 chaque jour pour récupérer l'emploi du temps du lendemain et enverra une notification Pushbullet avec les détails des cours.

## Exemple avec la version console :

https://github.com/Sebb955/script_notifications_cours/assets/79416415/6870b868-937a-4e22-9fef-476affbc1db2

## Remarques importantes

- Assurez-vous que votre ordinateur est allumé et connecté à Internet au moment de l'exécution planifiée.
- Les détails de l'emploi du temps sont extraits en utilisant des sélecteurs XPath spécifiques. En cas de modification du site Web, ces sélecteurs peuvent devenir obsolètes, nécessitant une mise à jour du script.
- Le script utilise la bibliothèque `schedule` pour planifier les tâches. Assurez-vous que le fuseau horaire de votre système est correctement configuré.

## Auteur

Ce script a été développé par Sebby75.

---
