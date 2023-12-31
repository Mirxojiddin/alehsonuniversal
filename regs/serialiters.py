from rest_framework import serializers
from regs.models import RegStepOne, RegStepTwo, PaginationType, Province, District, Pagination
from rest_framework.exceptions import ValidationError


class RegStepOneSerializer(serializers.ModelSerializer):
	province_id = serializers.IntegerField()
	district_id = serializers.IntegerField()

	passport = serializers.CharField(max_length=10, required=True, error_messages={
		'max_length': "Passport ma'lumotlari xato kiritilgan",
		'required': "Pasport ma'lumotlari kiritilmagan"
	})
	full_name = serializers.CharField(max_length=200, error_messages={
			'required': "Ism va familya kiritlmagan"
	})

	birthday = serializers.DateField(required=True, input_formats=['%m/%d/%Y'], error_messages={
		'invalid': "Tu'ilgan kun noto'g'ri formatda kiritilgan",
		'required': "Tug'ilgan kiritilmagan"
	})

	class Meta:
		model = RegStepOne
		fields = ('full_name', 'passport', 'birthday', 'district_id','province_id')

	def validate_passport(self, value):
		if not value:
			raise ValidationError("pasport ma'lumotlari kiritilmagan")
		check_value = value.replace(' ', '')
		if len(check_value) != 9:
			raise ValidationError("pasport ma'lumotlari xato kiritilgan")
		for char in check_value[0:2]:
			if not char.isalpha():
				raise ValidationError("pasport ma'lumotlari xato kiritilgan")
		for char in check_value[2:]:
			if not char.isdigit():
				raise ValidationError("pasport ma'lumotlari xato kiritilgan")
		return check_value

	def validate_full_name(self, value):
		for char in value:
			if char.isdigit():
				raise ValidationError("Ism familya noto'g'ri kiritilgan")
		return value

	def validate_full_name(self, value):
		for char in value:
			if char.isdigit():
				raise ValidationError("Ism familya noto'g'ri kiritilgan")
		return value


class PaginationTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = PaginationType
		fields = ('name', )


class DistrictSerializer(serializers.ModelSerializer):
	class Meta:
		model = District
		fields = ('id', 'name',)


class ProvinceSerializer(serializers.ModelSerializer):
	district = DistrictSerializer(many=True, read_only=True)

	class Meta:
		model = Province
		fields = ('id', 'name', 'district')


class RegStepTwoSerializer(serializers.ModelSerializer):

	card_number = serializers.CharField(max_length=20, required=True, error_messages={
		'max_length': "Karta raqam noto'g'ri kirtilgan",
		'required': "karta raqam kiritilmagan"
	})
	information = serializers.CharField(max_length=1000, required=True, error_messages={
			'required': "O'ziz haqizda ma'lumot kiritilmagan"
	})
	pagination_type = PaginationTypeSerializer(read_only=True)

	class Meta:
		model = RegStepTwo
		fields = ('card_number', 'information', 'pagination_type')

	def validate_card_number(self, value):
		check_value = value.replace(' ', '')
		if len(check_value) != 16 or not check_value.isdigit():
			raise ValidationError("Karta raqam xato kiritilgan")

		return value


class PaginationSerializer(serializers.ModelSerializer):
	province_id = serializers.IntegerField()
	district_id = serializers.IntegerField()
	card_number = serializers.CharField(max_length=20, required=True, error_messages={
		'max_length': "Karta raqam noto'g'ri kirtilgan",
		'required': "karta raqam kiritilmagan"
	})
	information = serializers.CharField(max_length=1000, required=True, error_messages={
		'required': "O'ziz haqizda ma'lumot kiritilmagan"
	})
	pagination_type = PaginationTypeSerializer(read_only=True)
	passport = serializers.CharField(max_length=10, required=True, error_messages={
		'max_length': "Passport ma'lumotlari xato kiritilgan",
		'required': "Pasport ma'lumotlari kiritilmagan"
	})
	full_name = serializers.CharField(max_length=200, error_messages={
			'required': "Ism va familya kiritlmagan"
	})

	birthday = serializers.DateField(required=True, input_formats=['%m/%d/%Y'], error_messages={
		'invalid': "Tu'ilgan kun noto'g'ri formatda kiritilgan",
		'required': "Tug'ilgan kiritilmagan"
	})

	phone_number = serializers.CharField(max_length=7, error_messages={
		'max_length': "telefon raqam xato kititilgan",
		'required': "Pasport ma'lumotlari kiritilmagan"
	})

	class Meta:
		model = Pagination
		fields = (
			'full_name', 'passport', 'birthday', 'district_id', 'province_id', 'phone_number', 'card_number',
			'information', 'pagination_type'
		)

	def validate_passport(self, value):
		if not value:
			raise ValidationError("pasport ma'lumotlari kiritilmagan")
		check_value = value.replace(' ', '')
		if len(check_value) != 9:
			raise ValidationError("pasport ma'lumotlari xato kiritilgan")
		for char in check_value[0:2]:
			if not char.isalpha():
				raise ValidationError("pasport ma'lumotlari xato kiritilgan")
		for char in check_value[2:]:
			if not char.isdigit():
				raise ValidationError("pasport ma'lumotlari xato kiritilgan")
		return check_value

	def validate_full_name(self, value):
		for char in value:
			if char.isdigit():
				raise ValidationError("Ism familya noto'g'ri kiritilgan")
		return value

	def validate_full_name(self, value):
		for char in value:
			if char.isdigit():
				raise ValidationError("Ism familya noto'g'ri kiritilgan")
		return value

	def validate_card_number(self, value):
		check_value = value.replace(' ', '')
		if len(check_value) != 16 or not check_value.isdigit():
			raise ValidationError("Karta raqam xato kiritilgan")

		return value

	def validate_phone_number(self, value):
		check_value = value.replace(' ', '')
		if len(check_value) != 13 or not check_value.isdigit():
			raise ValidationError("Telefon raqam xato kiritilgan")

		return value


class PaginationType2Serializer(serializers.ModelSerializer):
	pagination = PaginationSerializer(many=True, read_only= True)

	class Meta:
		model = PaginationType
		fields = ('name', 'pagination')