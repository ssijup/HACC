from django.shortcuts import render, redirect
from phase1.forms.users import AdvocateRegistrationForm
from django.views import View
from .models import Advocates
from instamojo_wrapper import Instamojo
from django.conf import settings
from .utilities import get_client
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login




api = Instamojo(api_key=settings.API_KEY, auth_token=settings.AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/')


class RequestMembershipView(View):
    def get(self, request):
        form = AdvocateRegistrationForm()
        return render(request, 'request_membership.html', {'form': form})
    
    def post(self, request):
        form = AdvocateRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
                form.save()
                print("inside valid")
                return redirect('pending')
        else:
            print("inside invalid")
            return render(request, 'request_membership.html', {'form': form})


def members(request):
    members = Advocates.objects.filter(active=True)
    return render(request, 'members.html',{'members':members})

def membership_payment(request):
    return render(request, 'membership_payment.html')

def advocates_dashboard(request):
    if 'name' in request.session:
        try:
            member  = Advocates.objects.get(name=request.session['name'])
            print(member)
            print(member.fee_paid)
        except:
            return redirect(request, 'members_login')
        return render(request,'advocates_dashboard.html',{'member':member})
    else:
        return redirect(request, 'members_login')
def advocates_dashboard_more(request):
    if 'name' in request.session:
        return render(request,'advocates_dashboard_more.html')
    else:
        return redirect(request, 'members_login')

class MembersLoginView(View):
    def get(self, request):
        return render(request, 'members_login.html')
    
    def post(self, request):
        name = request.POST.get('username')
        password = request.POST.get('password')
        print(name)
        print(password)
        try:
            user = Advocates.objects.get(name=name,password=password)
            print("check11")
        except:
            try:
                print("check22")

                user = User.objects.get(username=name)
                password_matches = check_password(password, user.password)
                if(password_matches):
                    login(request, user)
                    request.session['username'] = user.username
                    return redirect("admin_dashboard")

            except:
                print("check33")
                return redirect('members_login')
            print("check44")
            return redirect('admin_dashboard')

        request.session['name'] = name
        return redirect('advocates_dashboard')


def website_active(request):
    if 'name' in request.session:
        name = request.session['name']
        Advocates.objects.filter(name=name).update(website=True)
        return redirect('website')
    else:
        return redirect('members')

    
def website_payment(request):
    name = request.session['name']
    response = api.payment_request_create(
    amount='9500',
    purpose='Website Service',
    send_email=True,
    email="foo@example.com",
    redirect_url="http://127.0.0.1:8000/"
    )

    print(response)
    # print(response['payment_request']['longurl'])
    # print(response['payment_request']['id'])

    payment_request_id = response['payment_request']['id']

    payment_status_response = api.payment_request_status(payment_request_id)
    payment_status = payment_status_response['payment_request']['status']

    
    name = Advocates.objects.filter(name=name).update(website=True)

    return render(request, 'website_payment.html', context = {
        'payment_url' : response['payment_request']['longurl']
    })


def website(request):
    client = get_client(request)
    try:
        members = Advocates.objects.get(name=client,website=True)
    except:
        return redirect('error404')
    return render(request, 'website.html',{'members':members})

def error404(request):
    return render(request, 'error404.html')


def membership_payment(request):
    # name = request.session['name']
    response = api.payment_request_create(
    amount='5000',
    purpose='Membership fee',
    send_email=True,
    email="foo@example.com",
    redirect_url="name.localhost:8000/pending/"
    )


    # print(response['payment_request']['longurl'])
    # print(response['payment_request']['id'])

    payment_request_id = response['payment_request']['id']

    payment_status_response = api.payment_request_status(payment_request_id)
    payment_status = payment_status_response['payment_request']['status']

    
    # name = Advocates.objects.filter(name=name).update(website=True)

    return render(request, 'membership_payment.html', context = {
        'payment_url' : response['payment_request']['longurl']
    })

def pending(request):
    return render(request, 'pending.html')

def admin_dashboard(request):
    members = Advocates.objects.all()
    return render(request, 'admin_dashboard.html',{'members':members})


def members_logout(request):
    if 'name' in request.session:
        del request.session['name']
    return redirect('members_login')
