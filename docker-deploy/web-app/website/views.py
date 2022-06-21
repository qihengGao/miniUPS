from email import message
import socket
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from . import forms
import website.models as md
from django.conf import settings  # 将settings的内容引进


def index(request):
    is_login = False
    if 'username' in request.session:
        is_login = True
    if (request.method == 'POST'):
        track_form = forms.TrackForm(request.POST)
        if track_form.is_valid():
            try:
                package = md.Package.objects.filter(
                    tracking_id=track_form.cleaned_data['trackingid']).first()
            except:
                package = None
            if package is None:
                error_message = 'The tracking number you entered is not valid. Please try again.'
                return render(request, 'index.html', locals())
            return redirect('website:track', id=package.tracking_id)
    else:
        track_form = forms.TrackForm()
    return render(request, 'index.html', locals())


def track(request, id):
    is_login = False
    if 'username' in request.session:
        is_login = True
    package = get_object_or_404(md.Package, tracking_id=id)
    if request.method == 'POST':
        # package_form = forms.PackageForm(request.POST)
        user_name = request.session['username']
        package.user = get_object_or_404(md.User, username=user_name)
        package.save()
        message = 'package successfully binded!'
    return render(request, 'track.html', locals())


def register(request):
    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']

            try:
                existed = md.User.objects.get(username=user_name)
            except:
                existed = None
            if existed is not None:
                error_message = 'username existed!'
                return render(request, 'register.html', locals())
            try:
                existed_email = md.User.objects.get(email=email)
            except:
                existed_email = None
            if existed_email is not None:
                error_message = 'email has been used by another user'
                return render(request, 'register.html', locals())
            if password != password2:
                error_message = 'passwords are not same!'
                return render(request, 'register.html', locals())
            current_user = md.User.objects.create(
                username=user_name, email=email, password=password)
            return redirect('/login')
    else:
        register_form = forms.RegisterForm()
    return render(request, 'register.html', locals())


def login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = md.User.objects.filter(username=user_name).first()
            if not user:
                error_message = 'user does not exist'
                return render(request, 'login.html', locals())
            else:
                if user.password == password:
                    request.session['username'] = user.username
                    request.session.set_expiry(99999999999)
                    return redirect('/index')
                else:
                    error_message = 'wrong email or password'
                    return render(request, 'login.html', locals())
    else:
        login_form = forms.LoginForm()
    return render(request, 'login.html', locals())


def logout(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return redirect('/index')

def resend(request, package_id):
    msg = "resend, " + str(package_id)
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('web-server', 8888))
        client.send(msg.encode('utf-8'))
        print(msg)
    except:
        error_message = 'lost connection to server!'
    return redirect('/orders')

def change_dest(request, package_id, truck_id):
    is_login = True
    if 'username' not in request.session:
        is_login = False
        return redirect('/login')
    if request.method == 'POST':
        dest_form = forms.DestAddrForm(request.POST)
        if dest_form.is_valid():
            package = md.Package.objects.filter(shipment_id=package_id).first()
            if package.status == 'loading' or package.status == 'in WH':
                x = dest_form.cleaned_data['x']
                y = dest_form.cleaned_data['y']
                msg = "change," + str(truck_id) + ',' + str(package_id) + \
                    ',' + str(x) + ',' + str(y)
                # send the change dest addr requst to back end
                try:
                    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    client.connect(('web-server', 8888))
                    client.send(msg.encode('utf-8'))
                    print("change destination: " + str(x) +' ,' + str(y))
                except:
                    error_message = 'lost connection to server!'
                    # return redirect('/orders')
                    return render(request, 'change_dest.html', locals())
            return redirect('/orders')
    else:
        dest_form = forms.DestAddrForm()
    return render(request, 'change_dest.html', locals())


def orders(request):
    is_login = True
    if 'username' not in request.session:
        is_login = False
        return redirect('/login')
    user = md.User.objects.get(username=request.session['username'])
    try:
        user_packages = md.Package.objects.filter(
            user=request.session['username']).order_by('tracking_id')
    except:
        user_packages = None
    tracking_list = []
    for package in user_packages:
        tracking_list.append(package.tracking_id)
    try:
        pac_items = md.Item.objects.filter(tracking_id__in=tracking_list)
    except:
        pac_items = None
    return render(request, 'orders.html', locals())


def account(request):
    is_login = True
    if 'username' not in request.session:
        is_login = False
        return redirect('/login')
    user = md.User.objects.get(username=request.session['username'])
    packages_num = md.Package.objects.filter(user=user.username).count()
    delivered_pac = md.Package.objects.filter(
        user=user.username).filter(status="delivered").count()
    return render(request, 'account.html', locals())
# def package_detail(request):
#     return
