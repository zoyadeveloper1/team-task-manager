from django import forms

from accounts.models import User

from .models import Task, TaskComment


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task

        fields = [
            "project",
            "title",
            "description",
            "assigned_to",
            "priority",
            "status",
            "deadline",
        ]

        widgets = {
            "project": forms.Select(
                attrs={
                    "class": "form-control-custom",
                }
            ),

            "title": forms.TextInput(
                attrs={
                    "class": "form-control-custom",
                    "placeholder": "Enter task title",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control-custom",
                    "placeholder": "Add task description",
                    "rows": 5,
                }
            ),

            "assigned_to": forms.Select(
                attrs={
                    "class": "form-control-custom",
                }
            ),

            "priority": forms.Select(
                attrs={
                    "class": "form-control-custom",
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-control-custom",
                }
            ),

            "deadline": forms.DateInput(
                attrs={
                    "class": "form-control-custom",
                    "type": "date",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["assigned_to"].queryset = User.objects.filter(
            role=User.Role.TEAM_MEMBER
        )

        self.fields["description"].required = False


class TaskEditForm(TaskForm):
    pass


class TaskStatusForm(forms.ModelForm):
    class Meta:
        model = Task

        fields = ["status"]

        widgets = {
            "status": forms.Select(
                attrs={
                    "class": "form-control-custom",
                }
            ),
        }


class TaskCommentForm(forms.ModelForm):
    class Meta:
        model = TaskComment

        fields = ["comment"]

        widgets = {
            "comment": forms.Textarea(
                attrs={
                    "class": "form-control-custom",
                    "placeholder": "Add your progress update...",
                    "rows": 5,
                }
            ),
        }

    def clean_comment(self):
        comment = self.cleaned_data.get("comment", "").strip()

        if not comment:
            raise forms.ValidationError(
                "Progress comment is required."
            )

        return comment