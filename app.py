import pickle
from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__)

regmodel = pickle.load(open('regression_model.pkl', 'rb'))
scaler = pickle.load(open('scaling.pkl', 'rb'))

# Column order the preprocessor was trained with
FEATURES = list(scaler.feature_names_in_)
CAT_COLS = ["CHAS", "RAD"]  # trained as strings (OpenML categoricals)


def build_frame(data: dict) -> pd.DataFrame:
    missing = [c for c in FEATURES if c not in data]
    if missing:
        raise ValueError(f"Missing features: {missing}")

    df = pd.DataFrame([data])[FEATURES]  # enforce column order

    for col in CAT_COLS:
        # 1, 1.0, "1" -> "1"
        df[col] = df[col].apply(lambda v: str(int(float(v))))

    num_cols = [c for c in FEATURES if c not in CAT_COLS]
    df[num_cols] = df[num_cols].astype(float)
    return df


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict_api', methods=['POST'])
def predict_api():
    try:
        payload = request.get_json(force=True)
        new_data = build_frame(payload['data'])
        scaled = scaler.transform(new_data)
        result = regmodel.predict(scaled)
        return jsonify({'prediction': float(result[0])})
    except (KeyError, ValueError) as e:
        return jsonify({'error': str(e)}), 400

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form.to_dict()

        new_data = build_frame(data)

        scaled = scaler.transform(new_data)

        output = regmodel.predict(scaled)

        return render_template(
            'home.html',
            prediction_text=f'The House Price Prediction is: {output[0]:.2f}'
        )

    except (KeyError, ValueError) as e:
        return render_template(
            'home.html',
            prediction_text=f'Error: {str(e)}'
        )

if __name__ == "__main__":
    app.run(debug=True)