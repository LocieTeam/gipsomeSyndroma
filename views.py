from django.shortcuts import render
from rest_framework.parsers import JSONParser
from .serializers import AddEmployeeSerializer,ItemCheckSerializer,WebViewSerializer,ServeiSerializer,AdsRequestSerializer,DESerializer,AdvertismentSerializer,CR2FSerializer,ItemSerializer,OfferSerializer,OrderSerializer,RateSerializer,UsersSerializer,OTPSerializer,NotifierSerializer,BuissnessSerializer,AdminBaseSerializer,OptionsSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins,generics
from rest_framework.response import Response
import psycopg2
from django_filters.rest_framework import DjangoFilterBackend
from .models import Servei,AdsRequest,DE,Advertisment,CR2F,Item,Offer,Order,Rate,Rules,Users,OTP,Notifier,Buissness,AdminBase,Options,WebView



# Create your views here.
class ServeiView(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):

    """
        This is View is used for servei and my_employee,
        create, retreive and partial_update
        filter used : servei_id,employer
    """
    queryset = Servei.objects.all()
    serializer_class = ServeiSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['employer','allowed']
    lookup_field = 'servei_id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def partial_update(self,request,*args,**kwargs):
        kwargs['partial']=True
        return self.update(request,*args,**kwargs)

class AddEmployeeView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):

    """
      This view will specifically respond to AddEmployee

    """
    queryset = Servei.objects.all()
    serializer_class = AddEmployeeSerializer
    lookup_field = 'servei_id'

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def partial_update(self,request,*args,**kwargs):
        kwargs['partial']=True
        return self.update(request,*args,**kwargs)

class ItemCheckView(mixins.RetrieveModelMixin,generics.GenericAPIView):


    """
      This View will return data associated with the
      item in the view
      """
    queryset = Servei.objects.all()
    serializer_class = ItemCheckSerializer
    lookup_field = 'servei_id'

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

""" Views for servei ends here
    needed to add auth permissions and login and register power
"""

#####################################################################

"""
   AdsRequest and advertisment view
"""

class AdsRequestView(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):

    queryset = AdsRequest.objects.all()
    serializer_class = AdsRequestSerializer
    filer_backends = [DjangoFilterBackend]
    filterset_fields = ['status','servei_id','city_code']

    def get(self,request,*args,**kwargs):
        return self.retreive(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def partial_update(self,request,*args,**kwargs):
        kwargs['partial']=True
        return self.update(request,*args,**kwargs)

class AdvertismentView(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):

    queryset  = Advertisment.objects.all()
    serializer_class = AdvertismentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['plan','city_code','servei_id']

    def get(self,request,*args,**kwargs):
        return self.retreive(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def partial_update(self,request,*args,**kwargs):
        kwargs['partial']=True
        return self.update(request,*args,**kwargs)

"""
    Advertisment vieew ends here
 """
 #####################################################################

"""
   CR2F view for returning reports,review,feedbacks and concerns
   filterd by servei_id/de_id/order_id and type.
"""
class CR2FView(mixins.CreateModelMixin,mixins.RetrieveModelMixin,generics.GenericAPIView):

    queryset = CR2F.objects.all()
    serializer_class = CR2FSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['servei_id','item_id','de_id','order_id','type','user_id']

    def get(self,request,*args,**kwargs):
        return self.retreive(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class BuissnessReportView(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):

    queryset = Buissness.objects.all()
    serializer_class = BuissnessSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['customer_id','status']

    def get(self,request,*args,**kwargs):
        return self.retreive(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def partial_update(self,request,*args,**kwargs):
        kwargs['partial']=True
        return self.update(request,*args,**kwargs)

class OrderView(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'order_id'

    def get(self,request,*args,**kwargs):
        return self.retreive(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def partial_update(self,request,*args,**kwargs):
        kwargs['partial']=True
        return self.update(request,*args,**kwargs)

class NotifierView(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):

    queryset = Notifier.objects.all()
    serializer_class = NotifierSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['note_to','note_from','notify_state']


    def get(self,request,*args,**kwargs):
        return self.retreive(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def partial_update(self,request,*args,**kwargs):
        kwargs['partial']=True
        return self.update(request,*args,**kwargs)

class AdminBaseView(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):

    queryset = AdminBase
    serializer_class = AdminBaseSerializer
    lookup_field = 'id'

    def get(self,request,*args,**kwargs):
        return self.retreive(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def partial_update(self,request,*args,**kwargs):
        kwargs['partial']=True
        return self.update(request,*args,**kwargs)

class OptionsView(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):

    queryset = Options
    serializer_class = OptionsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','city_code','prev_option']

    def get(self,request,*args,**kwargs):
        return self.retreive(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def partial_update(self,request,*args,**kwargs):
        kwargs['partial']=True
        return self.update(request,*args,**kwargs)

class WebviewView(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):

    queryset = WebView
    serializer_class = WebViewSerializer
    filter_backends = [DjangoFilterBackend]
    lookup_field = 'web_view_id'
    filterset_fields = ['servei_id']

    def get(self,request,*args,**kwargs):
        return self.retreive(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def partial_update(self,request,*args,**kwargs):
        kwargs['partial']=True
        return self.update(request,*args,**kwargs)


# Login and Registration Views.......
############################################
############################################
################################################
