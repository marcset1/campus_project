from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout
from .models import Client
from django.contrib.auth.decorators import login_required
from .decorators import client_login_required
import json
from django.contrib.auth.hashers import make_password, check_password

@csrf_exempt
def signup(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		pseudo = data.get('pseudo')
		password = data.get('password')
		email = data.get('email')
		telephone = data.get('telephone')
		print(f"enregistrer: {pseudo}, {password}, {email}")
		if pseudo and password and email:
			hashed_password = make_password(password)
			print(f"hashed password {hashed_password}")
			client = Client.objects.create(pseudo=pseudo, password=hashed_password, email=email, telephone=telephone)
			client.save()
			login(request, client)
			return JsonResponse({'message': 'User created and logged in successfully'}, status=201)
		return JsonResponse({'error': 'Invalid data'}, status=400)
	return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def login_view(request):
	""" 23/12/2024 - je decides de laisser la gestion des token JWT au front-end : sinon y reflechir plus tard. """
	if request.method == 'POST':
		data = json.loads(request.body)
		pseudo = data.get('pseudo')
		password = data.get('password')
		try:
			client = Client.objects.get(pseudo=pseudo)
			if check_password(password, client.password):
				print(f"apres le login: {login(request, client)}")
				
				#request.session['client_id'] = client.id
				#print(f"la session du client est: {request.session['client_id']}")
				#client.session_id = request.session.session_key
				#client.save()
				
				print(f"{client.pseudo} logged in sucessfully with session id: {request.session['client_id']}")
				# return status and use in another view to perform action
				return JsonResponse({'message': 'Logged in successfully'}, status=200)
			else:
				return JsonResponse({'error': 'Invalid credentials'}, status=400)
		except Client.DoesNotExist:
			return JsonResponse({'error': 'Invalid credentials'}, status=400)
	return JsonResponse({'error': 'Invalid method'}, status=405)


