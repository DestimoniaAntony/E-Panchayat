from django.urls import path

from e_panchayath_app.staff_views import Indexview,Addproduct, View_Product,Reject


urlpatterns = [

    path('',Indexview.as_view()),
    path('addproduct',Addproduct.as_view()),
    path('viewproduct',View_Product.as_view()),
    path('remove',Reject.as_view()),
]


def urls():
    return urlpatterns, 'staff','staff'