from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import openai
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.vectorstores import faiss
from dotenv import load_dotenv