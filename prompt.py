from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.chains.retrieval_qa.base import RetrievalQA 
from langchain_openai import ChatOpenAI
from redundant_filter_retriver import RedundantFilterRetriver

load_dotenv()

chat = ChatOpenAI()

embeddings = OpenAIEmbeddings()
db = Chroma(
    persist_directory="emb",
    embedding_function=embeddings
)

retriever = RedundantFilterRetriver(
    embeddings=embeddings,
    chroma=db,
)

chain = RetrievalQA.from_chain_type(
    llm=chat,
    retriever=retriever,
    chain_type="stuff"
)

result = chain.invoke("what is an intresting fact about english language?")