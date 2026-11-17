from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

information = """ """
sumamry_template = """ 
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """
summary_promt_template = PromptTemplate(
    input_variables=["information"],
    template=sumamry_template,
)
llm = ChatGoogleGenerativeAI(temperature=0,
                             model="gemini-3.1-flash-lite"
                             )
chain = summary_promt_template | llm
response = chain.invoke(input={"information": information})

print(response.content)