from django.contrib import admin
from django.urls import path, include
# Three modules for swagger:
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#below shema_view for swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Flight Reservation API",
        default_version="v1",
        description="Flight Reservation API project provides flight and reservation info",
        terms_of_service="#",
        contact=openapi.Contact(
            email="yilmax4@gmail.com"),  # Change e-mail on this line!
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('users/', include('users.urls')),
    # path('flight/', include('flight.urls')),
    
    
    # Url paths for swagger:
    path("swagger(<format>\.json|\.yaml)", schema_view.without_ui(
        cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger",
        cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc",
        cache_timeout=0), name="schemaredoc"),
#below path for debug tool-bar
    path('__debug__/', include('debug_toolbar.urls')),


]
#yada debug true ise path'i aktif et şeklinde yazılabilir
# if DEBUG:
#     urlpatterns += path('__debug__/', include('debug_toolbar.urls'))