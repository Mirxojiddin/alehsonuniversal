from django.urls import path
from regs.views import salom

app_name = 'regs'
urlpatterns = [
	path('/', salom, name = 'salom')



]