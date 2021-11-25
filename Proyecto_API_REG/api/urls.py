from django.urls import path
from .views import registrarView
urlpatterns=[
    path('registrar/',registrarView.as_view(), name='registrar_list'),
    path('registrar/<int:id>',registrarView.as_view(), name='registrar_process')
]