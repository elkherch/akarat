from django.db import models
from django.conf import settings

class Profile(models.Model):
    ProfileID = models.AutoField(primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type_compte = models.CharField(max_length=20,null=True,)
    numero_tel = models.CharField(max_length=8)    
    facebook = models.CharField(max_length=20,null=True,)
    logo_profile = models.ImageField(upload_to='profile_logos/', blank=True, null=True)

    def get_username(self):
        return self.user.username , self.user.first_name , self.user.email

    def __str__(self):
        return f"{self.user.username}, {self.user.first_name}, {self.user.email}, {self.user.last_name}, {self.user.password}"

# Modèle Biens_immobiliers
class Biens_immobiliers(models.Model):
    BienID = models.AutoField(primary_key=True)
    type_de_bien = models.CharField(max_length=50)
    prix = models.CharField(max_length=80)
    surface = models.CharField(max_length=90)
    categorie = models.CharField(max_length=90, null=True, blank=True)
    adresse = models.CharField(max_length=90, null=True, blank=True)
    region = models.CharField(max_length=90, null=True, blank=True)
    emplacement = models.CharField(max_length=90, null=True, blank=True)
    nombre_de_salles_de_bains = models.IntegerField()
    nombre_de_salles_de_sals = models.IntegerField()
    description = models.CharField(max_length=200)
    date_publication = models.DateTimeField()
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
# Modèle Image
class Image(models.Model):
    imageID = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='property_images/')
    bien_immobilier = models.ForeignKey(Biens_immobiliers, on_delete=models.CASCADE)

class Ville(models.Model):
    VilleID = models.AutoField(primary_key=True)
    Nom_ville = models.CharField(max_length=100)
    def __str__(self):
        return self.Nom_ville
class Favoris(models.Model):
    FavoriID = models.AutoField(primary_key=True)
    ProfileID = models.ForeignKey(Profile, on_delete=models.CASCADE)
    BienID = models.ForeignKey(Biens_immobiliers, on_delete=models.CASCADE)

class Commentaires_et_évaluations(models.Model):
    CommentaireID = models.AutoField(primary_key=True)
    ProfileID = models.ForeignKey(Profile, on_delete=models.CASCADE)
    BienID = models.ForeignKey(Biens_immobiliers, on_delete=models.CASCADE)
    Commentaire = models.TextField()
    evaluation = models.IntegerField()
    Date = models.DateTimeField(auto_now_add=True)

class Notifications(models.Model):
    NotificationID = models.AutoField(primary_key=True)
    ProfileID = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Contenu = models.TextField()
    Date = models.DateTimeField(auto_now_add=True)
