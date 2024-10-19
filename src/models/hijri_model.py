from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np
import matplotlib.pyplot as plt
from datetime import timedelta

class HijriModel:
    def __init__(self, n_estimators=100, random_state=42):
        self.model = RandomForestRegressor(n_estimators=n_estimators, random_state=random_state)

    def train(self, X, y):
        self.model.fit(X, y)
        y_pred = self.model.predict(X)
        mse = mean_squared_error(y, y_pred)
        mae = mean_absolute_error(y, y_pred)
        print(f"Model Mean Squared Error: {mse} days^2")
        print(f"Model Mean Absolute Error: {mae} days")

    def cross_validate(self, X, y, cv=5):
        scores = cross_val_score(self.model, X, y, cv=cv, scoring='neg_mean_squared_error')
        print(f"Cross-validation MSE: {-scores.mean():.2f} (+/- {scores.std() * 2:.2f})")

    def predict(self, X):
        return self.model.predict(X)

    def plot_feature_importance(self, feature_names):
        importances = self.model.feature_importances_
        indices = np.argsort(importances)[::-1]

        plt.figure(figsize=(12, 8))
        plt.title("Feature Importances")
        plt.bar(range(len(importances)), importances[indices])
        plt.xticks(range(len(importances)), [feature_names[i] for i in indices], rotation=90)
        plt.tight_layout()
        plt.show()

    def visualize_predictions(self, X, y, gregorian_dates, hijri_dates, preprocessor):
        y_pred = self.predict(X)
        
        pred_hijri_dates = [preprocessor.gregorian_start + timedelta(days=days) for days in y_pred]
        true_hijri_dates = [preprocessor.gregorian_start + timedelta(days=days) for days in y]

        plt.figure(figsize=(15, 10))
        plt.scatter(gregorian_dates, true_hijri_dates, alpha=0.5, label='Actual')
        plt.scatter(gregorian_dates, pred_hijri_dates, alpha=0.5, label='Predicted')
        plt.xlabel('Gregorian Date')
        plt.ylabel('Hijri Date')
        plt.title('Actual vs Predicted Hijri Dates')
        plt.legend()
        plt.tight_layout()
        plt.show()

        # Error distribution
        errors = [(pred - true).days for pred, true in zip(pred_hijri_dates, true_hijri_dates)]
        plt.figure(figsize=(12, 6))
        plt.hist(errors, bins=50)
        plt.xlabel('Error (days)')
        plt.ylabel('Frequency')
        plt.title('Distribution of Prediction Errors')
        plt.tight_layout()
        plt.show()