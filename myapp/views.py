from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {'message': 'Toi la Pham Van Du'})
