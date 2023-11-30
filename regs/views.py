from rest_framework import status
from rest_framework.exceptions import ValidationError
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
		passport = request.data.get('passport').replace(' ', '')
		province = request.data.get('province_id')
		district = request.data.get('district_id')

		serializer = RegStepOneSerializer(data=request.data)
		if serializer.is_valid():
			if not Province.objects.filter(pk=province).exists():
				raise ValidationError("Viloyat xato tanlangan")
			if not District.objects.filter(province=province, pk=district).exists():
				raise ValidationError("Tuman Viloyatga mos kelmadi")
			if RegStepOne.objects.filter(passport=passport).exists():
				raise ValidationError("Bu pasport ro'yxatdan o'tgan")
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
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
			serializer.save()
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


class DistrictDetailApiView(APIView):
	def get(self, request, id):
		try:
			regs = District.objects.get(id=id)
			serializer = DistrictSerializer(regs)
			return Response(serializer.data, status=status.HTTP_200_OK)
		except District.DoesNotExist:
			raise ValidationError("bunday tuman yo'q")


class ProvinceApiView(APIView):
	def get(self, request):
		regs = Province.objects.all()
		serializer = ProvinceSerializer(regs, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class ProvinceDetailApiView(APIView):

	def get(self, request, id):

		try:
			regs = Province.objects.get(id=id)
			serializer = ProvinceSerializer(regs)
			return Response(serializer.data, status=status.HTTP_200_OK)
		except Province.DoesNotExist:
			raise ValidationError("bunday viloyat yo'q")
