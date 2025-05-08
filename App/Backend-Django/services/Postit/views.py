from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import JsonResponse


from Postit.models import *


@api_view(['GET'])
def getPostitsAllView(request):
	"""
		Function to get all Postits (in database).
			URL: http://127.0.0.1:8000/postitss/
	"""
	resp = getPostitsAllModel()
	return JsonResponse({"resp":resp})
	

@api_view(['POST'])
def createPostitView(request):
	"""
		Function to create a Postit (for a User).
			URL: http://127.0.0.1:8000/new/
	"""
	uid, title, time, memo, img  = request.data["uid"], request.data["title"], request.data["time"], request.data["memo"], request.data["img"]
	flag = createPostitModel(uid, title, time, memo, img)
	return JsonResponse({"resp":flag})
	
@api_view(['GET'])
def getPostitView(request):
	"""
		Function to get a Postit (according to its iid).
			URL: http://127.0.0.1:8000/postit?uid=""&iid=""
	"""
	uid, iid = request.GET.get("uid"), request.GET.get("iid")
	res = getPostitModel(uid)
	return JsonResponse({"resp":res})

@api_view(['GET'])
def getPostitsView(request):
	"""
		Function to get (all) Postits (for a User).
			URL: http://127.0.0.1:8000/postits?uid=""
	"""
	uid = request.GET.get("uid")
	res = getPostitsModel(uid)
	return JsonResponse({"resp":res})

@api_view(['DELETE'])	
def removePostitView(request):
	"""
		Function to remove a Postit (according to its iid).
			URL: http://127.0.0.1:8000/close/postit?uid=""&iid=""
	"""
	uid, iid = request.GET.get("uid"), request.GET.get("iid")
	flag = removePostitModel(uid, iid)
	return JsonResponse({"resp":flag})

@api_view(['DELETE'])
def removePostitsView(request):
	"""
		Function to remove (all) Postits (for a User).
			URL: http://127.0.0.1:8000/close/postits?uid=""
	"""
	uid = request.GET.get("uid")
	flag = removePostitsModel(uid)
	return JsonResponse({"resp":flag})
