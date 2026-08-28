
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from accounts.models import User

from .forms import (
    TaskCommentForm,
    TaskEditForm,
    TaskForm,
    TaskStatusForm,
)

from .models import (
    DeadlineHistory,
    Task,
)


# =========================================================
# ADMIN - TASK LIST
# =========================================================


@login_required
def task_list(request):

    # Only Admin can access all tasks
    if request.user.role != User.Role.ADMIN:
        return redirect("accounts:member_dashboard")

    tasks = Task.objects.select_related(
        "project",
        "assigned_to",
    )

    # Search
    search = request.GET.get("search", "").strip()

    if search:
        tasks = tasks.filter(
            title__icontains=search
        )

    # Project filter
    project_id = request.GET.get("project", "").strip()

    if project_id:
        tasks = tasks.filter(
            project_id=project_id
        )

    # Assigned member filter
    member_id = request.GET.get("member", "").strip()

    if member_id:
        tasks = tasks.filter(
            assigned_to_id=member_id
        )

    # Priority filter
    priority = request.GET.get("priority", "").strip()

    if priority:
        tasks = tasks.filter(
            priority=priority
        )

    # Status filter
    status = request.GET.get("status", "").strip()

    if status:
        tasks = tasks.filter(
            status=status
        )

    # Data for filter dropdowns
    from projects.models import Project

    projects = Project.objects.all().order_by("name")

    members = User.objects.filter(
        role=User.Role.TEAM_MEMBER
    ).order_by("username")

    return render(
        request,
        "tasks/task_list.html",
        {
            "tasks": tasks,
            "projects": projects,
            "members": members,

            # Keep selected values in form
            "search": search,
            "selected_project": project_id,
            "selected_member": member_id,
            "selected_priority": priority,
            "selected_status": status,
        },
    )




# =========================================================
# ADMIN - CREATE TASK
# =========================================================

@login_required
def task_create(request):

    if request.user.role != User.Role.ADMIN:
        return redirect("accounts:member_dashboard")

    if request.method == "POST":

        form = TaskForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Task created successfully.",
            )

            return redirect("tasks:task_list")

    else:

        form = TaskForm()

    return render(
        request,
        "tasks/task_form.html",
        {
            "form": form,
            "page_title": "Create Task",
            "button_text": "Create Task",
        },
    )


# =========================================================
# ADMIN - EDIT TASK
# =========================================================

@login_required
def task_edit(request, pk):

    if request.user.role != User.Role.ADMIN:
        return redirect("accounts:member_dashboard")

    task = get_object_or_404(
        Task,
        pk=pk,
    )

    # Store the old deadline before saving
    old_deadline = task.deadline

    if request.method == "POST":

        form = TaskEditForm(
            request.POST,
            instance=task,
        )

        if form.is_valid():

            updated_task = form.save()

            # Save deadline history only when deadline changes
            if old_deadline != updated_task.deadline:

                DeadlineHistory.objects.create(
                    task=updated_task,
                    old_deadline=old_deadline,
                    new_deadline=updated_task.deadline,
                    changed_by=request.user,
                )

            messages.success(
                request,
                "Task updated successfully.",
            )

            return redirect(
                "tasks:task_list"
            )

    else:

        form = TaskEditForm(
            instance=task
        )

    return render(
        request,
        "tasks/task_form.html",
        {
            "form": form,
            "page_title": "Edit Task",
            "button_text": "Update Task",
            "is_edit": True,
            "task": task,
        },
    )


# =========================================================
# TEAM MEMBER - MY TASKS
# =========================================================

@login_required
def my_tasks(request):

    if request.user.role != User.Role.TEAM_MEMBER:
        return redirect("accounts:admin_dashboard")

    tasks = Task.objects.filter(
        assigned_to=request.user
    ).select_related(
        "project"
    )

    return render(
        request,
        "tasks/my_tasks.html",
        {
            "tasks": tasks,
        },
    )


# =========================================================
# TASK DETAIL
# =========================================================

@login_required
def task_detail(request, pk):

    task = get_object_or_404(
        Task.objects.select_related(
            "project",
            "assigned_to",
        ),
        pk=pk,
    )

    # Team member can view only their own task
    if request.user.role == User.Role.TEAM_MEMBER:

        if task.assigned_to != request.user:
            return redirect("tasks:my_tasks")

    status_form = TaskStatusForm(
        instance=task
    )

    comment_form = TaskCommentForm()

    history = task.deadline_history.select_related(
        "changed_by"
    )

    return render(
        request,
        "tasks/task_detail.html",
        {
            "task": task,
            "status_form": status_form,
            "comment_form": comment_form,
            "history": history,
        },
    )


# =========================================================
# TEAM MEMBER - UPDATE STATUS
# =========================================================

@login_required
def update_task_status(request, pk):

    task = get_object_or_404(
        Task,
        pk=pk,
    )

    if request.user.role != User.Role.TEAM_MEMBER:
        return redirect("accounts:admin_dashboard")

    if task.assigned_to != request.user:
        return redirect("tasks:my_tasks")

    if request.method == "POST":

        form = TaskStatusForm(
            request.POST,
            instance=task,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Task status updated successfully.",
            )

    return redirect(
        "tasks:task_detail",
        pk=pk,
    )


# =========================================================
# TEAM MEMBER - ADD COMMENT / PROGRESS
# =========================================================

@login_required
def add_comment(request, pk):

    task = get_object_or_404(
        Task,
        pk=pk,
    )

    if request.user.role != User.Role.TEAM_MEMBER:
        return redirect("accounts:admin_dashboard")

    if task.assigned_to != request.user:
        return redirect("tasks:my_tasks")

    if request.method == "POST":

        form = TaskCommentForm(
            request.POST
        )

        if form.is_valid():

            comment = form.save(
                commit=False
            )

            comment.task = task
            comment.user = request.user

            comment.save()

            messages.success(
                request,
                "Progress update added successfully.",
            )

    return redirect(
        "tasks:task_detail",
        pk=pk,
    )

