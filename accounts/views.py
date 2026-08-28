
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import TeamMemberCreationForm
from .models import User


# =========================================================
# LOGIN
# =========================================================

def login_view(request):

    # If already logged in, send user to the correct dashboard
    if request.user.is_authenticated:
        return redirect_after_login(request.user)

    if request.method == "POST":

        username = request.POST.get(
            "username",
            ""
        ).strip()

        password = request.POST.get(
            "password",
            ""
        )

        # Authenticate user
        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is not None:

            # Create login session
            login(
                request,
                user
            )

            # Redirect based on role
            return redirect_after_login(user)

        # Invalid credentials
        messages.error(
            request,
            "Invalid username or password."
        )

    return render(
        request,
        "accounts/login.html"
    )


# =========================================================
# ROLE BASED REDIRECT
# =========================================================

def redirect_after_login(user):

    if user.role == User.Role.ADMIN:

        return redirect(
            "accounts:admin_dashboard"
        )

    return redirect(
        "accounts:member_dashboard"
    )


# =========================================================
# LOGOUT
# =========================================================

def logout_view(request):

    logout(request)

    return redirect(
        "accounts:login"
    )


# =========================================================
# COMMON DASHBOARD REDIRECT
# =========================================================

@login_required
def dashboard(request):

    return redirect_after_login(
        request.user
    )


# =========================================================
# ADMIN DASHBOARD
# =========================================================

@login_required
def admin_dashboard(request):

    # Only Admin can access
    if request.user.role != User.Role.ADMIN:

        return redirect(
            "accounts:member_dashboard"
        )

    # Import models here to avoid unnecessary circular imports
    from projects.models import Project
    from tasks.models import Task

    # -----------------------------------------------------
    # PROJECT STATISTICS
    # -----------------------------------------------------

    projects = Project.objects.all()

    total_projects = projects.count()


    # -----------------------------------------------------
    # TASK STATISTICS
    # -----------------------------------------------------

    total_tasks = Task.objects.count()


    completed_tasks = Task.objects.filter(
        status=Task.Status.COMPLETED
    ).count()


    pending_tasks = Task.objects.exclude(
        status=Task.Status.COMPLETED
    ).count()


    # -----------------------------------------------------
    # OVERALL PROGRESS
    # -----------------------------------------------------

    overall_progress = 0

    if total_tasks > 0:

        overall_progress = round(
            (completed_tasks / total_tasks) * 100
        )


    # -----------------------------------------------------
    # RECENT PROJECTS
    # -----------------------------------------------------

    recent_projects = projects[:5]


    # -----------------------------------------------------
    # CONTEXT
    # -----------------------------------------------------

    context = {

        "projects": projects,

        "recent_projects": recent_projects,

        "total_projects": total_projects,

        "total_tasks": total_tasks,

        "completed_tasks": completed_tasks,

        "pending_tasks": pending_tasks,

        "overall_progress": overall_progress,

    }


    return render(
        request,
        "accounts/admin_dashboard.html",
        context
    )


# =========================================================
# TEAM MEMBER DASHBOARD
# =========================================================

@login_required
def member_dashboard(request):

    # Only Team Member can access
    if request.user.role != User.Role.TEAM_MEMBER:

        return redirect(
            "accounts:admin_dashboard"
        )

    return render(
        request,
        "accounts/member_dashboard.html"
    )


# =========================================================
# ADD TEAM MEMBER
# =========================================================

@login_required
def add_team_member(request):

    # Only Admin can add users
    if request.user.role != User.Role.ADMIN:

        return redirect(
            "accounts:member_dashboard"
        )


    if request.method == "POST":

        form = TeamMemberCreationForm(
            request.POST
        )


        if form.is_valid():

            # Save Team Member
            form.save()


            messages.success(
                request,
                "Team member created successfully."
            )


            return redirect(
                "accounts:team_members"
            )


    else:

        form = TeamMemberCreationForm()


    return render(
        request,
        "accounts/add_team_member.html",
        {
            "form": form
        }
    )


# =========================================================
# TEAM MEMBERS LIST
# =========================================================

@login_required
def team_members(request):

    # Only Admin can view members
    if request.user.role != User.Role.ADMIN:

        return redirect(
            "accounts:member_dashboard"
        )


    members = User.objects.filter(
        role=User.Role.TEAM_MEMBER
    ).order_by(
        "username"
    )


    return render(
        request,
        "accounts/team_members.html",
        {
            "members": members
        }
    )

