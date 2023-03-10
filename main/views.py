from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *
import json
import random
from adschlarship import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
def index(request):
    clickld = request.session.get('click')
    try:
        user=Clicks.objects.get(name=request.user)
    except:
        user=None
    if request.method =='POST':
        if request.user.is_authenticated:

            try:
                user=Clicks.objects.get(name=request.user)
            except:
                user=None
            if user is not None:
                user.number=user.number+1
                user.save()
            else:
                Nuser=Clicks(name=request.user,number=1)
                Nuser.save()
            if not clickld:
                pass
            else:
                user=Clicks.objects.get(name=request.user)
                user.number=int(user.number)+int(clickldint)
                user.save()
                request.session['click'] = 0
                print('Laban')
            return redirect('index')
        else:
            messages.error(request, f'Please LogIn, To keep your clicks safe')
            return redirect('index')
    if user is not None:
        dollar=((int(user.number)*3)/1000)
        click=user.number  
    else:
        dollar=0
        click=0
    Lists=[]
    List=[]

    lists=AdsLink.objects.all()
    if len(lists)>=3:
        for i in lists:
            List.append(i.name)
    else:
        pass
    Lists=random.sample(List, len(List))
    Lists=Lists[:3]
    context={'Lists':Lists,'List':List,'click':click,'dollar':dollar}
    return render(request, 'index.html',context)
@login_required(login_url='login')
def withdraw(request):
    form=WithdrawForm()
    try:
        user=Clicks.objects.get(name=request.user)
    except:
        user=None
    if user is not None:
        dollar=((int(user.number)*3)/1000)
        click=user.number  
    else:
        dollar=0
        click=0
    if request.method =='POST':
        form=WithdrawForm(request.POST)
        if form.is_valid():
            if not click:
                messages.error(request, f'Error, You either do not have any aquired clicks or rebort you device and try Again')
                return redirect('index')
            
            else:
                if click is None:
                    messages.error(request, f'Empty, ! No clicks available!!!, Please click "Click Ads" Button to make the Money.')
                    return redirect('index')
                else:
                    dollar=((int(click)*3)/1000)
                    if (int(dollar)>=int(form.cleaned_data['amount'])):
                        balance=(int(dollar)-int(form.cleaned_data['amount']))
                        click=((int(balance)*1000)/3)
                        request.session['click'] =click
                        print(request.session['click'])
                        feed_back=form.save(commit=False)
                        feed_back.customer=request.user
                        feed_back.save()
                        '''send_mail(subject,
                                f'',
                                settings.EMAIL_HOST_USER,
                                [f'{request.user.email}'],
                                fail_silently = True,
                                )'''
                        messages.success(request, f'Withdraw Request Made Successfully.You will be Contacted Soon.')
                        return redirect('index')
                    else:
                        messages.error(request, f'Insufficient Balance')
                        return redirect('withdraw')

    
    
    #List=json.dumps(List)
    Lists=[]
    List=[]
    lists=AdsLink.objects.all()
    if len(lists)>=3:
        for i in lists:
            List.append(i.name)
    else:
        pass
    Lists=random.sample(List, len(List))
    Lists=Lists[:3]
    context={'Lists':Lists,'click':click,'dollar':dollar,'form':form,'header':'Withdraw, Minimum $10','button':'Make Withdraw Request'}
    return render(request, 'form.html',context)




    # Create your views here.
def signin(request):
    try:
        user=Clicks.objects.get(name=request.user)
    except:
        user=None
    if user is not None:
        dollar=((int(user.number)*3)/1000)
        click=user.number  
    else:
        dollar=0
        click=0
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username,password=password)

        if user is not None:
            login(request,user)
            request.session['customer'] = user.id
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            else:
                messages.success(request, f'Welcome, {username}.You have Signed In Successfully')
                return redirect('index')
        else:
            print('else')
            messages.success(request, 'Username or Password Incorrect!')
            return redirect('login')
    form=LoginForm()

    #List=json.dumps(List)

    context={'click':click,'dollar':dollar,'form':form,'button':'LogIn'}
    return render(request,'form1.html',context)

