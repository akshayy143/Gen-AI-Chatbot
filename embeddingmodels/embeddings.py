# from langchain_google_genai import GoogleGenAIEmbeddings

# embeddings = GoogleGenAIEmbeddings(model="gemini-embedding-001",
#                                    dimensions=64
#                                    )

# vector = embeddings.embed_query("You are going to learn Gen AI")
# print(vector)  # 


import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings

os.environ["GOOGLE_API_KEY"] = "wQ"

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    output_dimensionality=64
)

vector = embeddings.embed_query("You are going to learn Gen AI")

print(vector)
