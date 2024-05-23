from django.urls import path
from .views import *

urlpatterns = [
    path('helloworld/', hello_world, name='hellowworrld'),
    path('productlist/',productlist,name='productlist'),
    path('detalislist/',detailslist,name='detailslist'),
    path('productadd/',productadd,name='productadd'),
    path('detailsadd/',detailsadd,name='detailsadd'),
    path('productview/<int:product_id>/',productview,name='productview'),
    path('detailsview/<int:details_id>/',detailsview,name='detailsview'),
    path('product_delete/<int:product_id>', product_delete,name=' product_delete'),
    path('details_delete/<int:detail_id>',details_delete,name='details_delete'),
    path('productedit/<int:product_id>/',productedit,name='productedit'),
    path('detailsedit/<int:details_id>/',detailsedit,name="detailsedit"),
    path('productedit2/<int:product_id>/',productedit2,name="productedit2"),
    path('caradd/',caradd,name='caradd'),
    path('cardelete/<int:car_id>/',cardelete,name="cardelete"),
    path('caredit/<int:car_id>/',caredit,name="caredit"),
    path('caredit2/<int:car_id>/',caredit2,name='caredit2')

]