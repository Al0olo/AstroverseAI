from data_loader import DataLoader
from preprocessor import Preprocessor
from hijri_model import HijriModel
from eclipse_predictor import EclipsePredictor
from planetary_eclipse_predictor import PlanetaryEclipsePredictor
from meteor_shower_predictor import MeteorShowerPredictor
from gb_meteor_shower_predictor import GBMeteorShowerPredictor
from eclipse_model_tuner import EclipseModelTuner
from hyperparameter_optimizer import HyperparameterOptimizer
from time_series_model import TimeSeriesModel
from geographical_analysis import GeographicalAnalysis
from datetime import datetime, timedelta
import unittest
from test_eclipse_predictor import TestEclipsePredictor
from test_planetary_eclipse_predictor import TestPlanetaryEclipsePredictor
from test_meteor_shower_predictor import TestMeteorShowerPredictor
import matplotlib.pyplot as plt

def plot_meteor_shower_predictions(rf_predictions, gb_predictions, shower_name):
    plt.figure(figsize=(12, 6))
    plt.plot(rf_predictions['date'], rf_predictions['intensity'], label='Random Forest')
    plt.plot(gb_predictions['date'], gb_predictions['intensity'], label='Gradient Boosting')
    plt.title(f'{shower_name} Meteor Shower Prediction Comparison')
    plt.xlabel('Date')
    plt.ylabel('Intensity')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # ... (previous code for Hijri date prediction, Earth eclipse prediction, and planetary eclipse prediction remains the same)

    # Load and preprocess data
    loader = DataLoader('path_to_your_data.csv')
    data = loader.load_data()
    preprocessor = Preprocessor()
    X = preprocessor.prepare_features(data['gregorian_date'])
    y = preprocessor.prepare_target(data['hijri_date'])

    # Hyperparameter optimization for Hijri model
    optimizer = HyperparameterOptimizer(X, y)
    best_params, best_score = optimizer.random_search()
    print(f"Best hyperparameters for Hijri model: {best_params}")
    print(f"Best score for Hijri model: {best_score}")

    # Train optimized Hijri model
    optimized_hijri_model = HijriModel(**best_params)
    optimized_hijri_model.train(X, y)

    # Time series analysis for Hijri predictions
    ts_model = TimeSeriesModel(data)
    ts_model.fit_arima()
    ts_mse = ts_model.evaluate(data['hijri_date'][-365:])  # Evaluate on last year of data
    print(f"Time Series Model MSE for Hijri predictions: {ts_mse}")

    # Geographical analysis for Hijri predictions
    geo_analyzer = GeographicalAnalysis(optimized_hijri_model, preprocessor)
    regions = data['region'].unique()  # Assuming 'region' column exists
    regional_results = geo_analyzer.analyze_by_region(data, regions)
    geo_analyzer.plot_regional_performance(regional_results)


    # Eclipse predictor
    loader = DataLoader('path_to_your_eclipse_data.csv')
    eclipse_data = loader.load_eclipse_data()
    eclipse_predictor = EclipsePredictor()

    # Fine-tuning the eclipse prediction model
    tuner = EclipseModelTuner(eclipse_predictor)
    X = eclipse_predictor.prepare_features(eclipse_data['date'])
    y = eclipse_data['eclipse_type']
    best_model = tuner.random_search(X, y)
    eclipse_predictor.model = best_model

    # Train the fine-tuned model
    eclipse_predictor.train(eclipse_data)

    # Run tests
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEclipsePredictor)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # Generate eclipse predictions for next 10 years
    start_date = datetime.now()
    end_date = start_date + timedelta(days=3650)  # Roughly 10 years
    eclipse_calendar = eclipse_predictor.generate_eclipse_calendar(start_date, end_date)
    print("Predicted Eclipses for next 10 years:")
    print(eclipse_calendar.head())  # Print first few predictions

    # Evaluate eclipse predictions (assuming we have actual eclipse data for comparison)
    actual_eclipses = loader.load_actual_eclipses(start_date, end_date)
    from evaluate_eclipse_predictions import evaluate_eclipse_predictions
    evaluation_results = evaluate_eclipse_predictions(eclipse_calendar, actual_eclipses)
    print("Eclipse Prediction Evaluation Results:")
    for metric, value in evaluation_results.items():
        print(f"{metric}: {value}")

    # Planetary Eclipse Predictor
    planetary_predictor = PlanetaryEclipsePredictor()
    planetary_optimizer = PlanetaryEclipseOptimizer()
    planets = ['mercury', 'venus', 'mars', 'jupiter', 'saturn']
    
    # Load historical planetary eclipse data
    loader = DataLoader()
    historical_planetary_data = {planet: loader.load_planetary_eclipse_data(planet) for planet in planets}

    # Optimize and train planetary eclipse models
    for planet in planets:
        print(f"\nOptimizing and training model for {planet} eclipses:")
        X = planetary_predictor.prepare_features(historical_planetary_data[planet]['date'], planet)
        y = historical_planetary_data[planet]['eclipse_type']
        
        best_model = planetary_optimizer.random_search(X, y, n_iter=50, cv=5)
        planetary_predictor.models[planet] = best_model

    # Run tests for planetary eclipse prediction
    planetary_suite = unittest.TestLoader().loadTestsFromTestCase(TestPlanetaryEclipsePredictor)
    unittest.TextTestRunner(verbosity=2).run(planetary_suite)

    # Generate planetary eclipse predictions for next 10 years
    start_date = datetime.now()
    end_date = start_date + timedelta(days=3650)  # Roughly 10 years
    for planet in planets:
        predictions = planetary_predictor.generate_eclipse_calendar(start_date, end_date, planet)
        print(f"\nPredicted Eclipses for {planet.capitalize()} (next 10 years):")
        print(predictions.head())
        
        # Plot predictions
        plot_planetary_eclipse_predictions(predictions, planet)

    # Meteor Shower Predictors
    rf_predictor = MeteorShowerPredictor()
    gb_predictor = GBMeteorShowerPredictor()
    shower_data = load_shower_data()
    historical_meteor_data = load_historical_observations()

    # Train the meteor shower models
    for shower_name, shower_info in shower_data.items():
        print(f"\nTraining models for {shower_name}:")
        print("Random Forest Model:")
        rf_predictor.train(shower_info, historical_meteor_data)
        print("\nGradient Boosting Model:")
        gb_predictor.train(shower_info, historical_meteor_data)

    # Run tests for meteor shower prediction
    meteor_suite = unittest.TestLoader().loadTestsFromTestCase(TestMeteorShowerPredictor)
    unittest.TextTestRunner(verbosity=2).run(meteor_suite)

    # Generate meteor shower predictions for next year
    start_date = datetime.now()
    end_date = start_date + timedelta(days=365)
    for shower_name, shower_info in shower_data.items():
        rf_predictions = rf_predictor.predict_shower(start_date, end_date, shower_info)
        gb_predictions = gb_predictor.predict_shower(start_date, end_date, shower_info)

        rf_peak_date, rf_peak_intensity = rf_predictor.get_peak_time(rf_predictions)
        gb_peak_date, gb_peak_intensity = gb_predictor.get_peak_time(gb_predictions)

        print(f"\nPredictions for {shower_name}:")
        print(f"Random Forest - Predicted peak: {rf_peak_date} with intensity {rf_peak_intensity}")
        print(f"Gradient Boosting - Predicted peak: {gb_peak_date} with intensity {gb_peak_intensity}")

        # Plot predictions
        plot_meteor_shower_predictions(rf_predictions, gb_predictions, shower_name)

    # You could add more analysis or visualization here

if __name__ == "__main__":
    main()
