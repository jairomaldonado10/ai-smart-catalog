import google.generativeai as genai
import os
from .models import Product
from dotenv import load_dotenv

load_dotenv()

def get_ai_recommendation(user_query):
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash')
    products = Product.objects.all()
    context = "Catálogo de Alpha Tech Chile:\n"
    for p in products:
        context += f"- {p.name}: {p.description}. Precio: ${p.price}. Categoría: {p.category}\n"

    prompt = f"""
    Eres un asistente de ventas experto de 'Alpha Tech Chile'. 
    Usa SOLO esta lista para recomendar:
    {context}

    Pregunta del cliente: "{user_query}"
    
    Instrucciones:
    - Si el cliente pregunta por un presupuesto, filtra los productos.
    - Sé amable y destaca por qué el producto le sirve.
    - Si no tienes el producto, sugiere algo parecido o di que pronto llegará stock.
    """

    response = model.generate_content(prompt)
    return response.text