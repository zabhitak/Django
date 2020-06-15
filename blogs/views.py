from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .forms import EmailPostForm
from django.http import HttpResponse
from .models import Resource
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from .forms import ResourceForm 
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)



class ResourceListView(ListView):
    model = Resource
    template_name = 'blogs/about.html'
    context_object_name = 'resources'
    


def upload_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blogs:about')
    else:
        form = ResourceForm()

    return render(request,{'form':form})





def post_share(request):
   
    return render(request, 'blogs/index.html')

def post_share1(request):
    return render(request, 'blogs/404.html')


def post_share2(request):
    return render(request, 'blogs/abhinav.html')


def post_share4(request):
    return render(request, 'blogs/bhavya.html')


def post_share5(request):
    return render(request, 'blogs/blog.html')




def post_share6(request):
    # Retrieve post by id
    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            message = "{0} has sent you a new message:\n\n{1}".format(cd['name'], cd['comments'])
            send_mail('XmetadorZ', message, 'admin@myblog.com',
 ['zabhi1292@gmail.com' ])
        return HttpResponse('Thanks for contacting us!')
         
    else:
        form = EmailPostForm()
    return render(request, 'blogs/contact.html', { 'form': form})



def post_share7(request):
    return render(request, 'blogs/gallery.html')


def post_share8(request):
    return render(request, 'blogs/guneet.html')

def post_share10(request):
    return render(request, 'blogs/kunal.html')

def post_share11(request):
    return render(request, 'blogs/portfolio.html')

def post_share12(request):
    return render(request, 'blogs/tanishq.html')

def post_share13(request):
    return render(request, 'blogs/utkrisht.html')


                                                   
