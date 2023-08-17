from django.shortcuts import render, redirect
from .forms import FormProduto

# Create your views here.

def home(request):
    produto_form = FormProduto()
    if request.method == "POST":
        produto_form = FormProduto(request.POST)
        if produto_form.is_valid():
            produto = produto_form.save(commit=False)
            produto.save()
            return redirect("/")

    return render(request, "homepage.html",{"produto_form": produto_form})
