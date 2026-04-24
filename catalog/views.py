from django.shortcuts import render
from .ai_assistant import get_ai_recommendation

def chat_view(request):
    response = None
    user_query = None
    
    if request.method == "POST":
        user_query = request.POST.get("query")
        response = get_ai_recommendation(user_query)
        
    return render(request, 'catalog/chat.html', {
        'response': response,
        'user_query': user_query
    })