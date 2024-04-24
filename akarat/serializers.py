from rest_framework import serializers
from .models import Profile, Biens_immobiliers, Favoris, Commentaires_et_évaluations, Notifications, Ville,Image

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['ProfileID', 'user', 'numero_tel']
 
class Biens_immobiliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biens_immobiliers
        fields = ['BienID', 'type_de_bien', 'prix', 'surface', 'nombre_de_salles_de_bains', 'nombre_de_salles_de_sals', 'description', 'date_publication','categorie','region','emplacement','adresse','id_user']
class FavorisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favoris
        fields = ['FavoriID', 'ProfileID', 'BienID']  

class Commentaires_et_évaluationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaires_et_évaluations
        fields = ['CommentaireID', 'ProfileID', 'BienID', 'Commentaire', 'Évaluation', 'Date']  

class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = ['NotificationID', 'ProfileID', 'Contenu', 'Date']

class VillesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ville
        fields = ['VilleID', 'Nom_ville']
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['imageID', 'image', 'BienID']