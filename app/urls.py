from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, logout_then_login

urlpatterns = [
    path("accounts/login/", views.login1, name="login"),
    path("logout/", logout_then_login, name="logout"),


    path("checkbox", views.checkbox, name="checkbox"),
    path("home2", views.home2, name="home2"),
    path("", views.home1, name="home1"),
    path("yafetChore", views.yafetChore, name="yafetChore"),
    
    path("AddUser", views.AddUser, name="AddUser"),
    path("thanks/", views.thanks, name="thanks"),
    path("user/<user_id>/", views.user, name="user"),
    #path("check/", views.CHECKBOXES, name="checkboxes"),
    path("chore/<chore_id>", views.chore, name="chore"),
    path("<int:year>/<str:month>/", views.calendar, name="calendar"),
    #path("add_event/", views.add_event, name="add-event"),
    path("addChore/", views.addChore, name="addChore"),
    path("addedChore/", views.addedChore, name="addedChore"),
    path("editChore/<int:id>/", views.editChore, name="editChore"),
    path("deleteChore/<int:id>", views.removeChore, name="deleteChore"),
    path("startChore/<int:id>", views.startChore, name="startChore")
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)              #That is a conf for media file