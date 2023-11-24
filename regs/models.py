from django.db import models


class RegStepOne(models.Model):
	full_name = models.CharField(verbose_name="Ism, familyasi", max_length=100, null=False, blank=False)
	passport = models.CharField(verbose_name="Passporti ", max_length=8, unique=True, null=False, blank=False)
	birthday = models.DateField(verbose_name="Tug'ilgan kuni")

	def __str__(self):
		return self.full_name


# Create your models here.
