from django.urls import path

from e_panchayath_app.users_views import Indexview,Serviceview,RequestView,UpdateProfile,ApplyApplication,AppliedServicesStatusView,View_Productgallery


urlpatterns = [

    path('',Indexview.as_view()),
    path('path',Indexview.as_view()),
    path('applyservice',Serviceview.as_view()),
    path('apply',RequestView.as_view()),
    path('updateprofile',UpdateProfile.as_view()),
    path('applyapplication',ApplyApplication.as_view()),
    path('status',AppliedServicesStatusView.as_view()),
    path('gallery',View_Productgallery.as_view()),
]


def urls():
    return urlpatterns, 'users','users'