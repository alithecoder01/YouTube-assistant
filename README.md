# YouTube assistant
 Creating YouTube assistant using LangChain framework

### 1. Create the .venv using cmd
 > python -m venv .venv

### 2. Activate the .venv
 > source .venv/bin/activate

### 3. Install requred packeges 
 > pip install langchain openai faiss-cpu streamlit python-dotenv youtube-transcript-api

### 4. Import the laibraries
 ```
 from langchain.document_loaders import YoutubeLoader
 from langchain.text_splitter import RecursiveCharacterTextSplitter
 from langchain.llms import openai
 from langchain import PromptTemplate
 from langchain.chains import LLMChain
 from langchain.vectorstores import faiss
 ```