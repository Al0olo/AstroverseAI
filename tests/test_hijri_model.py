import unittest
from datetime import datetime
from data_processing.data_loader import DataLoader
from data_processing.preprocessor import Preprocessor
from models.hijri_model import HijriModel
from utils.astronomical_calculations import AstronomicalCalculator
from models.hybrid_model import HybridModel

class TestHijriModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load a small test dataset
        cls.loader = DataLoader('test_data.csv')
        cls.data = cls.loader.load_data()
        cls.preprocessor = Preprocessor()
        cls.X = cls.preprocessor.prepare_features(cls.data['gregorian_date'])
        cls.y = cls.preprocessor.prepare_target(cls.data['hijri_date'])
        
        # Train the ML model
        cls.ml_model = HijriModel()
        cls.ml_model.train(cls.X, cls.y)
        
        # Initialize other components
        cls.astro_calc = AstronomicalCalculator()
        cls.hybrid_model = HybridModel(cls.ml_model, cls.astro_calc)

    def test_ml_model_prediction(self):
        test_date = datetime(2023, 11, 15)
        features = self.preprocessor.prepare_features(np.array([test_date]))
        prediction = self.preprocessor.gregorian_start + timedelta(days=self.ml_model.predict(features)[0])
        self.assertIsInstance(prediction, datetime)

    def test_astronomical_calculation(self):
        test_date = datetime(2023, 11, 15)
        hijri_date = self.astro_calc.gregorian_to_hijri(test_date)
        self.assertIsInstance(hijri_date, tuple)
        self.assertEqual(len(hijri_date), 3)

    def test_hybrid_model(self):
        test_date = datetime(2023, 11, 15)
        prediction = self.hybrid_model.predict_hijri_date(test_date, self.preprocessor)
        self.assertIsInstance(prediction, datetime)

    def test_model_accuracy(self):
        # Test on a subset of data
        test_subset = self.data.iloc[:100]
        X_test = self.preprocessor.prepare_features(test_subset['gregorian_date'])
        y_test = self.preprocessor.prepare_target(test_subset['hijri_date'])
        
        predictions = self.ml_model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        self.assertLess(mse, 5)  # Assuming we want error less than 5 days^2

    def test_cross_validation(self):
        scores = self.ml_model.cross_validate(self.X, self.y)
        self.assertGreater(len(scores), 1)
        self.assertLess(np.mean(scores), 5)  # Assuming we want average error less than 5 days^2

if __name__ == '__main__':
    unittest.main()