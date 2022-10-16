from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *
urlpatterns = [
    path('', home, name="Home"),
    path('api/links', SocailMediaLinkApiView.as_view(),
         name="SocailMediaLinkApiView"),
    path('api/links/<int:pk>/', SocailMediaLinkApiView.as_view(),
         name="SocailMediaLinkApiView"),
    path('api/blogs', BlogModelApiView.as_view(), name="BlogModelApiView"),
    path('api/blogs/<int:pk>/',
         BlogModelApiView.as_view(), name="BlogModelApiView"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
