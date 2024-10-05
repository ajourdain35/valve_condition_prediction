# -*- coding: utf-8 -*-
import unittest

from src.app import app, load_data, train_model

class TestValveConditionPrediction(unittest.TestCase):

    def setUp(self):
        self.training_samples = 1600

    def test_load_data(self):
        X, y = load_data()
        self.assertEqual(X.shape[0], len(y))
        self.assertEqual(X.shape[1], 6600)

    def test_train_model(self):
        X, y = load_data()
        model, accuracy = train_model(X, y, self.training_samples)
        self.assertGreater(accuracy, 0.95)


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home_get(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_predict_with_valid_training_samples(self):
        response = self.app.post('/', data={'training_samples': '1500'})
        self.assertEqual(response.status_code, 200)
        response_text = response.data.decode('utf-8')
        self.assertIn('Exactitude du mod\u00e8le', response_text)

    def test_predict_with_invalid_training_samples(self):
        response = self.app.post('/', data={'training_samples': '3000'})
        self.assertEqual(response.status_code, 200)
        response_text = response.data.decode('utf-8')
        self.assertIn('Erreur : Nombre d&#39;exemples hors limite', response_text)