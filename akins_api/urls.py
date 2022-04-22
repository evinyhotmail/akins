from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from . import views


urlpatterns = [

    path('', views.ApiOverview, name='home'),
    path('drones/', views.drone_list.as_view(), name='drone_list'),
    path('drone/<int:pk>', views.drone_crud, name='drone_crud'),
    path('camera/', views.camera_view.as_view(), name='camera_search'),



    # TODO: To use in the future with Angular in order to provide a JWT
    path('token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),

]
