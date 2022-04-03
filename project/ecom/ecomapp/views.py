from django.shortcuts import render
from django.http import HttpResponse

from .utils import upload_file
from .forms import SignupForm

# Create your views here.


def ecomp(request):
    if request.method == 'POST':
        Signup = SignupForm(request.POST, request.FILES)
        if Signup.is_valid():
            # lets do something
            # print (request.FILES['profile_image'])
            upload_file(request.FILES['profile_image'])
            #return HttpResponse("login.html")
            return render(request, "login.html")
        else:
            return render(request, 'signup.html', {'form': Signup})
    else:
        Signup = SignupForm()

    return render(request, "signup.html", {"form": Signup})