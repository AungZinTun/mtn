from django.urls import path

from . import views

urlpatterns = [
    path('', views.CaseList.as_view(), name='case_list'),
    path('new/', views.CaseCreate.as_view(), name='new'),
    path('case/<int:pk>', views.CaseView.as_view(), name='case_detail')
]