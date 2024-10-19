# AstroverseAI

## Overview

This project combines advanced machine learning techniques with astronomical calculations to provide accurate predictions for:
- The Hijri (Islamic) calendar
- Solar and lunar eclipses on Earth
- Planetary eclipses and transits in the solar system
- Meteor shower timing and intensity

It aims to bridge traditional Islamic calendar methodologies with modern data science approaches while extending its capabilities to broader astronomical predictions.

## Features

- Hijri date prediction based on Gregorian dates
- Solar and lunar eclipse prediction for Earth
- Planetary eclipse and transit predictions for Mercury, Venus, Mars, Jupiter, and Saturn
- Meteor shower predictions, including timing and intensity
- Integration of machine learning models with astronomical calculations
- Geographical analysis of calendar and eclipse observations
- Time series analysis for long-term predictions
- Hyperparameter optimization for model fine-tuning
- Comprehensive evaluation metrics for prediction accuracy

## Project Structure

```
AstroverseAI/
│
├── data/
├── src/
│   ├── data_processing/
│   ├── models/
│   │   ├── hijri_model.py
│   │   ├── eclipse_predictor.py
│   │   ├── planetary_eclipse_predictor.py
│   │   └── meteor_shower_predictor.py
│   ├── optimization/
│   ├── analysis/
│   ├── evaluation/
│   └── utils/
├── tests/
│   ├── test_hijri_model.py
│   ├── test_eclipse_predictor.py
│   ├── test_planetary_eclipse_predictor.py
│   └── test_meteor_shower_predictor.py
├── notebooks/
├── main.py
├── main_advanced.py
├── requirements.txt
└── README.md
```

## Installation

(Installation instructions remain the same)

## Usage

### Basic Usage

Run the main script for basic astronomical predictions:

```
python main.py
```

### Advanced Analysis

For advanced features including meteor shower predictions, model optimization, and geographical analysis:

```
python main_advanced.py
```

### Jupyter Notebooks

Explore detailed analyses and visualizations, including meteor shower patterns:

1. Start Jupyter Notebook:
   ```
   jupyter notebook
   ```

2. Open and run the notebooks in the `notebooks/` directory.

## Data

- Place your Hijri-Gregorian correspondence data in `data/hijri_gregorian_correspondence.csv`
- Historical Earth eclipse data should be in `data/historical_eclipses.csv`
- Planetary eclipse and transit data for each planet should be in separate files in the `data/` directory
- Meteor shower data and historical observations should be in `data/meteor_showers.csv` and `data/meteor_observations.csv` respectively

Ensure your data files follow the required format as described in the data processing modules.

## Model Evaluation

Evaluation metrics for all predictions (Hijri dates, Earth eclipses, planetary phenomena, and meteor showers) are output by the main scripts. For a detailed breakdown of the evaluation process, refer to the respective evaluation modules in `src/evaluation/`.

(The rest of the README remains largely the same, with appropriate additions to acknowledgments and citations if new data sources or methodologies were used for the meteor shower predictions.)