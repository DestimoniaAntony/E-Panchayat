from django.urls import path

from e_panchayath_app.admin_views import ApproveView, Indexview,Citizen_tableview, RejectView,Staff_tableview,AddServiceView,AppliedServicesview



urlpatterns = [

    path('',Indexview.as_view()),
    path('back',Indexview.as_view()),
    path('citizen_table',Citizen_tableview.as_view()),
    path('staff_table',Staff_tableview.as_view()),
    path('service',AddServiceView.as_view()),
    path('appliedserviceview',AppliedServicesview.as_view()),
    path('Approve',ApproveView.as_view()),
    path('Reject',RejectView.as_view()),
]


def urls():
    return urlpatterns, 'admin','admin'