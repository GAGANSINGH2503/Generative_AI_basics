from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.document_loaders import OnlinePDFLoader

## 1. Perform data ingestion 
doc_path='D:\prompting\ollama\data\paper.pdf'
model="llama3"

# local PDF file uploads
if doc_path:
    loader=UnstructuredPDFLoader(file_path=doc_path)
    data=loader.load()
    print("done loading....")
else:
    print("Upload a PDF file")
    
# preview the first page 
content=data[0].page_content
print(content[:100])

## 2.Extract Text from pdf file and split into small chunks 
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

# Split and chunk 
text_splitter=RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=300)
chunks=text_splitter.split_documents(data)
print("done splitting")

print(f"Number of chunks: {len(chunks)}")
print(f"Example chunk: {chunks[0]}")

## 3. Add in Vector Database 
import ollama
ollama.pull(model="nomic-embed-text")

vector_db=Chroma.from_documents(
    documents=chunks,
    embedding=OllamaEmbeddings(model="nomic-embed-text"),
    collection_name="simple-rag"
)
print("Done Adding to vector database....")

## Retrieval 
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnablePassthrough 
from langchain.retrievers.multi_query import MultiQueryRetriever

# set Up the model 
llm=ChatOllama(model=model)
QUERY_PROMPT=PromptTemplate(
    input_variables=["question"],
    template="""
    You are a highly intelligent and context-aware assistant with deep knowledge of the subject matter contained in the provided PDF document. Your task is to extract accurate information and provide insightful answers by analyzing the content of the document.

Given a user query, perform the following steps:
1. **Understand the question.**
2. **Break it down into multiple relevant sub-questions**, if applicable.
3. **Search the PDF content** for answers using your context window and memory.
4. **Generate a detailed yet concise answer** to the main question, based on the sub-questions and retrieved context.
5. Always respond in a professional, helpful tone.
Provide these alternative questions separately with solution.
Original Question: {question}
    """
)
retriever=MultiQueryRetriever.from_llm(
    vector_db.as_retriever(), llm, prompt=QUERY_PROMPT
)

# RAG prompt
template="""Answer the question based ONLY on the following context:  
{context}
Question: {question}
"""

prompt=ChatPromptTemplate.from_template(template)

chain=(
    {"context":retriever, "question":RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

res=chain.invoke(input=("What is the document about?",))
res2=chain.invoke(
    input=("what are the main points as a business owner I should ")
)
res1=chain.invoke(input=("how to report BOI?",))

print(res)
print(res2)
print(res1)