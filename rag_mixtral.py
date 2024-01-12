"""
Simple example of using the RAG model with a local LLM model.
and host it as a telegram chatbot
"""

from pathlib import Path
import qdrant_client
from llama_index import (
    VectorStoreIndex,
    ServiceContext,
    download_loader,
)
from llama_index.llms import Ollama
from llama_index.storage.storage_context import StorageContext
from llama_index.vector_stores.qdrant import QdrantVectorStore


def get_documents():
    # RAG data
    # JSONReader = download_loader("JSONReader")
    # loader = JSONReader()
    # documents = loader.load_data(Path('./tinytweets.json'))

    PDFReader = download_loader("PDFReader")
    loader = PDFReader()
    documents = loader.load_data(Path("./Penal-Code-Act-574.pdf"))
    return documents


def create_query_engine(llm, documents):
    print("init storage service context")
    client = qdrant_client.QdrantClient(
        path="./qdrant_data"
    )
    vector_store = QdrantVectorStore(
        client=client, collection_name="colletion_name1")
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    service_context = ServiceContext.from_defaults(
        llm=llm, embed_model="local")

    index = VectorStoreIndex.from_documents(documents,
                                            service_context=service_context,
                                            storage_context=storage_context)
    return index.as_query_engine()


if __name__ == "__main__":
    # llm = Ollama(model="mixtral_gpu") # custom model name
    llm = Ollama(model="mistral")
    docs = get_documents()
    query_engine = create_query_engine(llm, docs)

    response = query_engine.query(
        "What is the punishment for stealing in a shopping center?")

    print(response)
    print("-------------------done test, now run telegram----------------")

    import telebot

    key = input("Provide Telegram Bot Key: ")
    bot = telebot.TeleBot(key, parse_mode=None)

    @bot.message_handler(func=lambda m: True)
    def echo_all(message):
        print(message.text)
        response = query_engine.query(message.text)
        bot.reply_to(message, response)

    bot.infinity_polling()

    print("-------------------done exiting----------------")
    print("\n")
