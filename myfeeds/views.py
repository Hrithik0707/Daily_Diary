from django.shortcuts import render,redirect
from .models import Entry
from .forms import Entryform
# Create your views here.
def index(request):
    myfeeds = Entry.objects.order_by('-date_posted')
    context = {'myfeeds': myfeeds}
    return render(request,'myfeeds/index.html', context)

def add(request):
    if request.method == 'POST':
        form = Entryform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Entryform()

    context = {'form':form}
    return render(request, 'myfeeds/add.html', context)