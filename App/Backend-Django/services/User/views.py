from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import JsonResponse


from User.models import *


@api_view(['GET'])
def getUsersView(request):
	res = getUsersModel()
	return JsonResponse({"resp":res})
	

@api_view(['POST'])
def createUserView(request):
	"""
		Function to create a User (signup).
			URL: http://127.0.0.1:8000/signup/
	"""
	email, password = request.data["email"], request.data["password"]
	flag = createUserModel(email, password)
	return JsonResponse({"response":flag})
		

@api_view(['POST'])
def existUserView(request):
	"""
		Function to login (signin).
			URL: http://127.0.0.1:8000/signin/
	"""
	email, password = request.data["email"], request.data["password"]
	flag = existUserModel(email, password)
	return JsonResponse({"response":flag})

@api_view(['GET'])		
def getUserView(request):
	"""
		Function to get a User (account).
			URL: http://127.0.0.1:8000/user?uid=621e0d8d100f0c51f3152f843a3b72069e0e7a86
	"""
	uid = request.GET.get("uid")
	resp = getUserModel(uid)
	return JsonResponse({"response":resp})

@api_view(['POST'])
def updateEmailUserView(request):
	"""
		Function to update email (User).
			URL: http://127.0.0.1:8000/update/email/
	"""
	uid, email = request.data["uid"], request.data["email"]
	# procedure to check email, password
	resp = updateEmailUserModel(uid, email)
	return JsonResponse({"response":resp})

@api_view(['POST'])	
def updatePasswordUserView(request):
	"""
		Function to update password (User).
			URL: http://127.0.0.1:8000/update/password/
	"""
	uid, password = request.data["uid"], request.data["password"]
	# procedure to check email, password
	resp = updatePasswordUserModel(uid, password)
	return JsonResponse({"response":resp})

@api_view(['DELETE'])	
def removeUserView(request):
	"""
		Function to remove a User.
			URL: http://127.0.0.1:8000/close?uid=621e0d8d100f0c51f3152f843a3b72069e0e7a86
	"""
	uid = request.GET.get("uid")
	flag = removeUserModel(uid)
	return JsonResponse({"response": flag})
