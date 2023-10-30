from django.shortcuts import render

# Create your views here.
# To view my index.page of my website
def index(request):
    return render(request, 'index.html')

# To view the contact page of my website
def contact_page(request):
    return render(request, 'contact_page.html')

# To view about more about the product of the company
def about_page(request):
    return render(request, 'about_page.html')
