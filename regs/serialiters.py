from rest_framework import serializers
from regs.models import RegStepOne
from rest_framework.exceptions import ValidationError
from datetime import date


class RegStepOneSerializer(serializers.Serializer):
	class Meta:
		model = RegStepOne
		fields = ('full_name', "passport, 'birthday'")

	def validate(self, data):
		full_name = data.get('full_name')
		passport = data.get('passport')
		birthday = data.get('birthday')

		if len(passport.replase(' ', '')) != 7:
			raise ValidationError("pasport ma'lumotlari xato kiritilgan")
