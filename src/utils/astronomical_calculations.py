from datetime import datetime, timedelta
import math

class AstronomicalCalculator:
    def __init__(self, hijri_epoch=datetime(622, 7, 16)):
        self.hijri_epoch = hijri_epoch
        self.lunar_cycle = 29.53058868  # Mean length of synodic month

    def gregorian_to_hijri(self, gregorian_date):
        days_since_epoch = (gregorian_date - self.hijri_epoch).days
        lunar_cycles = days_since_epoch / self.lunar_cycle
        
        hijri_year = math.floor((30 * lunar_cycles + 10646) / 10631)
        hijri_month = math.floor((lunar_cycles - (29.5 * math.floor(lunar_cycles / 354.367))) + 1)
        hijri_day = math.floor(lunar_cycles - math.floor(lunar_cycles)) * self.lunar_cycle + 1

        return (hijri_year, int(hijri_month), int(hijri_day))

    def hijri_to_gregorian(self, hijri_year, hijri_month, hijri_day):
        lunar_cycles = (hijri_year * 354.367) + (hijri_month - 1) * 29.5 + (hijri_day - 1)
        days_since_epoch = lunar_cycles * self.lunar_cycle
        return self.hijri_epoch + timedelta(days=days_since_epoch)