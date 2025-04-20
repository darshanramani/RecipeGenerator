from langchain_core.prompts import PromptTemplate
from langchain_community.llms import OpenAI

def get_recipe_response(recipe_type, ingredients):
    # Load OpenAI LLM
    llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

    # Define prompt
    recipe_prompt = PromptTemplate(
        input_variables=["recipe_type", "ingredients"],
        template="Give me a {recipe_type} recipe using the following ingredients:\n{ingredients}"
    )

    # Chain prompt to LLM
    chain = recipe_prompt | llm

    # Run the chain
    result = chain.invoke({"recipe_type": recipe_type, "ingredients": ingredients})
    return result
