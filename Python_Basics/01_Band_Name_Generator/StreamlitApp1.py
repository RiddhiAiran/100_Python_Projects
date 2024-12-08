import streamlit as st


st.title("Basic Band Name Generator")
st.write("Welcome to the Basic Band Name Generator.")

city = st.text_input("What's the name of the city you grew up in?")
pet = st.text_input("What's your pet's name?")

def band_name_generator(city, pet):
    """Generate band name using user inputs"""
    return f"{city} {pet}"

if city and pet:
    band_name = band_name_generator(city, pet)
    st.write(f"Your band name could be: **{band_name}**")
