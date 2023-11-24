from rest_framework import serializers
from regs.models import RegStepOne
from rest_framework.exceptions import ValidationError
from datetime import date


class RegStepOneSerializer(serializers.Serializer):
	passport = serializers.CharField(max_length=10)

	class Meta:
		model = RegStepOne
		fields = ('full_name', 'passport', 'birthday')

	def validate_passport(self, value):
		if len(value.replace(' ','')) != 9:
			raise ValidationError("pasport ma'lumotlari xato kiritilgan")
		return value