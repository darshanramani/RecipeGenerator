from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_ollama import OllamaLLM
from langchain_community.llms import OpenAI




def get_recipe_response(recipe_type, ingredients):
    # Step 1: Load the Ollama model
    llm = OllamaLLM(model="gemma:2b")


    # Step 2: Create the prompt
    recipe_prompt = PromptTemplate(
        input_variables=["recipe_type", "ingredients"],
        template="Give me a {recipe_type} recipe using the following ingredients:\n{ingredients}",
    )

    # Step 3: Create runnable chain using new style
    chain = recipe_prompt | llm
    # chain = RunnableSequence([recipe_prompt, llm])


    # Step 4: Get output
    result = chain.invoke({"recipe_type": recipe_type, "ingredients": ingredients})
    return result


