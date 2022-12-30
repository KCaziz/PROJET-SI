from django.shortcuts import render, redirect
from .models import Produit, TypeProduit, BonDeCmd, Fournisseur, Produit_BonDeCmd, Entete, Facture
from .forms import ProduitForm, TypeForm, BonForm, LigneBonDeCommandeFormSet, LigneBonDeCommandeForm, FournisseurForm, EnteteForm, FactureForm
from django.http import JsonResponse


# Create your views here.
def acceuil(request):
    return render(request, "acceuil.html")

def produits(request):
    product = Produit.objects.all()
    return render(request, 'produit.html', {"produit" : product})
def voir(request, pk):
    try:
        product = Produit.objects.get(id=pk)
        return render(request, 'voir.html', {"produit" : product})
    except Produit.DoesNotExist:
        redirect('/acceuil')
def ajoutprd(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProduitForm()
            msg = "Produit ajouter, vous pouvez ajouter un autre"
        else : 
            msg = "Remplissez tous les champs"
        return render(request, "AjoutProduit.html", {"form": form, "message": msg})
    else :
            form = ProduitForm()
            msg = "Remplissez tous les champs"
            return render(request, "AjoutProduit.html", {"form":form, "message":msg})
def supprime_prd(request, pk):
    produit = Produit.objects.get(id=pk)
    produit.delete()
    return redirect('produit')
def modifier_produit(request, pk):
    produit = Produit.objects.get(id=pk)
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('produit')
    else:
        form = ProduitForm(initial={
            'nom':produit.nom_p,
            'prix achete':produit.prix_HT,
            'prix vendu':produit.prix_vd,
            'type_produit':produit.type_produit,
            'quantite':produit.quantite
        })
    return render(request, 'modifier_produit.html', {'form': form})
def rechercher_produits (request):
    produits =""
    if (request.method =="GET"):
        query=request.GET.get('recherche')
        if query:
             produits=Produit.objects.filter(nom_p__contains = query)
        return render(request, "search_p.html",{"products": produits})
#######################################################################
def type(request):
    tp = TypeProduit.objects.all()
    return render(request, 'TypeProduit.html', {"TypeProduit":tp}) 
def AjoutType(request):
    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
            form = TypeForm()
            msg = "Type ajouter, vous pouvez ajouter un autre"
        else : 
            msg = "Remplissez tous les champs"
        return render(request, "AjoutType.html", {"form": form, "message": msg})
    else :
        form = TypeForm()
        msg = "Remplissez tous les champs"
        return render(request, "AjoutType.html", {"form":form, "message":msg})
def supprime_type(request, pk):
    type = TypeProduit.objects.get(id=pk)
    type.delete()
    return redirect('TypeProduit')
def modifier_type(request, pk):
    type = TypeProduit.objects.get(id=pk)
    if request.method == 'POST':
        form = TypeForm(request.POST, instance=type)
        if form.is_valid():
            form.save()
            return redirect('TypeProduit')
    else:
        form = TypeForm(initial={
            'nom_t':type.nom_t
        })
    return render(request, 'modifier_type.html', {'form': form})
def rechercher_type (request):
    type =""
    if (request.method =="GET"):
        query=request.GET.get('recherche')
        if query:
            type=TypeProduit.objects.filter(nom_t__contains = query)
        return render(request, "search_t.html",{"types": type})
################################################################""""
def fournisseurs(request):
    fournisseurs = Fournisseur.objects.all()
    return render(request, 'fournisseurs.html', {"fournisseurs": fournisseurs})

 
def Ajout_fournisseur(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            form = FournisseurForm()
            msg = "fournisseur ajouter, vous pouvez ajouter un autre"
        else : 
            msg = "Remplissez tous les champs"
        return render(request, "Ajout_fournisseur.html", {"form": form, "message": msg})
    else :
        form = FournisseurForm()
        msg = "Remplissez tous les champs"
        return render(request, "Ajout_fournisseur.html", {"form":form, "message":msg})
def supprime_fournisseur(request, pk):
    fournisseur = Fournisseur.objects.get(id=pk)
    fournisseur.delete()
    return redirect('fournisseurs')
def modifier_fournisseur(request, pk):
    fournisseur = Fournisseur.objects.get(id=pk)
    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance=fournisseur)
        if form.is_valid():
            form.save()
            return redirect('fournisseurs')
    else:
        form = FournisseurForm(initial={
            'nom_f':fournisseur.nom_f,
            'prenom_f':fournisseur.prenom_f,
            'adresse_f':fournisseur.adresse_f,
            'telephone_f':fournisseur.telephone_f,
            'solde':fournisseur.solde
        })
    return render(request, 'modifier_fournisseur.html', {'form': form})
def rechercher_fournisseur (request):
    fournisseur =""
    if (request.method =="GET"):
        query=request.GET.get('recherche')
        if query:
            fournisseur=Fournisseur.objects.filter(nom_f__contains = query)
        return render(request, "search_f.html",{"fournisseurs": fournisseur})
















def Entree(request):
    return render(request, "Entree.html")
def affiche_BonDeCmd(request):
    bon = BonDeCmd.objects.all()
    return render(request, "BonDeCmd.html", {"bon":bon})
def ajouter_bon_de_commande(request):
    if request.method == 'POST':
        form = BonForm(request.POST)
        formset = LigneBonDeCommandeFormSet(request.POST, prefix='lignes')
        if form.is_valid() and formset.is_valid():
            bon_de_commande = form.save()
            lignes = formset.save(commit=False)
            for ligne in lignes:
                ligne.bon_de_commande = bon_de_commande
                ligne.save()
            return redirect('BonDeCmd')
    else:
        form = BonForm()
        formset = LigneBonDeCommandeFormSet(prefix='lignes')
    return render(request, 'Ajout_BonDeCmd.html', {
        'form': form,
        'formset': formset,
    })





def Ajouter_Bon_De_Commande(request):
    if request.method == 'POST':
        form = BonForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('BonDeCmd')
    else:
        form = BonForm()
        return render(request, 'Ajout_BonDeCmd.html', {'form':form})
def Ajouter_Produit_Bon_De_Commande(request, bon):
    if request.method == 'POST':
        form = LigneBonDeCommandeForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('BonDeCmd')
    else:
        form = LigneBonDeCommandeForm(initial={
            'bon': bon
        })
        return render(request, 'Ajout_Produit_BonDeCmd.html', {'form':form})

def new_form_field(request):
  if request.is_ajax():
        form = LigneBonDeCommandeForm()
        return render(request, 'new_form_field.html', {'form': form})
  else:
    return render(request, "acceuil.html")
# def ajouter_bon_de_commande(request):
#     if request.method == 'POST':
#         form = BonForm(request.POST)
#         formset = LigneBonDeCommandeFormSet(request.POST, prefix='lignes')
#         if form.is_valid() and formset.is_valid():
#             bon_de_commande = form.save()
#             formset.instance = bon_de_commande
#             formset.save()
#             return redirect('BonDeCmd')
#     else:
#         form = BonForm()
#         # Initialiser le formset avec la liste des produits disponibles
#         formset = LigneBonDeCommandeFormSet(prefix='lignes', queryset=Produit.objects.all())
#     return render(request, 'Ajout_BonDeCmd.html', {'form': form, 'formset': formset})





def details_bon(request,pk):
    produit_bon = Produit_BonDeCmd.objects.filter(bon__id=pk)
    return render(request, "details_bon.html", {"produit_bon": produit_bon })
def supprime_bon(request, pk):
    bon = BonDeCmd.objects.get(id=pk)
    bon.delete()
    return redirect('BonDeCmd')




def search(request):
  if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
    query = request.GET.get('q', '')
    results = Produit.objects.filter(nom_p__icontains=query)
    data = []
    for result in results:
      data.append({ 'qte': result.quantite, 'nom_p': result.nom_p })
    return JsonResponse({ 'data': data })
  else:
    return render(request, 'search.html')


def BL(request):
    bl = Entete.objects.all()
    return render(request, "BL.html", {"BLs":bl})
def entete(request):
    if request.method == 'POST':
        form = EnteteForm(request.POST)
        if form.is_valid():
            entete = form.save()
            return redirect('Ajout_Facture', pk=entete.id)
    else:
        form = EnteteForm()
        return render(request, "Entete.html", {"form":form})
def facture(request, pk):
    entete = Entete.objects.get(id=pk)
    if request.method == 'POST':
        form = FactureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Ajout_Facture', pk=entete.id)
    else:
        form = FactureForm(initial={
            'entete':entete,
            })
        return render(request, "Ajoute_Facture.html", {"form":form}) 
def supprime_facture(request, pk):
    bon = Entete.objects.get(id=pk)
    bon.delete()
    return redirect('BL')
def modifier_facture(request, pk):
    entete = Entete.objects.get(id=pk)
    if request.method == 'POST':
        form = EnteteForm(request.POST, instance=entete)
        if form.is_valid():
            form.save()
            return redirect('BL')
    else:
        form = EnteteForm(initial={
            'numero_ent' : entete.numero_ent,
            'date_ent'  : entete.date_ent,
            'fournisseur_ent': entete.fournisseur_ent,
        })
    return render(request, 'modifier_type.html', {'form': form})
def rechercher_facture (request):
    entete =""
    if (request.method =="GET"):
        query=request.GET.get('recherche')
        if query:
            entete=Entete.objects.filter(numero_ent__contains = query)
        return render(request, "search_BL.html",{"entetes": entete})
def details_BL(request,pk):
    total_HT = 0
    total_TTC = 0
    BL = Facture.objects.filter(entete__id=pk)
    entete = Entete.objects.get(id=pk)
    for ligne in BL:
        total_HT = total_HT +ligne.prix_HT * ligne.quantite
        total_TTC = total_TTC +ligne.prix_vd * ligne.quantite
    return render(request, "details_BL.html", {"BL": BL , "entete":entete, "total_HT":total_HT, "total_TTC":total_TTC})