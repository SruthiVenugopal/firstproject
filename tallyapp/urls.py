from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('page1',views.page1,name='page1'),
    path('payment',views.payment,name='payment'),
    path('receipt',views.receipt,name='receipt'),
    path('journal',views.journal,name='journal'),
    path('daybook',views.daybook,name='daybook')
]
   