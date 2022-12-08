from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import  forms
from .models import Product, Contact, Order, Updateorder

class UserCreation(UserCreationForm):

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        widgets= {'username':forms.TextInput(attrs={'class':'form-control','name':"name" ,'placeholder':"Enter Your Username"}),
                  'first_name': forms.TextInput(
                      attrs={'class': 'form-control',  'placeholder': "Enter Your First Name"}),
                  'last_name': forms.TextInput(
                      attrs={'class': 'form-control',  'placeholder': "Enter Your Last Name"}),
                  'email': forms.EmailInput(
                      attrs={'class': 'form-control',  'placeholder': "Enter Your Email"}),


                  }
class UserChange(UserChangeForm):
    password = None
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ['username','first_name','last_name','email','date_joined']

class AdminChange(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = User
        fields = '__all__'


class ProductForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':"card-img-top img-fluid"}), required=False)

    class Meta:
        model = Product
        fields = '__all__'
        # widgets = {'pub_date':forms.Da


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class UpdateOrderForm(forms.ModelForm):
    class Meta:
        model = Updateorder
        fields = '__all__'

