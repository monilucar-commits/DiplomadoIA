import os
import warnings
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.chat_history import InMemoryChatMessageHistory
import time

warnings.filterwarnings("ignore")

# 🔐 Cargar variables .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("❌ No se encontró OPENAI_API_KEY en el archivo .env")


# 🤖 Modelo OpenRouter
llm = ChatOpenAI(
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key=api_key,
    model_name="meta-llama/llama-3.3-70b-instruct",
    temperature=0.01,
)


print("💬 Chatbot con memoria vía OpenRouter")
print("Escribe 'salir' para terminar\n")


# 🧠 Memoria del chatbot
memoria = InMemoryChatMessageHistory()


Meta_promt = """

"""


while True:

    user_input = input("👤 Tú: ")

    if user_input.lower() in ["salir", "exit", "quit"]:
        print("👋 Hasta luego.")
        break


    try:

        # Guardar mensaje del usuario en memoria
        memoria.add_message(
            HumanMessage(content=user_input)
        )


        # Crear contexto completo
        mensajes = [
            HumanMessage(content=Meta_promt)
        ] + memoria.messages


        # Enviar conversación al modelo
        response = llm.invoke(mensajes)


        respuesta = response.content.strip()


        print(f"🤖 Bot: {respuesta}\n")


        # Guardar respuesta del bot en memoria
        memoria.add_message(
            AIMessage(content=respuesta)
        )


        time.sleep(2)


    except Exception as e:
        print(f"❌ Error: {e}\n")