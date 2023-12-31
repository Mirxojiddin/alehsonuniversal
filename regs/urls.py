from django.urls import path, include
from rest_framework.routers import DefaultRouter

from regs.views import RegStepOneApiView, RegStepTwoApiView, PaginationTypeApiView, DistrictApiView, ProvinceApiView, \
	ProvinceDetailApiView, DistrictDetailApiView, PaginationSearchApiView, PaginationDetailSearchApiView


app_name = 'regs'
urlpatterns = [
	path('reg-one', RegStepOneApiView.as_view(), name='regOne'),
	path('reg-two', RegStepTwoApiView.as_view(), name='regTwo'),
	path('pagination-type', PaginationTypeApiView.as_view(), name='pagination'),
	path('district', DistrictApiView.as_view(), name='district'),
	path('district/<int:id>', DistrictDetailApiView.as_view(), name='district detail'),
	path('province', ProvinceApiView.as_view(), name='province'),
	path('province/<int:id>', ProvinceDetailApiView.as_view(), name='province detail'),
	path('pagination-search', PaginationSearchApiView.as_view(), name='pagination search'),
	path('pagination-search/<int:pk>', PaginationDetailSearchApiView.as_view(), name='pagination detail'),
	path('api-auth/', include('rest_framework.urls')),
]
