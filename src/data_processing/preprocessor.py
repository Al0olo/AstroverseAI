import numpy as np
import pandas as pd
from datetime import datetime
from scipy.signal import find_peaks

class Preprocessor:
    def __init__(self, gregorian_start=datetime(622, 7, 16)):
        self.gregorian_start = gregorian_start
        self.metonic_cycle = 19 * 365.2425  # 19 years in days
        self.lunar_cycle = 29.53059  # Average lunar cycle in days

    def prepare_features(self, dates):
        days_since_start = (dates - self.gregorian_start).dt.total_seconds() / (24 * 3600)
        metonic_phase = (days_since_start % self.metonic_cycle) / self.metonic_cycle
        lunar_phase = (days_since_start % self.lunar_cycle) / self.lunar_cycle
        year = dates.dt.year
        month = dates.dt.month
        day = dates.dt.day
        day_of_year = dates.dt.dayofyear
        is_leap_year = dates.dt.is_leap_year.astype(int)
        
        # Season (using day of year as a proxy)
        season = np.sin(2 * np.pi * day_of_year / 365.25)
        
        # Moon's elongation (simplified calculation)
        elongation = (days_since_start % self.lunar_cycle) / self.lunar_cycle * 360
        
        # Identify potential start of Islamic months (simplified)
        potential_month_starts = find_peaks(lunar_phase, height=0.9)[0]
        is_potential_month_start = np.isin(range(len(dates)), potential_month_starts).astype(int)

        return np.column_stack((
            days_since_start, metonic_phase, lunar_phase, year, month, day, 
            day_of_year, is_leap_year, season, elongation, is_potential_month_start
        ))

    def prepare_target(self, dates):
        return (dates - self.gregorian_start).dt.total_seconds() / (24 * 3600)