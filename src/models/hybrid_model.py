import numpy as np
from datetime import timedelta

class HybridModel:
    def __init__(self, ml_model, astronomical_calculator, weight_ml=0.7):
        self.ml_model = ml_model
        self.astronomical_calculator = astronomical_calculator
        self.weight_ml = weight_ml
        self.weight_astro = 1 - weight_ml

    def predict_hijri_date(self, gregorian_date, preprocessor):
        # ML prediction
        features = preprocessor.prepare_features(np.array([gregorian_date]))
        ml_prediction_days = self.ml_model.predict(features)[0]
        ml_prediction = preprocessor.gregorian_start + timedelta(days=ml_prediction_days)

        # Astronomical calculation
        astro_prediction = self.astronomical_calculator.gregorian_to_hijri(gregorian_date)
        astro_prediction = datetime(astro_prediction[0], astro_prediction[1], astro_prediction[2])

        # Combine predictions
        combined_days = (self.weight_ml * ml_prediction_days +
                         self.weight_astro * (astro_prediction - preprocessor.gregorian_start).days)
        
        return preprocessor.gregorian_start + timedelta(days=combined_days)