from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *


 #class Logout(APIView):

    #def get(self, request, format=None):
        #request.user.auth_token.delet()
        #return Response(status=status.HTTP_200_OK)


class orderListView(generics.ListAPIView):
    serializer_class = orderListSerializer
    queryset = Order.objects.all()


class addOrder(generics.CreateAPIView):
    serializer_class = CreateOrderSerializer
    queryset = Order.objects.all()
    # permissions_class = IsAuthenticatedOrReadOnly


class orderUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = CreateOrderSerializer
    queryset = Order.objects.filter()
    # permissions_class = IsAuthenticatedOrReadOnly


class orderDestroyView(generics.DestroyAPIView):
    serializer_class = OrderRetrieveSerializer
    queryset = Order.objects.filter()


class orderRetrieveView(generics.RetrieveAPIView):
    serializer_class = OrderRetrieveSerializer
    queryset = Order.objects.filter()
    # permissions_class = IsAuthenticatedOrReadOnly


class piesListView(generics.ListAPIView):
    serializer_class = piesListSerializer
    queryset = Pies.objects.all()


class addPies(generics.CreateAPIView):
    serializer_class = CreatePiesSerializer
    queryset = Pies.objects.all()
    # permissions_class = IsAuthenticatedOrReadOnly


class piesUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = CreatePiesSerializer
    queryset = Pies.objects.filter()
    # permissions_class = IsAuthenticatedOrReadOnly


class piesDestroyView(generics.DestroyAPIView):
    serializer_class = PiesRetrieveSerializer
    queryset = Pies.objects.filter()
    # permissions_class = IsAuthenticatedOrReadOnly


class piesRetrieveView(generics.RetrieveAPIView):
    serializer_class = PiesRetrieveSerializer
    queryset = Pies.objects.filter()
    # permissions_class = IsAuthenticatedOrReadOnly


class userListView(generics.ListAPIView):
    serializer_class = userListSerializer
    queryset = User.objects.all()
    # permissions_class = IsAuthenticatedOrReadOnly


class addUser(generics.CreateAPIView):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()
    # permissions_class = IsAuthenticatedOrReadOnly


class userUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = CreatePiesSerializer
    queryset = User.objects.filter()
    # permissions_classes = IsAuthenticatedOrReadOnly


class userRetrieveView(generics.RetrieveAPIView):
    serializer_class = UserRetrieveSerializer
    queryset = User.objects.filter()
    # permissions_classes = IsAuthenticatedOrReadOnly
