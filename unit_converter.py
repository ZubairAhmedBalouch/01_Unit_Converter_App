import streamlit as st

st.title("Welcome to Unit Converter App⚡")
st.markdown("##### Convert Easily the Basic Units, Like Length📏, Weight⚖️, and Time.⏱️ ")
st.write("Welcome! Select a category, Enter a value and get the converted result.")

category = st.selectbox("Select a category:", ["Length", "Weight", "Time"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Meters":
            return value * 1000
        elif unit == "Meters to Kilometers":
            return value / 1000
        elif unit == "Miles to Kilometers":
            return value * 1.60934
        elif unit == "Kilometers to Miles": 
            return value / 1.60934
        
    elif category == "Weight":
        if unit == "Kilograms to Grams":
            return value * 1000
        elif unit == "Grams to Kilograms":
            return value / 1000
        elif unit == "Pounds to Kilograms":
            return value * 0.453592
        elif unit == "Kilograms to Pounds":
            return value / 0.453592
    
    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60

if category == "Length":
    unit = st.selectbox("📏Select a unit:", ["Kilometers to Meters", "Meters to Kilometers", "Miles to Kilometers", "Kilometers to Miles"])
elif category == "Weight":
    unit = st.selectbox("📏Select a unit:", ["Kilograms to Grams", "Grams to Kilograms", "Pounds to Kilograms", "Kilograms to Pounds"])
elif category == "Time":
    unit = st.selectbox("📏Select a unit:", ["Seconds to Minutes", "Minutes to Seconds", "Hours to Minutes", "Minutes to Hours"])

value = st.number_input("Enter the value to convert:")        

if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The converted value is: {result:.2f}")

