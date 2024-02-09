from langchain_community.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.llms import openai
#from langchain.prompts.PromptTemplate import PromptTemplate
from langchain_openai import OpenAIEmbeddings
from langchain.chains import LLMChain
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

embading = OpenAIEmbeddings()

url = "https://www.youtube.com/watch?v=lG7Uxts9SXs&t=430s"

# load all the transcipt from the video and splite it into chunks of 1000 only cuz openai can't take more than 1000, and save them as vector
def create_vector_db_from_youTube_url(vid_Url: str) -> FAISS:
    # will load the vidoe and take the transcript of it
    loader = YoutubeLoader.from_youtube_url(vid_Url)
    trascript = loader.load()

    # splite the text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 100)
    docs = text_splitter.split_documents(trascript)

    db = FAISS.from_documents(docs,embading)
    return db

