from django.db import models
from django.core.exceptions import ValidationError


def validate_max_length(value):
	if len(value) > 10:
		raise ValidationError("Passport ma'lumotlari xato kiritilgan")


class PaginationType(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class RegStepTwo(models.Model):
	card_number = models.CharField(verbose_name="Plastig raqam",max_length=20, null=False, blank=False)
	pagination_type = models.ForeignKey(PaginationType, on_delete=models.CASCADE, null=False, blank=False)
	information = models.TextField(null=False, blank=False)

	def __str__(self):
		return self.information


class Province(models.Model):
	name = models.CharField(max_length=50)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name


class District(models.Model):
	name = models.CharField(max_length=50)
	province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='district')

	class Meta:
		ordering = ['province', 'name']

	def __str__(self):
		return self.name


class RegStepTree(models.Model):
	phone_number = models.CharField(max_length=12)
	code = models.IntegerField()

	def __str__(self):
		return self.phone_number


class RegStepOne(models.Model):
	full_name = models.CharField(verbose_name="Ism, familyasi", max_length=100, null=False, blank=False)
	passport = models.CharField(verbose_name="Passporti ", max_length=10, unique=True, null=False, blank=False, validators=[validate_max_length])
	birthday = models.DateField(verbose_name="Tug'ilgan kuni")
	province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='province')
	district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='district')

	def __str__(self):
		return self.full_name
