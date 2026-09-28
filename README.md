# Boston House Price Prediction

A machine learning web application that predicts a house's price using property and neighbourhood information from the Boston Housing dataset. The project uses a trained regression model and a Flask web interface where users can enter feature values and receive a prediction.

## Live Demo

**Try the application:**  
https://boston-house-pricing-ml-vsz7.onrender.com/

## Project Overview

The goal of this project is to build and deploy a machine learning model that estimates house prices from 13 input features.

The application is built with:

- **Python** for the application and machine learning code
- **Flask** for the web server and prediction routes
- **Pandas and NumPy** for handling input data
- **Scikit-learn** for preprocessing and regression prediction
- **HTML and CSS** for the user interface
- **Gunicorn** as the production web server
- **Render** for deployment

The user enters the property information in a web form. The application arranges the values in the feature order expected by the model, applies the saved scaler, and passes the transformed data to the trained regression model.

## Features

- Web form for entering all 13 model features
- Dropdown inputs for `CHAS` and `RAD`
- Input labels and descriptions to help users understand each feature
- Preprocessing with a saved scaler
- House price prediction using a saved regression model
- Flask route for form-based predictions
- JSON API route for sending prediction requests
- Hosted online using Render

## Machine Learning Features

The model uses the following 13 features from the Boston Housing dataset:

| Feature | Description |
|---|---|
| `CRIM` | Per capita crime rate by town |
| `ZN` | Proportion of residential land zoned for lots over 25,000 sq. ft. |
| `INDUS` | Proportion of non-retail business acres per town |
| `CHAS` | Charles River dummy variable: `1` if the tract bounds the river, otherwise `0` |
| `NOX` | Nitric oxides concentration, in parts per 10 million |
| `RM` | Average number of rooms per dwelling |
| `AGE` | Proportion of owner-occupied units built before 1940 |
| `DIS` | Weighted distances to five Boston employment centres |
| `RAD` | Index of accessibility to radial highways |
| `TAX` | Full-value property-tax rate per $10,000 |
| `PTRATIO` | Pupil-teacher ratio by town |
| `B` | Dataset feature calculated as `1000(Bk - 0.63)²` |
| `LSTAT` | Percentage of lower-status population |

**Important:** Enter values using the definitions and units above. The model expects these specific features in this order:

```text
CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT
```

## How It Works

1. The user opens the application and enters the 13 property and neighbourhood values.
2. The form sends the values to the Flask prediction route.
3. The application arranges the values in the same order used during model training.
4. The saved scaler transforms the input features.
5. The transformed values are passed to the trained regression model.
6. The application displays the predicted house price.

The model and scaler are stored as serialized files and loaded by the Flask application.

## Project Structure

A typical project layout looks like this:

```text
Boston-House-Price-Prediction/
│
├── app.py
├── home.html
├── regression_model.pkl
├── scaling.pkl
├── requirements.txt
├── Procfile
├── .gitignore
└── README.md
```

If your HTML file is stored in a Flask `templates` directory, use this layout instead:

```text
Boston-House-Price-Prediction/
│
├── app.py
├── regression_model.pkl
├── scaling.pkl
├── requirements.txt
├── Procfile
├── .gitignore
├── README.md
│
└── templates/
    └── home.html
```

Make sure the paths in `app.py` match the actual locations of your model, scaler, and HTML template files.

## Requirements

- Python 3.10–3.12 recommended
- pip
- The trained model file: `regression_model.pkl`
- The fitted scaler file: `scaling.pkl`

Use the same or compatible versions of Scikit-learn and related libraries that were used when the model and scaler were saved. Pickle-based model files may not load correctly across incompatible library versions.

## Run the Project Locally

### 1. Clone the repository

Replace the example URL below with your GitHub repository URL.

```bash
git clone https://github.com/your-username/your-repository.git
```

Move into the project directory:

```bash
cd your-repository
```

### 2. Create a virtual environment

On Windows:

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you do not yet have a `requirements.txt`, create one with the libraries used by your application. For example:

```text
Flask
pandas
numpy
scikit-learn
gunicorn
```

For a reproducible deployment, pin the versions that match your development and model-training environment.

### 4. Check the model files

Confirm that these files exist in the expected locations:

```text
regression_model.pkl
scaling.pkl
```

