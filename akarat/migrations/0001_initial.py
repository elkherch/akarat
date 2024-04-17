# Generated by Django 3.2.12 on 2024-04-17 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Biens_immobiliers',
            fields=[
                ('BienID', models.AutoField(primary_key=True, serialize=False)),
                ('type_de_bien', models.CharField(max_length=20)),
                ('prix', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('surface', models.IntegerField(default=0)),
                ('nombre_de_salles_de_bains', models.IntegerField()),
                ('nombre_de_salles_de_sals', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('date_publication', models.DateTimeField()),
                ('lien', models.CharField(max_length=100)),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('VilleID', models.AutoField(primary_key=True, serialize=False)),
                ('Nom_ville', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('ProfileID', models.AutoField(primary_key=True, serialize=False)),
                ('type_compte', models.CharField(max_length=20)),
                ('numero_tel', models.CharField(max_length=8)),
                ('facebook', models.CharField(max_length=20)),
                ('logo_profile', models.ImageField(blank=True, null=True, upload_to='profile_logos/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('NotificationID', models.AutoField(primary_key=True, serialize=False)),
                ('Contenu', models.TextField()),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('ProfileID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='akarat.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('imageID', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='property_images/')),
                ('bien_immobilier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='akarat.biens_immobiliers')),
            ],
        ),
        migrations.CreateModel(
            name='Favoris',
            fields=[
                ('FavoriID', models.AutoField(primary_key=True, serialize=False)),
                ('BienID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='akarat.biens_immobiliers')),
                ('ProfileID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='akarat.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Commentaires_et_évaluations',
            fields=[
                ('CommentaireID', models.AutoField(primary_key=True, serialize=False)),
                ('Commentaire', models.TextField()),
                ('evaluation', models.IntegerField()),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('BienID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='akarat.biens_immobiliers')),
                ('ProfileID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='akarat.profile')),
            ],
        ),
    ]