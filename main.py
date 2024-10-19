import sys
from datetime import datetime, timedelta
from src.data_processing.data_loader import DataLoader
from src.models.hijri_model import HijriModel
from src.models.eclipse_predictor import EclipsePredictor
from src.models.planetary_eclipse_predictor import PlanetaryEclipsePredictor
from src.models.meteor_shower_predictor import MeteorShowerPredictor
from src.models.gb_meteor_shower_predictor import GBMeteorShowerPredictor

def load_and_train_models():
    loader = DataLoader()
    
    # Hijri Calendar Model
    hijri_data = loader.load_hijri_data()
    hijri_model = HijriModel()
    hijri_model.train(hijri_data)
    
    # Earth Eclipse Model
    eclipse_data = loader.load_eclipse_data()
    eclipse_model = EclipsePredictor()
    eclipse_model.train(eclipse_data)
    
    # Planetary Eclipse Model
    planetary_model = PlanetaryEclipsePredictor()
    for planet in ['mercury', 'venus', 'mars', 'jupiter', 'saturn']:
        planet_data = loader.load_planetary_eclipse_data(planet)
        planetary_model.train(planet_data, planet)
    
    # Meteor Shower Models
    meteor_data = loader.load_meteor_shower_data()
    rf_meteor_model = MeteorShowerPredictor()
    gb_meteor_model = GBMeteorShowerPredictor()
    rf_meteor_model.train(meteor_data)
    gb_meteor_model.train(meteor_data)
    
    return hijri_model, eclipse_model, planetary_model, rf_meteor_model, gb_meteor_model

def main():
    print("Loading and training models...")
    hijri_model, eclipse_model, planetary_model, rf_meteor_model, gb_meteor_model = load_and_train_models()
    print("Models loaded and trained successfully.")

    while True:
        print("\nAstronomical Prediction System")
        print("1. Hijri Date Conversion")
        print("2. Earth Eclipse Prediction")
        print("3. Planetary Eclipse Prediction")
        print("4. Meteor Shower Prediction")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            gregorian_date = input("Enter Gregorian date (YYYY-MM-DD): ")
            hijri_date = hijri_model.predict(datetime.strptime(gregorian_date, "%Y-%m-%d"))
            print(f"Corresponding Hijri date: {hijri_date}")
        
        elif choice == '2':
            date = input("Enter date for eclipse prediction (YYYY-MM-DD): ")
            eclipse = eclipse_model.predict(datetime.strptime(date, "%Y-%m-%d"))
            print(f"Eclipse prediction for {date}: {eclipse}")
        
        elif choice == '3':
            planet = input("Enter planet name (mercury, venus, mars, jupiter, saturn): ")
            date = input("Enter date for planetary eclipse prediction (YYYY-MM-DD): ")
            eclipse = planetary_model.predict_eclipse(datetime.strptime(date, "%Y-%m-%d"), planet)
            print(f"Planetary eclipse prediction for {planet} on {date}: {eclipse}")
        
        elif choice == '4':
            start_date = input("Enter start date for meteor shower prediction (YYYY-MM-DD): ")
            end_date = input("Enter end date for meteor shower prediction (YYYY-MM-DD): ")
            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(end_date, "%Y-%m-%d")
            date_range = pd.date_range(start, end)
            rf_predictions = rf_meteor_model.predict({'date': date_range})
            gb_predictions = gb_meteor_model.predict({'date': date_range})
            print("Meteor shower predictions:")
            for date, rf_pred, gb_pred in zip(date_range, rf_predictions, gb_predictions):
                print(f"{date.date()}: RF: {rf_pred:.2f}, GB: {gb_pred:.2f} (meteors/hour)")
        
        elif choice == '5':
            print("Thank you for using the Astronomical Prediction System. Goodbye!")
            sys.exit()
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()