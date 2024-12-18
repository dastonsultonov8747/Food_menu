from django.urls import path
from . import views

urlpatterns = [
    path('', views.bigmenu_list, name='bigmenu_list'),
    path('cart/', views.cart_view, name='cart_view'),
    path('smallmenu/<int:pk>/', views.smallmenu_detail, name='smallmenu_detail'),
    path('bigmenu/', views.bigmenu_list, name='bigmenu_list'),
    path('bigmenu/<int:pk>/', views.bigmenu_detail, name='bigmenu_detail'),
    path('smallmenu/', views.smallmenu_detail, name='smallmenu_list'),
    path('smallmenu/<int:pk>/', views.smallmenu_detail, name='smallmenu_detail'),
    path('api/bigmenu/', views.BigMenuListView.as_view(), name='BigMenu_list'),
    path('api/bigmenu/<int:pk>/', views.BigMenuDetailView.as_view(), name='BigMenu_detail'),
    path('api/smallmenu/', views.SmallMenuListView.as_view(), name='SmallMenu_list'),
    path('api/smallmenu/<int:pk>/', views.SmallMenuDetailView.as_view(), name='SmallMenu_detail'),
    path('api/product/', views.ProductListView.as_view(), name='Product_list'),
    path('api/product/<int:pk>/', views.ProductDetailView.as_view(), name='Product_detail'),
]
