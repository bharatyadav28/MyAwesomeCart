from django.urls import path
from . import views
urlpatterns = [

    path('',views.index, name= "ShopHome"),
    path('about/',views.about, name= "AboutUs"),
    path('contact/',views.contact, name= "ContactUs"),
    path('tracker/',views.tracker, name= "TrackingStatus"),
    path('search/',views.search, name= "Search"),
    path('products/<int:myid>',views.productview, name= "ProductView"),
    path('checkout/',views.checkout, name= "CheckOut"),


    path('signup/',views.sign_up, name= "signup"),
    path('login/',views.user_login, name= "login"),
    path('logout/',views.user_logout, name= "logout"),
    path('changepassword/',views.change_password, name= "changepassword"),
    path('viewprofile/',views.view_profile, name= "viewprofile"),
    path('admin_view_profile/<int:id>/',views.admin_view_profile, name= "admin_view_profile"),
    path('check/',views.check, name= "check"),
    path('deleterecord/<int:myid>',views.delete_record, name= "deleterecord"),
    path('updaterecord/<int:myid>',views.update_record, name= "updaterecord"),
]