from django.urls import path,include
from rest_framework import routers
from . import views

app_name = 'smak'

router = routers.DefaultRouter()
router.register('fakultetet', views.FakultetiViewSet)

urlpatterns = [
    
    #path('fakultetet/',views.FakultetiListView.as_view(),name='fakulteti_list'),
    path('fakulteti/<pk>/',views.FakultetiDetailView.as_view(),name='fakulteti_detail'),
    path('departamentet/',views.DepartamentiListView.as_view(),name='departamenti_list'),
    path('api-auth/',include('rest_framework.urls')),
    path('csrf_cookie/',views.getCSRFToken.as_view()),
    path('authenticated/',views.checkAuthenticatedView.as_view()),
    path('login/',views.LoginView.as_view()),
    path('', include(router.urls)),


    ]