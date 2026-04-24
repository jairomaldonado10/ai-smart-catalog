import google.generativeai as genai
import os
from .models import Product

def get_ai_recommendation(user_query):
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash')

    # 1. Obtenemos los productos de la DB
    products = Product.objects.all()
    context = "Lista de productos disponibles:\n"
    for p in products:
        context += f"- {p.name}: {p.description}. Precio: ${p.price}. Categoría: {p.category}\n"

    prompt = f"""
    Eres un asistente de ventas experto. Basándote SOLO en la lista de productos abajo, 
    responde a la duda del cliente: "{user_query}"
    
    Si el cliente menciona un presupuesto (ej: 50 lucas), filtra los productos.
    Responde de forma amable y profesional.
    
    {context}
    """

    response = model.generate_content(prompt)
    return response.text