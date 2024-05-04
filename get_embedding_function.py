from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.embeddings.bedrock import BedrockEmbeddings
from langchain_community.embeddings.gpt4all import GPT4AllEmbeddings

def get_embedding_function():
    embeddings = OllamaEmbeddings(model="xwinlm")
    # embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings


        # credentials_profile_name="default", region_name="us-east-1"