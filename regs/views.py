from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from regs.models import RegStepOne
from regs.serialiters import RegStepOneSerializer


class RegStepOneApiView(APIView):
	def get(self, request):
		regs = RegStepOne.objects.all()
		serializer = RegStepOneSerializer(regs, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request):
		full_name = request.data.get('full_name')
		passport = request.data.get('passport')
		birthday = request.data.get('birthday')

		serializer = RegStepOneSerializer(data=request.data)
		if serializer.is_valid():
			return Response({"status":"ishladi"}, status=status.HTTP_200_OK)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

