from django.urls import path, include
from .views import urun_siparis_olustur, musteri_siparis_getir



urlpatterns = [
    path('urun_siparis_olustur/', urun_siparis_olustur, name='urun_siparis_olustur'),
     path('musteri_siparis_getir/<int:pk>/', musteri_siparis_getir, name='musteri-siparis-getir')
]