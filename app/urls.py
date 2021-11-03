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
    path("<int:year>/<str:month>/", views.calendar, name="calendar"),
    #path("add_event/", views.add_event, name="add-event"),
    path("addChore/", views.addChore, name="addChore"),
    path("addedChore/", views.addedChore, name="addedChore"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)              #That is a conf for media file