def signup(response):
    try:
        user=Clicks.objects.get(name=request.user)
    except:
        user=None
    if user is not None:
        dollar=((int(user.number)*3)/1000)
        click=user.number  
    else:
        dollar=0
        click=0
    ref_name=response.POST.get('ref_name')
    if response.method=="POST":
        form=RegistrationForm(response.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            username=form.cleaned_data['username']
            try:
                referral_code=User.objects.get(username=ref_name)
            except:
                referral_code=None
            if referral_code:
                '''send_mail('AdsMoney Referral',
                    f'{username} Just Joined Using You as a Referral. \n Remember to claim your money. \n And refer more.',
                    settings.EMAIL_HOST_USER,
                    [f'{referral_code.email}'],
                    fail_silently = True,
                    )'''
                referreds=Referred(personwhorefferred=referral_code,personrefferred=username)
                referralbonus=ReferralBonu(person=referral_code,amount=30)
                referreds.save()
                referralbonus.save()
            form.save()
            messages.success(response, f'Successfully Registered,Please log into your Account and Start Earning')
            return redirect('login')
        else:
            messages.success(response, f'Invalid Form, Contact Admin for Assitance')
            return redirect('login')
    form=RegistrationForm()

    
    
    #List=json.dumps(List)

    context={'click':click,'dollar':dollar,'form':form,'button':'SignUp'}
    return render(response,'form.html',context)


@login_required(login_url='login')
def Logout(request):
    logout(request)
    messages.success(request, 'You have Signed Out Successfully')
    return redirect('index')
@login_required(login_url='login')
def claim(request):
    try:
        user=Clicks.objects.get(name=request.user)
    except:
        user=None
    if user is not None:
        dollar=((int(user.number)*3)/1000)
        click=user.number  
    else:
        dollar=0
        click=0
    clicks=ReferralBonu.objects.filter(person=request.user)
    #List=json.dumps(List)
    Lists=[]
    List=[]
    lists=AdsLink.objects.all()
    if len(lists)>=3:
        for i in lists:
            List.append(i.name)
    else:
        pass
    Lists=random.sample(List, len(List))
    Lists=Lists[:3]
    context={'Lists':Lists,'click':click,'clicks':clicks,}
    return render(request,'claim.html',context)

@login_required(login_url='login')
def claimid(request, id):
    try:
        user=Clicks.objects.get(name=request.user)
    except:
        user=None
    if user is not None:
        dollar=((int(user.number)*3)/1000)
        click=user.number  
    else:
        dollar=0
        click=0
    clicks=ReferralBonu.objects.get(id=id)
    if user is not None:
        user.number=int(clicks.amount)+int(click)
        user.save()
    else:
        number=int(clicks.amount)+int(click)
        Nuser=Clicks(name=request.user,number=number)
        Nuser.save()
    messages.success(request, 'Clicks CLaimed Successfully.')
    clicks.paid=True
    clicks.save()
    return redirect('claim')


@login_required(login_url='login')
def kyc(request):
    Lists=[]
    List=[]
    lists=AdsLink.objects.all()
    if len(lists)>=3:
        for i in lists:
            List.append(i.name)
    else:
        pass
    Lists=random.sample(List, len(List))
    Lists=Lists[:3]
    form=KYCForm()
    try:
        user=Clicks.objects.get(name=request.user)
    except:
        user=None
    if user is not None:
        dollar=((int(user.number)*3)/1000)
        click=user.number  
    else:
        dollar=0
        click=0
    if request.method =='POST':
        if form.is_valid():
            feed_back=form.save(commit=False)
            feed_back.name=request.user
            feed_back.save()
            messages.success(request, 'KYC Submission Complete')
            return redirect('index')
    context={'Lists':Lists,'click':click,'dollar':dollar,'form':form,'header':'KYC FORM','button':'SUBMIT'}
    return render(request, 'form2.html',context)

