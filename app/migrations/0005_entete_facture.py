# Generated by Django 4.1.4 on 2022-12-30 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_produit_bondecmd_produit_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_ent', models.IntegerField()),
                ('date_ent', models.DateField()),
                ('fournisseur_ent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.fournisseur')),
            ],
        ),
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField()),
                ('prix_HT', models.DecimalField(decimal_places=2, max_digits=10)),
                ('prix_vd', models.DecimalField(decimal_places=2, max_digits=10)),
                ('entete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.entete')),
            ],
        ),
    ]
