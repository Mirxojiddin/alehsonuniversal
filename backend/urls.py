
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="All exson",
        default_version='v1',
        description="all exson uchun yaratilgan api",
        terms_of_service="https://yourapp.com/terms/",
        contact=openapi.Contact(email="umirxojiddin@gmail.coom"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/regs/', include('regs.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('schema-redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
