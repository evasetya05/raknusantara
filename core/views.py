from django.shortcuts import render, redirect
from item.models import Item, Category
from perpustakaan.models import Perpustakaan
from .forms import SignupForm


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    perpustakaans = Perpustakaan.objects.all()[:8]  # Show 8 latest perpustakaan

    return render(request=request, template_name='core/index.html', context={
        'categories': categories,
        'items': items,
        'perpustakaans': perpustakaans,
    })


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()

    form = SignupForm()

    return render(request=request, template_name='core/signup.html', context={
        'form': form
    })
