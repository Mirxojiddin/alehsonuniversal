from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from regs.models import RegStepOne, RegStepTwo, PaginationType, Province, District, Pagination
from regs.serialiters import RegStepOneSerializer, PaginationTypeSerializer, RegStepTwoSerializer
from regs.serialiters import DistrictSerializer, ProvinceSerializer, PaginationSerializer, PaginationType2Serializer


class RegStepOneApiView(APIView):
	queryset = RegStepOne.objects.all()
	serializer_class = RegStepOneSerializer

	def get(self, request, *args, **kwargs):
		regs = RegStepOne.objects.all()
		serializer = RegStepOneSerializer(regs, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request, *args, **kwargs):
		passport = request.data.get('passport').replace(' ', '')
		province = request.data.get('province_id')
		district = request.data.get('district_id')

		serializer = RegStepOneSerializer(data=request.data)
		if serializer.is_valid():
			if not Province.objects.filter(pk=province).exists():
				raise ValidationError("Viloyat xato tanlangan")
			if not District.objects.filter(province=province, pk=district).exists():
				raise ValidationError("Tuman Viloyatga mos kelmadi")
			if Pagination.objects.filter(passport=passport).exists():
				raise ValidationError("Bu pasport ro'yxatdan o'tgan")
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegStepTwoApiView(APIView):
	queryset = RegStepTwo.objects.all()
	serializer_class = RegStepTwoSerializer

	def get(self, request, *args, **kwargs):
		regs = RegStepTwo.objects.all()
		serializer = RegStepTwoSerializer(regs, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request, *args, **kwargs):
		serializer = RegStepTwoSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({"status": "ishladi"}, status=status.HTTP_200_OK)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaginationTypeApiView(APIView):
	queryset = PaginationType.objects.all()
	serializer_class = PaginationTypeSerializer
	def get(self, request, *args, **kwargs):
		regs = PaginationType.objects.all()
		serializer = PaginationTypeSerializer(regs, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class DistrictApiView(APIView):
	queryset = District.objects.all()
	serializer_class = DistrictSerializer

	def get(self, request, *args, **kwargs):
		regs = District.objects.all()
		serializer = DistrictSerializer(regs, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class DistrictDetailApiView(APIView):
	queryset = District.objects.all()
	serializer_class = DistrictSerializer

	def get(self, request, id, *args, **kwargs):
		try:
			regs = District.objects.get(id=id)
			serializer = DistrictSerializer(regs)
			return Response(serializer.data, status=status.HTTP_200_OK)
		except District.DoesNotExist:
			raise ValidationError("bunday tuman yo'q")


class ProvinceApiView(APIView):
	queryset = Province.objects.all()
	serializer_class = ProvinceSerializer

	def get(self, request, *args, **kwargs):
		regs = Province.objects.all()
		serializer = ProvinceSerializer(regs, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class ProvinceDetailApiView(APIView):
	queryset = Province.objects.all()
	serializer_class = ProvinceSerializer

	def get(self, request, id, *args, **kwargs):

		try:
			regs = Province.objects.get(id=id)
			serializer = ProvinceSerializer(regs)
			return Response(serializer.data, status=status.HTTP_200_OK)
		except Province.DoesNotExist:
			raise ValidationError("bunday viloyat yo'q")


class PaginationApiView(APIView):
	queryset = Pagination.objects.all()
	serializer_class = PaginationSerializer

	def get(self, request, *args, **kwargs):
		regs = Pagination.objects.all()
		serializer = PaginationSerializer(regs, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request, *args, **kwargs):
		passport = request.data.get('passport').replace(' ', '')
		province = request.data.get('province_id')
		district = request.data.get('district_id')

		serializer = PaginationSerializer(data=request.data)
		if serializer.is_valid():
			if not Province.objects.filter(pk=province).exists():
				raise ValidationError("Viloyat xato tanlangan")
			if not District.objects.filter(province=province, pk=district).exists():
				raise ValidationError("Tuman Viloyatga mos kelmadi")
			if Pagination.objects.filter(passport=passport).exists():
				raise ValidationError("Bu pasport ro'yxatdan o'tgan")
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaginationSearchApiView(APIView):
	queryset = PaginationType.objects.all()
	serializer_class = PaginationTypeSerializer
	def get(self, request, *args, **kwargs):
		regs = PaginationType.objects.all()
		serializer = ProvinceSerializer(regs, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class PaginationDetailSearchApiView(APIView):
	queryset = PaginationType.objects.all()
	serializer_class = PaginationTypeSerializer

	def get(self, request, pk, *args, **kwargs):
		regs = PaginationType.objects.get(pk=pk)
		serializer = ProvinceSerializer(regs)
		return Response(serializer.data, status=status.HTTP_200_OK)
