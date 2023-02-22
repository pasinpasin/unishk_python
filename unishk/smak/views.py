from rest_framework import generics,viewsets,permissions
from .models import Fakulteti,Departamenti
from .serializers import FakultetiSerializer,DepartamentiSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_protect
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from django.contrib.auth import authenticate, login




@method_decorator(ensure_csrf_cookie,name="dispatch")
class getCSRFToken(APIView):
    permission_classes=(permissions.AllowAny,)
    def get (self,request,format=None):
        return Response({ "success":"cookie set"})
    
@method_decorator(ensure_csrf_cookie,name="dispatch")
class checkAuthenticatedView(APIView):
    def get (self,request,format=None):
        try:
            isAuthenticated= User.is_authenticated
            if isAuthenticated:
                return Response({ "isAuthenticated":"success"}

                )
            else:
                return Response({ "isAuthenticated":"error"}

                )
        except:
            return Response({ "error":"something went wrong"})

        
@method_decorator(ensure_csrf_cookie,name="dispatch")
class LoginView(APIView):
    def post (self,request,format=None):

        data=self.request.data
        username=data['username']
        password=data['password']
        try:
            user=authenticate(username=username,password=password)
            
            if user is not None:
                login(request,user)
                return Response({ "success":"User authenticated","username":username}

                )
            else:
                return Response({ "error":"error authenticating"}

                )
        except:
             return Response({ "error":"something went wrong"})


            
        



class FakultetiListView(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Fakulteti.objects.all()
    serializer_class = FakultetiSerializer

class FakultetiViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Fakulteti.objects.all()
    serializer_class = FakultetiSerializer
    

class FakultetiDetailView(generics.RetrieveAPIView):
    queryset = Fakulteti.objects.all()
    serializer_class = FakultetiSerializer

class DepartamentiListView(generics.ListAPIView):
    queryset = Departamenti.objects.all()
    serializer_class = DepartamentiSerializer



    
