from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('page1',views.page1,name='page1'),
    path('editcon/<int:pk>',views.editcon,name='editcon'),
    path('pay',views.pay,name='pay'),
    path('editpay<int:pk>',views.editpay,name='editpay'),
    path('rec',views.rec,name='rec'),
    path('editrec<int:pk>',views.editrec,name='editrec'),
    path('jou',views.jou,name='jou'),
    path('editjou<int:pk>',views.editjou,name='editjou'),
    path('sal',views.sal,name='sal'),
    path('pur',views.pur,name='pur'),
    path('daybook',views.daybook,name='daybook'),
    path('daybookcon',views.daybookcon,name='daybookcon'),
    path('daybookpay',views.daybookpay,name='daybookpay'),
    path('daybookrec',views.daybookrec,name='daybookrec'),
    path('daybookjou',views.daybookjou,name='daybookjou'),
    path('delcon<int:pk>',views.delcon,name='delcon'),
    path('delpay<int:pk>',views.delpay,name='delpay'),
    path('delrec<int:pk>',views.delrec,name='delrec'),
    path('deljou<int:pk>',views.deljou,name='deljou')
]
   