# Valve Condition Prediction

## Description
Ce projet vise à prédire l'état de la valve d'un système hydraulique en utilisant un modèle de machine learning et à identifier les causes d'un état non-optimal de la valve. 

## Fonctionnalités principales
- **Tâche principale** : Exploration des données et analyse dans notebooks/valve_condition_prediction.ipynb
- **Tâche bonus 1** : Mise à disposition du projet sur github. Cloner le projet avec "git clone https://github.com/ajourdain35/valve_condition_prediction.git"
- **Tâche bonus 2** : Ajout de tests unitaires. Exécuter "python -m unittest discover -s tests" à la racine du projet pour lancer les tests dans tests/test_app.py
- **Tâche bonus 3** : Possibilité de containeriser le code avec le Dockerfile présent à la racine et la commande "docker build -t valve_condition_prediction ."
- **Tâche bonus 4** : Application web (voir dossiers src/ et templates/) permettant de définir le nombre d'exemples d'apprentissage pour entraîner le modèle et d'afficher sa fiabilité après entraînement. Lancer l'application à partir du docker avec "docker run -p 5000:5000 valve_condition_prediction". 