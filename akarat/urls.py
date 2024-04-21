from django.urls import path
from .views import fetch_biens_immobiliers,favorie_biens,sing_in,create_user,profile_list,fetch_user,biens_immobiliers_list,create_biens_immobiliers
from django.conf.urls.static import static

from django.conf import settings
urlpatterns = [
    path('create_user/', create_user, name='create_user'),
    path('login/', sing_in, name='sing_in'),

    path('user_list/', profile_list, name='profile_list'),
    path('favorie/', favorie_biens, name='favorie_biens'),
    path('create_biens_immobiliers/',create_biens_immobiliers , name='create_biens_immobiliers'),
    path('biens_immobiliers/', biens_immobiliers_list, name='biens_immobiliers_list'),
    path('fetch_biens_immobiliers/',fetch_biens_immobiliers, name='fetch_biens_immobiliers'),
    path('fetch_user/',fetch_user, name='fetch_user')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
