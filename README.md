# YouTube assistant
 Creating YouTube assistant using LangChain framework

### 1. Create the .venv using cmd
 > python -m venv .venv

### 2. Activate the .venv
 > source .venv/bin/activate

### 3. Install requred packeges 
 > pip install langchain openai faiss-cpu streamlit python-dotenv youtube-transcript-api

### 4. Import the laibraries im Langchain_helper.py
 ```
 from langchain_community.document_loaders import YoutubeLoader
 from langchain.text_splitter import RecursiveCharacterTextSplitter
 from langchain_community.llms import openai
 from langchain.prompts import PromptTemplate
 from langchain_openai import OpenAIEmbeddings
 from langchain.chains import LLMChain
 from langchain_community.vectorstores import FAISS
 from dotenv import load_dotenv
 ```

### 5. use dotenv to load the einvironment
 ```
 load_dotenv()
 ```

### 6. initiate the openai embading 
 ```
 embading = OpenAIEmbeddings()
 ```

### 7. Create the function for creating youtube vector from vide using faiss
 ```
 # load all the transcipt from the video and splite it into chunks of 1000 only cuz openai can't take more than 1000,and save them as vector
 def create_vector_db_from_youTube_url(vid_Url: str) -> FAISS:
    # will load the vidoe and take the transcript of it
    loader = YoutubeLoader.from_youtube_url(vid_Url)
    trascript = loader.load()

    # splite the text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 100)
    docs = text_splitter.split_documents(trascript)

    db = FAISS.from_documents(docs,embading)
    return db
 ```

### 8. Create the second function which will be used to genrate the respons
```
def get_respons_from_quary(db , query, k=4):
    # text-davianci can handel only 4000 tokens

    docs = db.similarity_search(query, k=k)
    # to compain the 4 pages sp total will be 4000 only
    docs_page_content= " ".join([d.page_content for d in docs])

    llm = openai(model= "text-davianci-003")

    prmpt = PromptTemplate(
        input_variables=["question","docs"],
        template="""
        You are a helpful assistant that that can answer questions about youtube videos 
        based on the video's transcript.
        
        Answer the following question: {question}
        By searching the following video transcript: {docs}
        
        Only use the factual information from the transcript to answer the question.
        
        If you feel like you don't have enough information to answer the question, say "I don't know".
        
        Your answers should be verbose and detailed.
        """,
    )

    chain = LLMChain(llm=llm, prompt=prmpt)

    respons = chain.run(question=query, docs=docs_page_content)
    respons = respons.replace("\n","")
    
    return respons
```

### 9. Create the streamlit interface 
> import the libraries 
```
import streamlit as st
import Langchain_helper as lgc 
import textwrap
```
