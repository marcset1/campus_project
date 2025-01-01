from functools import wraps
from django.http import HttpResponseRedirect
from .models import Client

def client_login_required(view_func):
	@wraps(view_func)
	def wrapper(request, *args, **kwargs):
		#if not request.session.get('client_id'):
		#""" pas de session pour ce client : se connecter pour avoir une session """	
		#print(f"pas de session pour le client {request.session.get('client_id')}")
		#return HttpResponseRedirect('/login/')
		#client = Client.objects.get(id=request.session['client_id'])
		#if not client:
		#""" pas de client pour cette session : se connecter avec autre client """
		#print("pas de client pour la session")
		#return HttpResponseRedirect('/login/')
		#return view_func(request, *args, **kwargs)
		#""" on retourne le decorateur apres son traitement. """
		#return wrapper
		if 'client_id' in request.session:
			print("client connected")
		else:
			print("client disconnected")
