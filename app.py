import streamlit as st
import os
from recipe_bot.langchain_chain import get_recipe_response

# Set the OpenAI API key from Streamlit Secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# Streamlit page config
st.set_page_config(page_title="Recipe Chatbot", layout="centered")
st.title("🥗 Recipe Generator Chatbot")

# Input ingredients
ingredients = st.text_input("Enter ingredients (comma separated):", placeholder="e.g. tomato, onion, paneer")

# Diet type selector
diet_choice = st.radio("Select Diet Type:", ["Vegetarian", "Non-Vegetarian"], horizontal=True)

# Generate button
if st.button("Get Recipe"):
    if ingredients.strip() == "":
        st.warning("Please enter at least one ingredient.")
    else:
        recipe_type = "vegetarian" if diet_choice == "Vegetarian" else "non-vegetarian"
        result = get_recipe_response(recipe_type, ingredients)
        st.markdown("### 🧑‍🍳 Your Generated Recipe:")
        st.success(result)
