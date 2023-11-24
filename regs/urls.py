from django.urls import path
from regs.views import RegStepOneApiView

app_name = 'regs'
urlpatterns = [
	path('/', RegStepOneApiView.as_view(), name='regOne')



]