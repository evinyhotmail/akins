from django.urls import path
from rest_framework_simplejwt import views as jwt_views


from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('drone/all', views.drone_list, name='drone_list'),
    path('drone/add', views.drone_add, name='drone_add'),
    path('drone/<int:pk>', views.drone_detail, name='drone_detail'),




    # TODO: To use in the future with Angular in order to provide a JWT
    path('token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),

]
