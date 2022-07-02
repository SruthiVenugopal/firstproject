from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('page1',views.page1,name='page1'),
    path('editcon/<int:pk>',views.editcon,name='editcon'),
    path('payment',views.payment,name='payment'),
    path('editpay<int:pk>',views.editpay,name='editpay'),
    path('receipt',views.receipt,name='receipt'),
    path('editrec<int:pk>',views.editrec,name='editrec'),
    path('journal',views.journal,name='journal'),
    path('editjou<int:pk>',views.editjou,name='editjou'),
    path('sales',views.sales,name='sales'),
    path('purchase',views.purchase,name='purchase'),
    path('daybook',views.daybook,name='daybook'),
    path('daybookcon',views.daybookcon,name='daybookcon'),
    path('daybookpay',views.daybookpay,name='daybookpay'),
    path('daybookrec',views.daybookrec,name='daybookrec'),
    path('daybookjou',views.daybookjou,name='daybookjou')
]
   