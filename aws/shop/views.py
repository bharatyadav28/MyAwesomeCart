from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Product, Contact, Order, Updateorder
from math import ceil
import numpy as np
from .forms import UserCreation, UserChange, AdminChange,ProductForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate, update_session_auth_hash
import json
from django.contrib import messages


# Create your views here.

def sign_up(request):
    '''Sign Up neww user'''
    if request.method == 'POST':
        form = UserCreation(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"SignUp successfull!!!")
            form = UserCreation()

    else:
        form = UserCreation()
    return render(request,'shop/sign_up.html',{'form':form})

def user_login(request):
    ''' Authenticate the User'''
    if not  request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    user_login=True

                    return HttpResponseRedirect('/shop/')
        else:
            form = AuthenticationForm()
        return render(request,'shop/login.html',{'form': form})
    else:
        return HttpResponseRedirect('/shop/')


def user_logout(request):
    ''' log Out the user if already logged in'''
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/shop/login/')

def change_password(request):
    ''' Change the account Password of the User'''
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm( request.user,data=request.POST )
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,request.user)
                messages.success(request, "Updated successfull!!!")
                return HttpResponseRedirect('/shop/')

        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'shop/changepassword.html', {'form': form})


def view_profile(request):
    if request.method == 'POST':
        if request.user.is_superuser:
            all_users = User.objects.all()
            form = AdminChange(instance=request.user, data=request.POST)
        else:
            form = UserChange(instance=request.user, data=request.POST)
            all_users = None
        if form.is_valid():
            form.save()
            messages.success(request,"Updated Succesfully!!!")
    else:
        if request.user.is_superuser:
            form = None
            # form = AdminChange(instance=request.user)
            all_users = User.objects.all()
        else:
            form = UserChange(instance=request.user)
            all_users = None
    return render(request,'shop/userprofile.html',{'form': form, 'all_users':all_users})


def admin_view_profile(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AdminChange(instance=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Updated Succesfully!!!")
        else:
            data = User.objects.get(pk=id)
            form = AdminChange(instance=data)
        return render(request, 'shop/admin_view_profile.html', {'form': form,})



def check(request):
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Created successfully!!!")


    else:
        form = ProductForm()
    all_products = Product.objects.all()

    return render(request, 'shop/check.html', {'form': form,'all_products':all_products})

# def updateorviewproducts(request):
#     all_products = Product.objects.all()
#     form = ProductForm()
#     return render(request, 'shop/check.html', {'form': form, })


def delete_record(request, myid):
    print("id",myid)
    data = Product.objects.get(pk=myid)
    data.delete()
    messages.success(request, "Deleted successfull!!!")
    all_products = Product.objects.all()
    form =ProductForm()
    return render(request, 'shop/check.html', {'form': form, 'all_products': all_products})


def update_record(request, myid):
    if request.method == 'POST':

        form = ProductForm(request.POST)

        if form.is_valid():
            product_name = form.cleaned_data['product_name']
            desc= form.cleaned_data['desc']
            cateogry = form.cleaned_data['Cateogry']
            subcateogry = form.cleaned_data['subcateogry']
            price = form.cleaned_data['price']
            pub_date = form.cleaned_data['pub_date']
            # image = form.cleaned_data['image']
            # print("image",image)
            stu = Product(id=myid,product_name=product_name, desc=desc,Cateogry=cateogry,subcateogry=subcateogry,price=price,pub_date=pub_date,)
            stu.save()
            messages.success(request, "Updated Successfully!!!")

    else:
        data = Product.objects.get(pk=myid)
        form = ProductForm(instance= data)
    return render(request, 'shop/update.html', {'form': form})

def index(request):
    if request.user.is_authenticated:
        products = Product.objects.all()
        n = len(products)
        nslides = n // 4 * ceil((n / 4) - (n // 4))

        cateogries = []
        for product in products:
            cateogries.append(product.Cateogry)
        cateogries = np.array(cateogries)
        cateogries = np.unique(cateogries)
        # form = ProductForm()

        params = {"products": products, "no_of_slides": nslides, "range": range(1, nslides), "cateogries": cateogries}

        return render(request, "shop/index.html", params)

    else:
        return HttpResponseRedirect('/shop/login/')


def about(request):
    # return HttpResponse("We are at about")


    return render(request, "shop/about.html")


def productview(request, myid):
    product = Product.objects.filter(id=myid)
    return render(request, "shop/productview.html", {"product": product[0]})


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        query = request.POST.get('query')
        contact = Contact(name=name, email=email, phone=phone, query=query)
        contact.save()
        submitted = True
        id = contact.query_id
        return render(request, "shop/contactus.html", {"submitted": submitted, "id": id})

    return render(request, "shop/contactus.html")

def checkout(request):
    if request.method == "POST":
        json_items = request.POST.get('json_items')
        name = request.POST.get('name')
        email = request.POST.get('email')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')

        order = Order(json_items=json_items, name=name, email=email, address1=address1, address2=address2, city=city,
                      state=state, zip=zip)
        order.save()
        ordered = True
        id = order.order_id

        update_order = Updateorder(order_id =id, update_desc="The order has been placed" )
        update_order.save()

        return render(request, "shop/checkout.html", {"ordered": ordered, "id": id})

    return render(request, "shop/checkout.html")


def tracker(request):

    if request.method =="POST":

        order_id = request.POST.get('orderId')
        status = Updateorder.objects.filter(order_id= order_id)
        submitted = True
        update_table = []
        for i in status:
            # reversing the list
            update_table.insert(0, i)
        print(update_table)

        return render(request, "shop/tracker.html", {"order": update_table,"submitted": submitted})



    return render(request, "shop/tracker.html")


def search(request):
    # return HttpResponse("We are at search")
    return render(request, "shop/search.html")


