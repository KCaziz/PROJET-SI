# Generated by Django 4.1.4 on 2022-12-29 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_c', models.CharField(max_length=100)),
                ('prenom_c', models.CharField(max_length=100)),
                ('adresse_c', models.TextField()),
                ('telephone_c', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='EntreeStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_e', models.CharField(max_length=20)),
                ('date_e', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_f', models.CharField(max_length=100)),
                ('prenom_f', models.CharField(max_length=100)),
                ('adresse_f', models.TextField()),
                ('telephone_f', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_p', models.CharField(max_length=100)),
                ('prix_HT', models.DecimalField(decimal_places=2, max_digits=10)),
                ('prix_vd', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantite', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeProduit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_t', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_v', models.CharField(max_length=20)),
                ('date_v', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.client')),
            ],
        ),
        migrations.CreateModel(
            name='ProduitVente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField()),
                ('prix_unite_ht', models.DecimalField(decimal_places=2, max_digits=10)),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.produit')),
                ('vente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.vente')),
            ],
        ),
        migrations.CreateModel(
            name='ProduitEntreeStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField()),
                ('prix_unite_ht', models.DecimalField(decimal_places=2, max_digits=10)),
                ('entree_stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.entreestock')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.produit')),
            ],
        ),
        migrations.AddField(
            model_name='produit',
            name='type_produit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.typeproduit'),
        ),
        migrations.AddField(
            model_name='entreestock',
            name='fournisseur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.fournisseur'),
        ),
        migrations.CreateModel(
            name='BonDeCmd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField()),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.produit')),
            ],
        ),
    ]