from django.urls import path
from .views import fetch_biens_immobiliers,delete_favorie,favorie_biens,liste_biens,create_favorie,sing_in,create_user,profile_list,fetch_user,biens_immobiliers_list,create_biens_immobiliers
from django.conf.urls.static import static

from django.conf import settings
urlpatterns = [
    path('create_user/', create_user, name='create_user'),
    path('login/', sing_in, name='sing_in'),

    path('user_list/', profile_list, name='profile_list'),
    path('favorie/', favorie_biens, name='favorie_biens'),
    path('create_favorie/', create_favorie, name='create_favorie'),
    path('delete_favorie/', delete_favorie, name='delete_favorie'),
    path('liste_biens/', liste_biens, name='liste_biens'),

    path('create_biens_immobiliers/',create_biens_immobiliers , name='create_biens_immobiliers'),
    path('biens_immobiliers/', biens_immobiliers_list, name='biens_immobiliers_list'),
    path('fetch_biens_immobiliers/',fetch_biens_immobiliers, name='fetch_biens_immobiliers'),
    path('fetch_user/',fetch_user, name='fetch_user')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
