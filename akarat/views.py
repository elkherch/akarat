from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

import json
from .models import Profile, Biens_immobiliers, Favoris, Commentaires_et_évaluations, Notifications, Ville
from .serializers import ProfileSerializer, Biens_immobiliersSerializer,Image, FavorisSerializer, Commentaires_et_évaluationsSerializer, NotificationsSerializer, VillesSerializer
from django.views.decorators.csrf import csrf_exempt

@api_view(['GET', 'POST'])
def profile_list(request):
    if request.method == 'GET':
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # Logique pour gérer la création d'un nouveau profil
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

@api_view(['POST'])
def create_user(request):
    data = request.data
    
    user_data = {
        'username': data['username'],
        'first_name': data['first_name'],
        'email': data['email'],
        'password': data['password']
    }
    
    # Créer l'utilisateur
    user = User.objects.create_user(**user_data)

    profile_data = {
        'user': user.id,  # Utiliser l'identifiant de l'utilisateur
        'type_compte': data['type_compte'],
        'numero_tel': data['numero_tel'],
        'facebook': data['facebook'],
    }

    serializer = ProfileSerializer(data=profile_data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)
@api_view(['POST'])
@csrf_exempt
def sing_in(request):
    if request.method == "POST":  # Vérifie si la méthode est POST
        data = json.loads(request.body.decode('utf-8'))  # Extrait les données JSON de la requête
        username = data.get('username', None)  # Extrait le nom d'utilisateur de données JSON
        password = data.get('password', None)  # Extrait le mot de passe de données JSON

        # Authentification de l'utilisateur avec les identifiants fournis
        authenticated_user = authenticate(request, username=username, password=password)

        if authenticated_user:  # Si l'authentification réussit
            # Retourne une réponse JSON avec le succès et l'ID de l'utilisateur
            return JsonResponse({"success": True, "user_id": authenticated_user.id})
        else:
            # Si l'authentification échoue, retourne une réponse JSON avec un message d'erreur
            return JsonResponse({'message': "Invalid credentials.", "success": False})

    # Si la méthode de la requête n'est pas POST, renvoie une réponse indiquant que cette méthode n'est pas autorisée
    return HttpResponse("This method is not a POST")
@api_view(['POST'])
@csrf_exempt
def fetch_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            iduser = data.get('iduser')
            users = Profile.objects.filter(user=iduser)

            _list_users = []
            for profile in users:
                utilisateur = profile.user
                user = User.objects.get(id=utilisateur.id)

                bien_data = {
                    
                    'type_compte': profile.type_compte,
                    'numero_tel': profile.numero_tel,
                    'facebook': profile.facebook,
                    'username': user.username,
                    'first_name': user.first_name,
                    'email': user.email,
                }
                _list_users.append(bien_data)

            print(_list_users)
            return JsonResponse({'list_biens': _list_users}, safe=False, status=200)
        except json.decoder.JSONDecodeError as e:
            return JsonResponse({'error': 'Erreur lors du décodage des données JSON.'}, status=400)
    else:
        return Response(status=404)

@api_view(['POST'])
def create_biens_immobiliers(request):
    data = request.data
    bien_data = {
        'type_de_bien': data.get('type_de_bien'),
        'prix': float(data.get('prix', 0)),  # Convertir en float ou gérer les erreurs
        'surface': int(data.get('surface', 0)),  # Convertir en int ou gérer les erreurs
        'nombre_de_salles_de_bains': int(data.get('nombre_de_salles_de_bains', 0)),
        'nombre_de_salles_de_sals': int(data.get('nombre_de_salles_de_sals', 0)),
        'description': data.get('description'),
        'date_publication': data.get('date_publication'),
        'lien': data.get('lien'),
        'id_user': data.get('id_user'),
    }

    serializer = Biens_immobiliersSerializer(data=bien_data)
    if serializer.is_valid():
        bien_immobilier = serializer.save()

        # Récupérer les fichiers téléchargés
        images = request.FILES.getlist('images')

        # Enregistrer les images associées au bien immobilier
        for image in images:
            Image.objects.create(image=image, bien_immobilier=bien_immobilier)
        
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)




@api_view(['GET'])
@csrf_exempt
def biens_immobiliers_list(request):
    biens_immobiliers = Biens_immobiliers.objects.all()
    
    _list_biens = []
    
    for bien in biens_immobiliers:
        # Récupérer toutes les images associées à ce bien immobilier
        images = Image.objects.filter(bien_immobilier=bien)
        
        # Liste des URLs des images associées à ce bien immobilier
        image_urls = [image.image.url for image in images]
        
        # Ajouter les détails du bien immobilier et la liste des URLs des images à la liste
        _list_biens.append({
            'bienID': bien.BienID,
            'type_de_bien': bien.type_de_bien,
            'prix': bien.prix,
            'surface': bien.surface,
            'nombre_de_salles_de_bains': bien.nombre_de_salles_de_bains,
            'nombre_de_salles_de_sals': bien.nombre_de_salles_de_sals,
            'images': image_urls,  # Liste des URLs des images associées
            'description': bien.description,
            'lien': bien.lien,
            'id_user': bien.id_user.id if bien.id_user else None,
            'date_publication': bien.date_publication,
        })
    
    # Convertir la liste en format JSON
    return JsonResponse({'list_biens': _list_biens}, safe=False, status=200)

@api_view(['POST'])
@csrf_exempt
def fetch_biens_immobiliers(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            idbien = data.get('idbien')
            biens_immobiliers = Biens_immobiliers.objects.filter(BienID=idbien)

            _list_biens = []
            for bien in biens_immobiliers:
                utilisateur = bien.id_user
                # profile = Profile.objects.get(ProfileID=utilisateur)
                user = User.objects.get(id=utilisateur.id)

                bien_data = {
                    'bienID': bien.BienID,
                    'type_de_bien': bien.type_de_bien,
                    'prix': bien.prix,
                    'surface': bien.surface,
                    'nombre_de_salles_de_bains': bien.nombre_de_salles_de_bains,
                    'nombre_de_salles_de_sals': bien.nombre_de_salles_de_sals,
                    'image':  None,
                    'description': bien.description,
                    'lien': bien.lien,
                    # 'type_compte': profile.type_compte,
                    # 'numero_tel': profile.numero_tel,
                    # 'facebook': profile.facebook,
                    'username': user.username,
                    'first_name': user.first_name,
                    'email': user.email,
                    'coordonnees_geographique': bien.coordonnees_geographique,
                    'date_publication': bien.date_publication,
                }
                _list_biens.append(bien_data)

            print(_list_biens)
            return JsonResponse({'list_biens': _list_biens}, safe=False, status=200)
        except json.decoder.JSONDecodeError as e:
            return JsonResponse({'error': 'Erreur lors du décodage des données JSON.'}, status=400)
    else:
        return Response(status=404)