The filenames must match the filenames referenced in `app.py`. For example, `scale.pkl` and `scaling.pkl` are different names.

### 5. Start the Flask application

```bash
python app.py
```

Open the local address printed in your terminal, commonly:

```text
http://127.0.0.1:5000/
```

Enter the feature values and submit the form to see a prediction.

## API Usage

The application also provides a JSON prediction route at:

```text
POST /predict_api
```

Send a JSON object containing a `data` object. The `data` object must include all 13 feature names and their numeric values.

### Example request

```json
{
  "data": {
    "CRIM": 0.00632,
    "ZN": 18,
    "INDUS": 2.31,
    "CHAS": 0,
    "NOX": 0.538,
    "RM": 6.575,
    "AGE": 65.2,
    "DIS": 4.09,
    "RAD": 1,
    "TAX": 296,
    "PTRATIO": 15.3,
    "B": 396.9,
    "LSTAT": 4.98
  }
}
```

### Example using Python

```python
import requests

url = "http://127.0.0.1:5000/predict_api"

payload = {
    "data": {
        "CRIM": 0.00632,
        "ZN": 18,
        "INDUS": 2.31,
        "CHAS": 0,
        "NOX": 0.538,
        "RM": 6.575,
        "AGE": 65.2,
        "DIS": 4.09,
        "RAD": 1,
        "TAX": 296,
        "PTRATIO": 15.3,
        "B": 396.9,
        "LSTAT": 4.98
    }
}

response = requests.post(url, json=payload)

print(response.status_code)
print(response.json())
```

For the deployed application, replace the local URL with:

```text
https://boston-house-pricing-ml-vsz7.onrender.com/predict_api
```

The API expects all required feature names. If the request format or feature names do not match what the application expects, the request may fail.

## Deployment

This project is deployed on [Render](https://render.com/).

Typical Render configuration for a Flask application:

| Setting | Value |
|---|---|
| Runtime | Python |
| Build command | `pip install -r requirements.txt` |
| Start command | `gunicorn app:app` |

The start command assumes that:

- The Python application file is named `app.py`.
- The Flask application instance inside it is named `app`.
- `gunicorn` is included in `requirements.txt`.

If you use a different Python filename or Flask instance name, update the start command accordingly.

## Model and Preprocessing Notes

- The regression model is loaded from `regression_model.pkl`.
- The fitted preprocessing scaler is loaded from `scaling.pkl`.
- Inputs must be provided in the feature order used during training.
- The scaler should be used for transforming new inputs; it should not be fitted again on a single prediction request.
- The model's output unit depends on how the target variable was prepared during training. Check your training notebook before interpreting the numeric prediction as dollars or thousands of dollars.

## Testing the Application

After starting the application:

1. Open the homepage in your browser.
2. Enter values for all 13 features.
3. Select values for `CHAS` and `RAD` where applicable.
4. Click **Predict House Price**.
5. Check that the result is displayed on the page.
6. If the app returns an error, check the Flask terminal output and confirm that the model and scaler files are present and compatible.

You can also test the JSON endpoint using Python, Postman, or another HTTP client.

## Limitations

- The prediction is an estimate from a trained machine learning model, not a professional property valuation.
- The model reflects patterns in its training dataset and may not represent current housing prices.
- The Boston Housing dataset is historical and geographically specific; its relationships may not generalize to present-day markets or other locations.
- Prediction quality depends on the training data, preprocessing, and model evaluation.
- The application does not replace an appraisal, inspection, or local real estate market analysis.

## Future Improvements

Possible future enhancements include:

- Add clearer validation messages for missing or invalid inputs.
- Display the prediction with a clearly stated unit and currency.
- Add a chart showing how selected input values relate to the dataset.
- Compare multiple regression algorithms and evaluation metrics.
- Add automated tests for input validation and prediction routes.
- Improve accessibility and mobile responsiveness.
- Add a model information page describing training data and evaluation results.

## License

Add a license before distributing or reusing this project. If you intend to use an open-source license, create a `LICENSE` file in the repository and name the license here.

## Author

**Anil Aryal**

BSc in Computer Science and Information Technology  
Interested in machine learning, data science, and web development.

---

**Disclaimer:** This project is developed for educational and demonstration purposes. Predictions should not be used as the sole basis for financial or real estate decisions.