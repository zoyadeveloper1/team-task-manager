
from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    path("dashboard/", views.dashboard, name="dashboard"),

    path(
        "admin-dashboard/",
        views.admin_dashboard,
        name="admin_dashboard"
    ),

    path(
        "member-dashboard/",
        views.member_dashboard,
        name="member_dashboard"
    ),

    path(
        "team-members/",
        views.team_members,
        name="team_members"
    ),

    path(
        "team-members/add/",
        views.add_team_member,
        name="add_team_member"
    ),
]

