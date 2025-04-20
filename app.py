import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from recipe_bot.langchain_chain import get_recipe_response
from langchain_community.llms import OpenAI



# Set Streamlit page config
st.set_page_config(page_title="Recipe Chatbot", layout="centered")

st.title("🥗 Recipe Generator Chatbot")

# 1. Input box for ingredients
ingredients = st.text_input("Enter ingredients (comma separated):", placeholder="e.g. tomato, onion, paneer")

# 2. Veg/Non-Veg selection
diet_choice = st.radio("Select Diet Type:", ["Vegetarian", "Non-Vegetarian"], horizontal=True)

# 3. Generate Recipe button
if st.button("Get Recipe"):
    if ingredients.strip() == "":
        st.warning("Please enter at least one ingredient.")
    else:
        recipe_type = "vegetarian" if diet_choice == "Vegetarian" else "non-vegetarian"
        result = get_recipe_response(recipe_type, ingredients)

        st.write(f"Result: {result}")
