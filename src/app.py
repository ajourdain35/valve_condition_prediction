# -*- coding: utf-8 -*-
import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from flask import Flask, request, render_template

current_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(os.path.dirname(current_dir), 'templates')

app = Flask(__name__, template_folder=template_dir)

def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(current_dir)

    profile_path = os.path.join(base_dir, "data_subset", "profile.txt")
    fs1_path = os.path.join(base_dir, "data_subset", "FS1.txt")
    ps2_path = os.path.join(base_dir, "data_subset", "PS2.txt")

    names = ["cooler_condition", "valve_condition", "internal_pump_leakage", "hydraulic_accumulator", "stable_flag"]
    profile = pd.read_csv(profile_path, sep=r"\s+", names=names)
    fs1 = pd.read_csv(fs1_path, sep=r"\s+", header=None)
    ps2 = pd.read_csv(ps2_path, sep=r"\s+", header=None)

    X = pd.concat([fs1, ps2], axis=1, keys=['fs1', 'ps2'])
    y = profile["valve_condition"]

    return X, y


def train_model(X, y, training_samples=2000):
    if training_samples <= 0 or training_samples >= X.shape[0]:
        raise ValueError("Le nombre d'échantillons d'apprentissage doit être compris entre 1 et 2204.")
    
    X_train, y_train = X[:training_samples], y[:training_samples]
    X_test, y_test = X[training_samples:], y[training_samples:]
    
    rf = RandomForestClassifier()
    rf.fit(X_train, y_train)
    
    accuracy = rf.score(X_test, y_test)
    
    return rf, accuracy


@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    training_samples = None

    if request.method == 'POST':
        try:
            training_samples = int(request.form['training_samples'])
            if training_samples < 1 or training_samples > 2204:
                return render_template('index.html', prediction="Erreur : Nombre d'exemples hors limite.", training_samples=training_samples)
            X, y = load_data()
            rf, accuracy = train_model(X, y, training_samples=training_samples)
            prediction = f"Exactitude du modèle : {accuracy:.2%}"
        except Exception as e:
            prediction = f"Erreur lors du calcul : {str(e)}"

    return render_template('index.html', prediction=prediction, training_samples=training_samples)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")