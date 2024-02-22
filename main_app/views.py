from django.shortcuts import render




# controller in Express = view in django
# Create your views here.
def home(request):
    return True


def about(request):
    return render (request, 'about.html')