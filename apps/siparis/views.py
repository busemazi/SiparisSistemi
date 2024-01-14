from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Siparis
from apps.urun.models import Urun
from .serializers import SiparisSerializer , UrunSiparisSerializer
from rest_framework.decorators import action
from apps.musteri.models import Musteri

from .serializers import SiparisSerializer
from apps.urun_siparis.serializers import UrunSiparisSerializer
from django.contrib.auth.decorators import login_required


@api_view(['POST'])
def urun_siparis_olustur(request):
    try:
        #Request bodynin içinden ürün id listesine ulaş.
        urun_detay = request.data.get('urun_detay', []) #eğer urun_ids boş ise boş liste oluştur dedik.

        # for item in urun_detay:
        #     urun= Urun.objects.filter(id=item['id'])
        #     urunler.append(urun)

        #idsi verilen ürünleri veritabında filtreleme yapılması:
        urunler = Urun.objects.filter(id__in=[item['id'] for item in urun_detay])

        #eğer gelen id sayısı ile veri tabanında filtrelenen id sayısı aynı değilse hata döner.
        if len(urunler) != len(urun_detay):

            return Response("Siparişinize eklediğiniz ürünlerin bir kısmı veri tabanında bulunmamaktadır.", status=status.HTTP_404_NOT_FOUND)
        
        #sipariş kaydı oluştrmak için body oluşturacağız.
        siparis_data = {
            'toplam_fiyat': request.data.get('toplam_fiyat', 0),
            'adres' : request.data.get('adres', None),
            'musteri': request.data.get('musteri', None),
        }

        siparis_serializer = SiparisSerializer(data=siparis_data)

        if siparis_serializer.is_valid():

            siparis = siparis_serializer.save()

            for urun_data in urun_detay:
                urun = Urun.objects.get(id=urun_data['id'])
                urun_siparis_data = {
                    'adet' : urun_data['adet'],
                    'urun': urun.id,
                    'siparis': siparis.id,
                    'fiyat': urun.fiyat * int(urun_data['adet']),
                }

                urun_siparis_serializer = UrunSiparisSerializer(data=urun_siparis_data)

                if urun_siparis_serializer.is_valid():

                    urun_siparis_serializer.save()
                   
                else:
                    siparis.delete()

                    return Response('Urun sipariş oluşturulurken hata oluştu.'+ urun_siparis_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            return Response('Sipariş başarıyla oluşturuldu', status=status.HTTP_200_OK)

        else:
            return Response(siparis_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response('Siparişiniz başarıyla oluşturuldu', status=status.HTTP_200_OK)

    except Exception as e:
        return Response(e, status= status.HTTP_400_BAD_REQUEST)
    
#Müşteri bazlı sipariş getirme
@api_view(['GET'])
def musteri_siparis_getir(request,pk):

    musteri = Musteri.objects.get(id=pk)

    if musteri == None:

        return Response({'error': 'Böyle bir müşteri bulunamadı.'}, status=status.HTTP_400_BAD_REQUEST)
    
    siparisler = Siparis.objects.filter(musteri=musteri)

    serialized_siparisler = SiparisSerializer(siparisler, many=True).data

    response_data = {
        'musteri_ad': musteri.ad ,
        'musteri_soyad' : musteri.soyad,
        'siparisler': serialized_siparisler
    }

    return Response(response_data, status=status.HTTP_200_OK)
