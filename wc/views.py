from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages, auth
from wc.models import shorturl,notuserurl
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import random
import string

# Create your views here.


def signin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            if request.POST['email'] and request.POST['password']:
                try:
                    user = User.objects.get(email=request.POST['email'])
                    auth.login(request, user)
                    messages.success(
                        request, "You are successfully loggedin now you can see your dashboard")
                    return redirect('dashboard')
                except User.DoesNotExist:
                    return render(request, 'signin.html', {'error': "User doesnot exists"})
            else:
                return render(request, 'signin.html', {'error': "Enter correct password or email address or username"})
        else:
            return render(request, 'signin.html')
    else:
        return redirect('/')


def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password2']:
            if request.POST['username'] and request.POST['email'] and request.POST['password']:
                try:
                    user = User.objects.get(email=request.POST['email'])
                    return render(request, 'signup.html', {'error': "User already exists"})
                except User.DoesNotExist:
                    user = User.objects.create_user(
                        username=request.POST['username'],
                        email=request.POST['email'],
                        password=request.POST['password'],
                    )
                    user.save()
                    messages.success(request, "Signup Successfully Logged In")
                    return redirect(signin)
            else:
                return render(request, 'signup.html', {'error': "Empty Fields"})
        else:
            return render(request, 'signup.html', {'error': "Password Don't Match"})
    else:
        return render(request, 'signup.html')
    return render(request, 'signup.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def randgenerate():
    return ''.join(random.choice(string.ascii_uppercase + string.digits +
                          string.ascii_lowercase) for _ in range(6))

def notgenerate(request):
    count =0
    if request.method == "POST":
        if request.POST['notoriginal']:
            notoriginal = request.POST['notoriginal']
            gen =False
            while not gen:
                short = randgenerate()
                check = notuserurl.objects.filter(short_url=short)
                if not (check and count==5):
                    newurl = notuserurl(original_url=notoriginal,short_url=short)
                    urls = notuserurl.objects.filter(short_url=short)
                    newurl.save()
                    return render(request, 'home.html', {'urls': urls})
                else:
                    continue
        else:
            pass
    else:
        pass
    return render(request, 'home.html', {'urls': urls})

@login_required(login_url='/signin/')
def generate(request):
    if request.method == "POST":
        if request.POST["original"] and request.POST['short']:
            usr = request.user
            original = request.POST['original']
            short = request.POST['short']
            check = shorturl.objects.filter(short_url=short)
            if not check:
                newurl = shorturl(
                    user=usr, original_url=original, short_url=short,)
                newurl.save()
                return redirect(dashboard)
            else:
                messages.error(request, "Your url is already exists")
                return redirect('/dashboard')
        elif request.POST['original']:
            usr = request.user
            original = request.POST['original']
            gen = False
            while not gen:
                short = randgenerate()
                check = shorturl.objects.filter(short_url=short)
                if not check:
                    newurl = shorturl(
                        user=usr, original_url=original, short_url=short)
                    newurl.save()
                    return redirect(dashboard)
                else:
                    continue
        else:
            messages.error(request, 'Empty Fields.Please fill that.')
            return redirect('/dashboard')
    else:
        return redirect('/dashboard')


@login_required(login_url='/signin/')
def dashboard(request):
    usr = request.user
    urls = shorturl.objects.filter(user=usr)
    return render(request, 'dashboard.html', {'urls': urls})

@login_required(login_url='/signin/')
def passgen(request):
    return render(request,'passgen.html')


def home(request, query=None):
    if not query or query is None:
        return render(request,'home.html')
    else:
        try:
            check = shorturl.objects.get(short_url=query)
            check.clicks = check.clicks + 1
            check.save()
            url_redirect = check.original_url
            return redirect(url_redirect)
        except shorturl.DoesNotExist:
            return render(request, 'home.html', {'error': 'Error'})