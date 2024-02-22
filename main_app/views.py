from django.shortcuts import render


cats = [
  {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
  {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
]

# controller in Express = view in django
# Create your views here.
def home(request):
    return True


def about(request):
    return render (request, 'about.html')

def cat_index(request):
    context={
        'cats': cats
    }
    return render (request, 'cat_index.html', context)