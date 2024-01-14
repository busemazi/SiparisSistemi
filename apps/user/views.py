from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import CustomUserSerializer

from apps.musteri.models import Musteri

@api_view(['POST'])
def register_user(request):
    try:
        serializer = CustomUserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            cinsiyet = request.data.get('cinsiyet', '')

            musteri = Musteri.objects.create(
                ad= user.first_name,
                soyad=user.last_name,
                cinsiyet=cinsiyet
            )

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as e:
       return Response (e, status=status.HTTP_400_BAD_REQUEST)