from rest_framework import serializers
from regs.models import RegStepOne
from rest_framework.exceptions import ValidationError
from datetime import date


class RegStepOneSerializer(serializers.Serializer):
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
		fields = ('full_name', 'passport', 'birthday')

	def validate_passport(self, value):
		if not value:
			raise ValidationError("pasport ma'lumotlari kiritilmagan")
		check_value = value.replace(' ', '')
		if len(check_value) != 9:
			raise ValidationError("pasport ma'lumotlari xato kiritilgan")
		if len(check_value) != 9:
			raise ValidationError("pasport ma'lumotlari xato kiritilgan")
		for char in check_value[0:2]:
			if not char.isalpha():
				raise ValidationError("pasport ma'lumotlari xato kiritilgan")
		for char in check_value[2:]:
			if not char.isdigit():
				raise ValidationError("pasport ma'lumotlari xato kiritilgan")
		return value


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
