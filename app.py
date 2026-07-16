import streamlit as st
import joblib
import pandas as pd

model = joblib.load('quebec_house_price_model.joblib')
df = pd.read_csv("quebec_housing_sales.csv")

def run():
    st.title("🏠 Quebec House Price Predictor")
    st.caption("Estimate the market value of a residential property in Quebec.")

    with st.container():

        st.subheader("📍 Location")

        col1, col2 = st.columns(2)

        with col1:
            city = st.selectbox(
                "City",
                sorted(df["city"].unique())
            )

        with col2:
            neighborhood = st.selectbox(
                "Neighborhood",
                sorted(df["neighborhood"].unique())
            )

        property_type = st.selectbox(
            "Property Type",
            sorted(df["property_type"].unique())
        )
    
    st.divider()

    st.subheader("🏡 Property Details")

    col1, col2 = st.columns(2)

    with col1:
        bedrooms = st.number_input(
        "Bedrooms",
        min_value=1,
        max_value=10
    )

    with col2:
        bathrooms = st.number_input(
            "Bathrooms",
            min_value=1,
            max_value=10
        )

    col1, col2 = st.columns(2)

    with col1:
        living_area = st.number_input(
            "Living Area (sq ft)",
            min_value=300,
            max_value=4000
        )

    with col2:
        lot_size = st.number_input(
            "Lot Size (sq ft)",
            min_value=1500,
            max_value=15000
        )

    year_built = st.slider(
        "Year Built",
        1900,
        2026,
        1985
    )

    col1, col2 = st.columns(2)

    with col1:
        garage = st.selectbox(
            "Garage",
            df["garage"].unique()
        )

    with col2:
        basement = st.selectbox(
            "Basement",
            df["basement"].unique()
        )

    sale_year = st.slider(
        "Year of Purchase",
        2020,
        2026,
        2023
    )

    st.divider()

    if st.button("🔍 Predict House Price", use_container_width=True):
        features = pd.DataFrame({
        "city": [city],
        "neighborhood": [neighborhood],
        "property_type": [property_type],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "living_area_sqft": [living_area],
        "lot_size_sqft": [lot_size],
        "year_built": [year_built],
        "garage": [garage],
        "basement": [basement],
        "sale_year": [sale_year]
    })

        prediction = model.predict(features)

        st.success(f"Estimated House Price: CAD${prediction[0]:,.2f}")
run()