from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from accounts.models import User
from .forms import ProjectForm
from .models import Project


def admin_only(request):
    return request.user.is_authenticated and (
        request.user.role == User.Role.ADMIN
    )


@login_required
def project_list(request):
    if not admin_only(request):
        return redirect("accounts:member_dashboard")

    projects = Project.objects.all()

    return render(
        request,
        "projects/project_list.html",
        {"projects": projects},
    )


@login_required
def project_create(request):
    if not admin_only(request):
        return redirect("accounts:member_dashboard")

    if request.method == "POST":
        form = ProjectForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Project created successfully."
            )
            return redirect("projects:project_list")

    else:
        form = ProjectForm()

    return render(
        request,
        "projects/project_form.html",
        {
            "form": form,
            "page_title": "Create Project",
            "button_text": "Create Project",
        },
    )


@login_required
def project_edit(request, pk):
    if not admin_only(request):
        return redirect("accounts:member_dashboard")

    project = get_object_or_404(Project, pk=pk)

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Project updated successfully."
            )
            return redirect("projects:project_list")

    else:
        form = ProjectForm(instance=project)

    return render(
        request,
        "projects/project_form.html",
        {
            "form": form,
            "page_title": "Edit Project",
            "button_text": "Update Project",
        },
    )


@login_required
def project_delete(request, pk):
    if not admin_only(request):
        return redirect("accounts:member_dashboard")

    project = get_object_or_404(Project, pk=pk)

    if request.method == "POST":
        project.delete()
        messages.success(
            request,
            "Project deleted successfully."
        )
        return redirect("projects:project_list")

    return render(
        request,
        "projects/project_confirm_delete.html",
        {"project": project},
    )