import numpy as np
from datetime import datetime

class Preprocessor:
    def __init__(self, gregorian_start=datetime(622, 7, 16)):
        self.gregorian_start = gregorian_start
        self.metonic_cycle = 19 * 365.2425  # 19 years in days

    def prepare_features(self, dates):
        days_since_start = (dates - self.gregorian_start).dt.total_seconds() / (24 * 3600)
        metonic_phase = (days_since_start % self.metonic_cycle) / self.metonic_cycle
        year = dates.dt.year
        month = dates.dt.month
        day = dates.dt.day
        return np.column_stack((days_since_start, metonic_phase, year, month, day))

    def prepare_target(self, dates):
        return (dates - self.gregorian_start).dt.total_seconds() / (24 * 3600)