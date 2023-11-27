from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from regs.models import RegStepOne, RegStepTwo, PaginationType, Province, District
from regs.serialiters import RegStepOneSerializer, PaginationTypeSerializer, RegStepTwoSerializer
from regs.serialiters import DistrictSerializer, ProvinceSerializer


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


class RegStepTwoApiView(APIView):
	def get(self, request):
		regs = RegStepTwo.objects.all()
		serializer = RegStepTwoSerializer(regs, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request):
		serializer = RegStepTwoSerializer(data=request.data)
		if serializer.is_valid():
			return Response({"status":"ishladi"}, status=status.HTTP_200_OK)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaginationTypeApiView(APIView):
	def get(self, request):
		regs = PaginationType.objects.all()
		serializer = PaginationTypeSerializer(regs, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class DistrictApiView(APIView):
	def get(self, request):
		regs = District.objects.all()
		serializer = DistrictSerializer(regs, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class ProvinceApiView(APIView):
	def get(self, request):
		regs = Province.objects.all()
		serializer = ProvinceSerializer(regs, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
