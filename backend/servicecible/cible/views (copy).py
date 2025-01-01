# myproject/views.py

#INSCRIPTION
from .models import Client, Bailleur
from django.contrib.auth.hashers import make_password
#
# myproject/views.py

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@csrf_exempt
@require_POST
def login_view(request):
    pseudo = request.POST.get('pseudo')
    password = request.POST.get('password')
    is_bailleur = request.POST.get('is_bailleur', False)

    if is_bailleur:
        user = authenticate(request, username=pseudo, password=password)
        if user and isinstance(user, Bailleur):
            login(request, user)
            return JsonResponse({'message': 'Login successful as bailleur'})
        else:
            return JsonResponse({'message': 'Invalid credentials for bailleur'}, status=400)
    else:
        user = authenticate(request, username=pseudo, password=password)
        if user and isinstance(user, Client):
            login(request, user)
            return JsonResponse({'message': 'Login successful as client'})
        else:
            return JsonResponse({'message': 'Invalid credentials for client'}, status=400)

@csrf_exempt
@require_POST
def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Logout successful'})


#INSCRIPTION
@csrf_exempt  # Désactive la vérification CSRF pour cette vue
def register_view(request):
	if request.method == 'POST':  # Vérifie si la méthode de la requête est POST
		pseudo = request.POST.get('pseudo')
		password = request.POST.get('password')
		adresse = request.POST.get('adresse')
		email = request.POST.get('email')
		print(email)
		numero_telephone = request.POST.get('numero_telephone')
		preferences_alimentaires = request.POST.get('preferences_alimentaires')
		preferences_sonore = request.POST.get('preferences_sonore')
		is_bailleur = request.POST.get('is_bailleur', False)
		is_client = request.POST.get('is_client', False)
		# Vérifie qu'au moins un email ou un numéro de téléphone est fourni
		if not email and not numero_telephone:
			return JsonResponse({'message': 'Le client doit avoir au moins un numéro de téléphone ou un email.'}, status=400)

		# Crée un nouveau client ou bailleur avec les informations fournies
		if is_bailleur:
			#ENREGISTREMENT SUR BAILLEUR
			client1 = Bailleur(pseudo_bailleur=pseudo_bailleur, pseudo=pseudo, password=make_password(password), adresse=adresse, email=email, numero_telephone=numero_telephone, preferences_alimentaires=preferences_alimentaires, preferences_sonore=preferences_sonore)
			#ENREGISTREMENT SUR CLIENT AUSSI 
			# Hache le mot de passe avant de le stocker
			client2 = Client(pseudo=pseudo, password=make_password(password), adresse=adresse, email=email, numero_telephone=numero_telephone, preferences_alimentaires=preferences_alimentaires, preferences_sonore=preferences_sonore)
			client1.save()
			client2.save()  # Sauvegarde le client ou bailleur dans la base de données
			return JsonResponse({'message': 'Client créé avec succès'})
		elif is_client and is_bailleur: # tu es deja client et tu veux devenir bailleur
			client = Bailleur(pseudo_bailleur=pseudo_bailleur, pseudo=pseudo, password=make_password(password), adresse=adresse, email=email, numero_telephone=numero_telephone, preferences_alimentaires=preferences_alimentaires, preferences_sonore=preferences_sonore)
			client.save()
		else:
			client = Client(pseudo=pseudo, password=make_password(password), adresse=adresse, email=email, numero_telephone=numero_telephone, preferences_alimentaires=preferences_alimentaires, preferences_sonore=preferences_sonore)
			client.save()
	return JsonResponse({'message': 'Only POST method is allowed'}, status=405)  # Retourne une erreur si la méthode n'est pas POST

