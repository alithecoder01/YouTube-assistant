from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import openai
from langchain import PromptTemplate
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import LLMChain
from langchain.vectorstores import faiss
from dotenv import load_dotenv

load_dotenv()

embading = OpenAIEmbeddings()

# load all the transcipt from the video and splite it into chunks of 1000 only cuz openai can't take more than 1000, and save them as vector
def create_vector_db_from_youTube_url(vid_Url: str) -> faiss:
    # will load the vidoe and take the transcript of it
    loader = YoutubeLoader.from_youTube_url(vid_Url)
    trascript = loader.load()

    # splite the text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 100)
    docs = text_splitter.split_documents(trascript)

    db = faiss.from_documents(docs,embading)
    return db
