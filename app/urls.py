from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("form", views.get_name, name="form"),
    path("thanks/", views.thanks, name="thanks"),
    path("user/<user_id>/", views.user, name="user"),
    path("check/", views.CHECKBOXES, name="checkboxes"),
    path("chore/<chore_id>", views.chore, name="chore"),
    #path("katian/", views.katian, name="katian"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)