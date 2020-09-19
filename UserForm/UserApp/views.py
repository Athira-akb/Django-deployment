from django.shortcuts import render
from .import forms

# Create your views here.
def index(request):
    return render(request, 'index.html')

def user(request):
    form = forms.user_form()
    if request.method == "POST":
        form = forms.user_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'index.html')

        else:
            print("Error")
    return render(request, 'user_form.html', {'form' : form})
