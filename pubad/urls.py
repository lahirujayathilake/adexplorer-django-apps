from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.index, name='pubad_index'),

    # ajax urls
    url(r'^api/get_genenames_pubad/', views.get_genenames_pubad, name='get_genenames_pubad'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
