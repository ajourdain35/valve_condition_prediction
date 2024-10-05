1. Github/Gitlab
2. Tests unitaires
    Se placer à la racine du projet puis exécuter "python -m unittest discover -s tests"
3. Contenairiser
    docker build -t valve_condition_prediction .
    docker run -p 5000:5000 valve_condition_prediction
4. App web
    Lancer "python ./app.py"
    http://127.0.0.1:5000/

valve_condition_prediction
├─── README.md
├─── requirements.txt
├─── Dockerfile
├─── .gitignore
└─── tests
     └─── test.py
     └─── __init__.py
└─── src
     └─── app.py
     └─── __init__.py
└─── templates
     └─── index.html
└─── notebooks
     └─── valve_condition_prediction.ipynb
└─── data_subset
     └─── FS1.txt
     └─── PS2.txt
     └─── profile.txt