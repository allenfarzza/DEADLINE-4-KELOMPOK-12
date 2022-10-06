from django.urls import path
from .  import views

urlpatterns = [
    path('dataproduk', views.dataproduk, name='dataproduk'),
    path('createproduk', views.createproduk, name='createproduk'),
    path('updateproduk/<str:id>', views.updateproduk, name='updateproduk'),
    path('deleteproduk/<str:id>', views.deleteproduk, name='deleteproduk'),

    #Karyawan
    path('datakaryawan', views.datakaryawan, name='datakaryawan'),
    path('createkaryawan', views.createkaryawan, name='createkaryawan'),
    path('updatekaryawan/<str:id>', views.updatekaryawan, name='updatekaryawan'),
    path('deletekaryawan/<str:id>', views.deletekaryawan, name='deletekaryawan'),

    #Pembelian
    path('datapembelian', views.datapembelian, name='datapembelian'),
    path('createpembelian', views.createpembelian, name='createpembelian'),
    path('updatepembelian/<str:id>', views.updatepembelian, name='updatepembelian'),
    path('deletepembelian/<str:id>', views.deletepembelian, name='deletepembelian'),

    #Penjualan
    path('datapenjualan', views.datapenjualan, name='datapenjualan'),
    path('createpenjualan', views.createpenjualan, name='createpenjualan'),
    path('updatepenjualan/<str:id>', views.updatepenjualan, name='updatepenjualan'),
    path('deletepenjualan/<str:id>', views.deletepenjualan, name='deletepenjualan'),

    #Detail Pembelian
    path('createdetailpembelian/<str:id>', views.createdetailpembelian, name='createdetailpembelian'),
    path('createdetailpenjualan/<str:id>', views.createdetailpenjualan, name='createdetailpenjualan'),

    path("", views.dashboard,name='dashboard')
]

