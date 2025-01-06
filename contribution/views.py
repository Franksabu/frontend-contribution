from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from membre.models import Membre
from cotisation.models import Contribution, Cotisation, TypeCotisation

from assistance.models import Assistance
from django.db.models import Sum, Count
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                messages.success(request, "Inscription réussie !")
                user.save()
                login(request, user)
                return redirect('login')
            
            except IntegrityError:
                messages.error(request, "Le nom d'utilisateur existe déjà !")
        else:
            messages.error(request, "password n'est pas correct !")

    return render(request, "registration/register.html")


def login_view(request):  
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = "Identifiants invalides."
            return render(request, 'registration/login.html', {'error': error})

    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')
# Utilisez @login_required pour les vues qui nécessitent une authentification
# @login_required(login_url="login")  # Changez login_url à "login" au lieu de "home"


@login_required
def home(request):
    user_all = User.objects.all()
    membre_all = Membre.objects.all()
    assistance_all = Assistance.objects.all()
    cotisation_all = Cotisation.objects.all()
    type_cotisation_all = TypeCotisation.objects.all()
    contribution_all = Contribution.objects.all()
    somme_users = User.objects.aggregate(total_users=Count("id"))
    somme_membres = Membre.objects.aggregate(total_membres=Count("id"))
    somme_assistances = Assistance.objects.aggregate(total_montant_assistances=Sum("montant_assistance"), total_assistances=Count("id"))
    somme_contributions = Contribution.objects.aggregate(total_montant_contributions=Sum("montant"), total_contributions=Count("id"))
     
    total_assistance = Assistance.objects.count()
    total_contribution = Contribution.objects.count()
    total_cotisation = Cotisation.objects.count()
    total_membre = Membre.objects.count()
    total_user = User.objects.count()    

    montant_min_cotisation = cotisation_all.first().montant_min if cotisation_all.exists() else 0

    # Créer une liste de contributions avec leur validité
    contributions_with_validity = []
    for contribution in contribution_all:
        is_valid = montant_min_cotisation <= contribution.montant
        contributions_with_validity.append({
            'contribution': contribution,
            'is_valid': is_valid,
        })

    contributions = Contribution.objects.select_related('cotisation').all()  # Charger les contributions avec leurs cotisations
    assistances = Assistance.objects.select_related('cotisation').all()  # Charger les assistances avec leurs cotisations
    assistance_data = []
    contributions_data = []
    for contribution in contributions:
        montant_min = contribution.cotisation.montant_min  # Montant minimum de la cotisation associée
        is_valid = contribution.montant >= montant_min  # Comparaison
        contributions_data.append({
            'membre': contribution.membre,  # Remplacez par le bon attribut de membre
            'date_contrib': contribution.date_contrib,
            'montant_min': montant_min,
            'montant': contribution.montant,
            'is_valid': is_valid,
        })
   
    for assistance in assistances:
        montant_min = assistance.cotisation.montant_min  # Montant minimum de la cotisation
        is_valid_ass = assistance.montant_assistance >= montant_min  # Comparaison
        assistance_data.append({
            'membre_assistant': assistance.membre_assistant,  # Remplacez par le bon attribut de
            'date_assistance': assistance.date_assistance,
            'montant_min': montant_min,
            'montant_assistance': assistance.montant_assistance,
            'is_valid_ass': is_valid_ass,
        })
    
    context = {
        # 'user_data': user_data,
        'user_all': user_all,
        "membre_all": membre_all,
        "contribution_all": contribution_all,
        "assistance_all": assistance_all,
        "type_cotisation_all": type_cotisation_all,
        "somme_users": somme_users,
        "somme_membres": somme_membres,
        "somme_assistances": somme_assistances,
        "somme_contributions": somme_contributions,
        # exemple
        "total_assistance": total_assistance,
        "total_contribution": total_contribution,
        "total_cotisation": total_cotisation,
        "total_membre": total_membre,
        "total_user": total_user,
        # 'is_valid': is_valid
        "contributions_with_validity": contributions_with_validity,
        'contributions_data': contributions_data,
        'assistance_data': assistance_data
     
    }
    return render(request, "home.html", context)


