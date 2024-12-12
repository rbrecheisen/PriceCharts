from django.urls import path

from .views import auth, healthcheck, custom_logout, logs, filesets, fileset


urlpatterns = [
    path('auth', auth),
    path('logs/', logs),
    path('healthcheck/', healthcheck),
    path('accounts/logout/', custom_logout, name='logout'),
    path('', filesets),
    path('filesets/', filesets),
    path('filesets/<str:fileset_id>', fileset),
]