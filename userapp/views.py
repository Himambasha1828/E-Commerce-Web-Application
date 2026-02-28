from django.shortcuts import render , redirect
from .models import *
from datetime import datetime
# from django.db.models import Q
# Create your views here.
def home(req):
    try:
        user_id = req.COOKIES["user"]
        user = User.objects.get(id=user_id)
        products = Product.objects.all()
        return render(req, 'index.html',locals())
    except:
        return redirect('login')

def signup(req):
    if req.method == 'POST':
        name = req.POST.get("name")
        mail = req.POST.get("mail")
        phno = req.POST.get("phno")
        pswd1 = req.POST.get("pswd1")
        pswd2 = req.POST.get("pswd2")

        if not (User.objects.filter(email = mail).first()):
            if pswd1 == pswd2:
                User(name = name , email = mail , contact = phno , password = pswd1 ).save()
                return redirect("login")
            else:
                msg = "password and re-enterd password are not same"
        else:
            msg = "this Email have account ! please login !"
    return render(req, 'signup.html' , locals())

def login(req):
    if req.method == 'POST':
        mail = req.POST.get("email")
        pswd = req.POST.get("password")
        data = User.objects.filter(email = mail).first()
        if data:
            if data.password == pswd:
                res = redirect("home")
                res.set_cookie('user',data.id)
                return res
            else:
                msg = "Invalid Password"
        else:
            msg = "Invalid Email! please signup !"
        
    return render(req,"login.html", locals())

def kind(req,_type):
    try:
        user_id = req.COOKIES["user"]
        user = User.objects.get(id=user_id)
        products = Product.objects.filter(category = _type)
        return render(req, 'index.html',locals())
    except:
        return redirect('login')

def account(req):
    try:
        user_id = req.COOKIES["user"]
        user = User.objects.get(id=user_id)
        return render(req, 'account.html', locals())
    except:
        return redirect('login')

def update_profile(req):
    try:
        user_id = req.COOKIES["user"]
        user = User.objects.get(id=user_id)
        if req.method == 'POST':
            user.name = req.POST.get("name")
            user.email = req.POST.get("mail")
            user.contact = req.POST.get("phno")
            user.address  = req.POST.get("add")
            if req.FILES.get("img"):
                user.image =req.FILES.get("img")
            user.save()
            return redirect('account')
        return render(req,"user_update.html" , locals())

    except:
        return redirect('login')

def place_order(req,ele):
    try:
        user_id = req.COOKIES["user"]
        user = User.objects.get(id=user_id)
        product = Product.objects.get(id=ele)
        if req.method == 'POST':
            order = Order(
                name =  product.name,
                price = product.discount,
                address = [req.POST.get('name'), req.POST.get('city'),req.POST.get('state'),req.POST.get('country'), req.POST.get('pincode')],
                user_id = user_id,
                seller_id = product.seller_id,
                order_date = datetime.now(),
                image = product.image
            )
            order.save()
            msg = "order placed successfully"

        return render(req, 'place_order.html', locals())
    except:
        return redirect('login')
    
def orders(req):
    try:
        user_id = req.COOKIES["user"]
        user = User.objects.get(id=user_id)
        orders = Order.objects.filter(user_id=user_id)
        return render(req, 'orders.html', locals())
    except:
        return redirect('login')

def cart(req):
    try:
        user_id = req.COOKIES["user"]
        user = User.objects.get(id=user_id)
        cart = [ Product.objects.get(id=y) for y in [x.product_id for x in Cart.objects.filter(user_id=user_id)]]
        return render(req, 'cart.html', locals())
    except:
        return redirect('login')

def add_cart(req,ele):
    try:
        user_id = req.COOKIES["user"]
        user = User.objects.get(id=user_id)
        product = Product.objects.get(id=ele)
        Cart(user_id=user_id , product_id = product.id).save()
        return redirect("home")
    except:
        return redirect("login")

def remove_cart(req,ele):
    try:
        user_id = req.COOKIES["user"]
        user = User.objects.get(id=user_id)
        product = Cart.objects.get(product_id = ele , user_id = user_id)
        product.delete()
        return redirect("cart")
    except:
        return redirect("login")

def cancel_order(req,ele):
    try:
        user_id = req.COOKIES["user"]
        user = User.objects.get(id=user_id)
        order = Order.objects.get(id=ele)
        order.status = "cancelled"
        order.save()
        return redirect("orders")    
    except:
        return redirect('login')

def update_password(req):
    try:
        user_id = req.COOKIES["user"]
        user = User.objects.get(id=user_id)
        if req.method == 'POST':
            old_password = req.POST.get("old")
            new_password = req.POST.get("new")
            confirm_password = req.POST.get("con")
            if old_password == user.password:
                if new_password == confirm_password:
                    user.password = new_password
                    user.save()
                    return redirect('account')
                else:
                    msg = "new and re-enterd password not sync !!"
            else:
                msg = "old password not match !!"
        return render(req,"update_password.html" , locals())
    except:
        return redirect('login')

def search(req):
    # try:
        user_id = req.COOKIES["user"]
        user = User.objects.get(id=user_id)
        if req.method == 'GET':
            search = req.GET.get("search")
            products = Product.objects.filter(name__contains = search)
        return render(req,"index.html",locals())
    # except:
    #     return redirect('login')

def logout(req):
    res = redirect("login")
    user_id = req.COOKIES["user"]
    user = User.objects.get(id=user_id)
    user.logout = datetime.now()
    user.save()
    res.delete_cookie('user')
    return res