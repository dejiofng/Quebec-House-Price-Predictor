# 🏠 Quebec House Price Prediction

A machine learning web application that predicts residential property prices in Quebec, Canada. The project uses a scikit-learn regression pipeline for data preprocessing and prediction, with an interactive Streamlit interface for users to estimate house prices based on property characteristics.

## Features

* Predicts house prices in Canadian Dollars (CAD).
* Interactive web interface built with Streamlit.
* Handles missing values automatically using a preprocessing pipeline.
* Encodes categorical variables using One-Hot Encoding.
* Accepts property details such as:

  * City
  * Neighborhood
  * Property Type
  * Bedrooms
  * Bathrooms
  * Living Area
  * Lot Size
  * Year Built
  * Garage
  * Basement
  * Sale Year

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib

## Machine Learning Pipeline

The model was trained using a Scikit-learn Pipeline, which automatically performs:

* Missing value imputation
* One-Hot Encoding for categorical features
* Linear Regression for price prediction

This ensures that the same preprocessing applied during training is also applied when making predictions in the web application.

## Project Structure

```text
├── app.py
├── quebec_house_price_model.joblib
├── house_price_prediction.ipynb
├── dataset.csv
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## Example Prediction

Enter the property details through the web interface, click **Predict House Price**, and the application returns the estimated market value in Canadian Dollars (CAD).

## Future Improvements

* Improve model accuracy through feature engineering.
* Compare multiple regression algorithms.
* Add interactive visualizations of property trends.
* Deploy the application online for public access.

## Author

**Adedeji Badmus**

Computer Science Student | Machine Learning Enthusiast
