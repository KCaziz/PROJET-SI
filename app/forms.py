from django.db.models import fields
from django import forms
from .models import Produit, TypeProduit, BonDeCmd, Produit_BonDeCmd, Fournisseur, Entete, Facture
from django.forms import formset_factory

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields="__all__"
class TypeForm(forms.ModelForm):
    class Meta:
        model = TypeProduit
        fields="__all__"
class BonForm(forms.ModelForm):
    class Meta:
        model = BonDeCmd
        fields=['fournisseur']
class LigneBonDeCommandeForm(forms.ModelForm):
    class Meta:
        model = Produit_BonDeCmd
        fields = ['produit', 'quantite']
# LigneBonDeCommandeFormSet = formset_factory(LigneBonDeCommandeForm, extra=1)
# class LigneBonDeCommandeForm(forms.ModelForm):
#     class Meta:
#         model = Produit_BonDeCmd
#         fields = ['quantite', 'produit']
#     # Utiliser un ModelMultipleChoiceField pour sélectionner plusieurs produits
#     produit = forms.ModelMultipleChoiceField(
#         queryset=Produit.objects.all(),
#         required=True
#     )
LigneBonDeCommandeFormSet = forms.inlineformset_factory(BonDeCmd, Produit_BonDeCmd, fields=('produit', 'quantite'), extra=1)

class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields="__all__"
class EnteteForm(forms.ModelForm):
    class Meta:
        model = Entete
        fields="__all__"
class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields="__all__"