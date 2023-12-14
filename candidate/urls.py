from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'candidate'

urlpatterns = [
    path('', views.create, name='candidate-create'),
    path('update/<int:pk>/', views.update, name='candidate-update')
]

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
