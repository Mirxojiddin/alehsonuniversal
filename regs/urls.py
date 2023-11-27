from django.urls import path
from regs.views import RegStepOneApiView,RegStepTwoApiView, PaginationTypeApiView, DistrictApiView, ProvinceApiView

app_name = 'regs'
urlpatterns = [
	path('reg-one', RegStepOneApiView.as_view(), name='regOne'),
	path('reg-two', RegStepTwoApiView.as_view(), name='regTwo'),
	path('pagination-type', PaginationTypeApiView.as_view(), name='pagination'),
	path('district', DistrictApiView.as_view(), name='district'),
	path('province', ProvinceApiView.as_view(), name='province')

]