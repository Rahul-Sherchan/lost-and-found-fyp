from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # This handles the root URL: http://127.0.0.1:8000/
    path('lost/', views.lost_items_list, name='lost_items'),
    path('found/', views.found_items_list, name='found_items'),
    path('item/<str:item_type>/<int:item_id>/', views.item_detail, name='item_detail'),
    path('report/lost/', views.report_lost_item, name='report_lost'),
    path('report/found/', views.report_found_item, name='report_found'),
    path('my-reports/', views.my_reports, name='my_reports'),
]