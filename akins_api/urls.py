from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from . import views

# defining the name of set of view with repective actions.
camera_list = views.CameraViewSet.as_view({
    'get': 'list'

})

urlpatterns = [

    path('', views.ApiOverview, name='home'),
    path('drones/', views.drone_list.as_view(), name='drone_list'),
    # FIXME: for future version include, remove it and add the method post in toe drone_crud view
    path('drone/add/', views.drone_add, name='drone_add'),
    path('drone/<int:pk>', views.drone_crud, name='drone_crud'),

    # Just to show how we can code lees... :)
    path('cameras/', camera_list, name='camera_list'),



    # TODO: To use in the future with Angular in order to provide a JWT
    path('token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),

]
