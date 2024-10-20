# AstroverseAI
<div align="center">
 <img alt="astroverseai"  width="800px" src="assets/astroverseai.jpg">
</div>


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
│   ├── hijri_gregorian_correspondence.csv
│   ├── historical_eclipses.csv
│   ├── planetary_eclipse_data/
│   │   ├── mercury_eclipses.csv
│   │   ├── venus_eclipses.csv
│   │   └── ...
│   └── meteor_shower_data.csv
│
├── src/
│   ├── data_processing/
│   │   ├── __init__.py
│   │   ├── data_loader.py
│   │   └── preprocessor.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── hijri_model.py
│   │   ├── eclipse_predictor.py
│   │   ├── planetary_eclipse_predictor.py
│   │   ├── meteor_shower_predictor.py
│   │   └── gb_meteor_shower_predictor.py
│   │
│   ├── optimization/
│   │   ├── __init__.py
│   │   ├── hyperparameter_optimizer.py
│   │   ├── meteor_shower_optimizers.py
│   │   └── planetary_eclipse_optimizer.py
│   │
│   ├── analysis/
│   │   ├── __init__.py
│   │   ├── time_series_model.py
│   │   └── geographical_analysis.py
│   │
│   ├── evaluation/
│   │   ├── __init__.py
│   │   └── prediction_evaluator.py
│   │
│   └── utils/
│       ├── __init__.py
│       └── astronomical_calculations.py
│
├── tests/
│   ├── __init__.py
│   ├── test_hijri_model.py
│   ├── test_eclipse_predictor.py
│   ├── test_planetary_eclipse_predictor.py
│   └── test_meteor_shower_predictor.py
│
├── notebooks/
│   ├── hijri_calendar_analysis.ipynb
│   ├── eclipse_prediction_analysis.ipynb
│   ├── planetary_phenomena_analysis.ipynb
│   └── meteor_shower_analysis.ipynb
│
├── main.py
├── main_advanced.py
├── requirements.txt
├── CONTRIBUTING.txt
└── README.md
```


## Docker Image

The latest version of this project is available as a Docker image on DockerHub:

[![Docker Image Version (latest by date)](https://img.shields.io/docker/v/al0olo/astroverseai?label=Docker%20Image)](https://hub.docker.com/r/al0olo/astroverseai)

You can pull the image using:

```bash
docker pull al0olo/astroverseai:latest
```

### Running with Docker

To run the application using the pre-built Docker image:

1. Pull the image (if you haven't already):
   ```bash
   docker pull al0olo/astroverseai:latest
   ```

2. Run the container:
   ```bash
   docker run -it al0olo/astroverseai:latest
   ```

This will start the application in interactive mode, allowing you to use the command-line interface.


## Installation

1. Clone the repository:
   ```
   git clone https://github.com/al0olo/AstroverseAI.git
   cd AstroverseAI
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the main script:
   ```
   python main.py
   ```

   For advanced features and analysis:
   ```
   python main_advanced.py
   ```

4. To run tests:
   ```
   python -m unittest discover tests
   ```

5. Explore the Jupyter notebooks in the `notebooks/` directory for detailed analysis and visualizations.

## Contributing

Contributions to this project are welcome! Please refer to the `CONTRIBUTING.md` file for guidelines.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

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


## Continuous Integration and Deployment

This project uses GitHub Actions for continuous integration and deployment.

### Automated Testing

On each pull request and push to the main branch, the following steps are automatically performed:

1. The code is checked out.
2. The project is set up with Python 3.7, 3.8, and 3.9.
3. All dependencies are installed.
4. All tests in the `tests` directory are run.

This ensures that new changes do not break existing functionality and that the code works across different Python versions.

### Automated Deployment

When changes are merged into the main branch:

1. A new Docker image is built.
2. The image is pushed to DockerHub with the tag `latest`.

This allows for easy deployment of the most recent version of the application.


## Data

- Place your Hijri-Gregorian correspondence data in `data/hijri_gregorian_correspondence.csv`
- Historical Earth eclipse data should be in `data/historical_eclipses.csv`
- Planetary eclipse and transit data for each planet should be in separate files in the `data/` directory
- Meteor shower data and historical observations should be in `data/meteor_showers.csv` and `data/meteor_observations.csv` respectively

Ensure your data files follow the required format as described in the data processing modules.

## Model Evaluation

Evaluation metrics for all predictions (Hijri dates, Earth eclipses, planetary phenomena, and meteor showers) are output by the main scripts. For a detailed breakdown of the evaluation process, refer to the respective evaluation modules in `src/evaluation/`.
