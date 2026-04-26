import pickle
import streamlit as st
import pandas as pd

model = pickle.load(open('model.pkl','rb'))

st.title("House Price Prediction App")

square_footage = st.number_input("Square Footage", value=1000.0)
num_bedrooms = st.number_input("Number of Bedrooms", value=3)
num_bathrooms = st.number_input("Number of Bathrooms", value=2)
year_built = st.number_input("Year Built", value=2000)
lot_size = st.number_input("Lot Size", value=5000.0)
garage_size = st.number_input("Garage Size", value=1)
neighborhood_quality = st.number_input("Neighborhood Quality (1-10)", value=5)

input_data = pd.DataFrame({
    'Square_Footage':[square_footage],
    'Num_Bedrooms':[num_bedrooms],
    'Num_Bathrooms':[num_bathrooms],
    'Year_Built':[year_built],
    'Lot_Size':[lot_size],
    'Garage_Size':[garage_size],
    'Neighborhood_Quality':[neighborhood_quality]
})

if st.button("Predict"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Price: {prediction[0]:.2f}")