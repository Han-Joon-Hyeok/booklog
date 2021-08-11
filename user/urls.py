from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('profile/<str:id>', views.profile, name="profile"),
    path('writeProfile/<int:pk>', views.writeprofile, name="writeprofile"),
    # path('writeProfile/<str:id>', pv.writeprofile, name="writeprofile"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
