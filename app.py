import streamlit as st

# Page title

st.title("🌏 Unit Converter App")
st.write("### Welcome to the unit converter!")
st.write("##### This app converts between different units of length, weight, and volume.")

# Simple categories with fewer options
length_units = ["Meters", "Kilometers", "Centimeters",]
weight_units = ["Kilograms", "Grams", "Pounds"]
volume_units = ["Liters", "Milliliters", "Gallons"]

# Category selection
category = st.radio("Select conversion type:", ["Length", "Weight", "Volume"])

# Choose units based on category
if category == "Length":
    units = length_units
elif category == "Weight":
    units = weight_units
else:  # Volume
    units = volume_units

# Select from and to units
col1, col2 = st.columns(2)
with col1:
    from_unit=st.selectbox("Convert from:",units)
with col2:
    to_unit=st.selectbox("Convert to:",units)

# Input value
value=st.number_input("Enter Value:",value=None,placeholder="type the value to convert")

# Conversion rates to base units
# Length (base: meters)
length_to_meters = {
    "Meters": 1.0,
    "Kilometers": 1000,
    "Centimeters": 0.01,
}
# Weight (base: Kilograms)
weight_to_kg = {
    "Kilograms": 1.0,
    "Grams": 0.001,
    "Pounds": 0.453592
}
# Volume (base: Liters)
volume_to_liters = {
    "Liters": 1.0,
    "Milliliters": 0.001,
    "Gallons": 3.78541
}

# Function to convert units
def convert_units(value, from_unit, to_unit):
    # Determine which conversion dictionary to use
    if from_unit in length_to_meters:
        conversion_dict = length_to_meters
    elif from_unit in weight_to_kg:
        conversion_dict = weight_to_kg
    else:
        conversion_dict = volume_to_liters

    # Convert to base unit first
    base_value = value * conversion_dict[from_unit]

    # Convert from base unit to target unit
    result = base_value / conversion_dict[to_unit]

    # Round to 3 decimal places for simplicity
    return round(result,2)

if st.button("Convert"):
    if value!=None:
        result = convert_units(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} ={result} {to_unit}")
    else:
        st.error("Please enter a value to convert")



st.markdown("---------------------------------------------------------------")  # Adds a horizontal line
st.markdown("**Developed by Nida Nasar** 👩🏻‍💻")





