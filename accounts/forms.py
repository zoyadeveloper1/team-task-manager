
from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class TeamMemberCreationForm(forms.ModelForm):
    """
    Form used by an Admin to create a Team Member account.
    """

    password = forms.CharField(
        label="Password",
        required=True,
        min_length=8,
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control-custom",
                "placeholder": "Enter password",
                "autocomplete": "new-password",
                "id": "id_password",
            }
        ),
        help_text="Password must contain at least 8 characters.",
    )

    class Meta:
        model = User

        fields = [
            "username",
            "email",
            "password",
        ]

        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-control-custom",
                    "placeholder": "Enter username",
                    "autocomplete": "username",
                    "id": "id_username",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control-custom",
                    "placeholder": "Enter email address",
                    "autocomplete": "email",
                    "id": "id_email",
                }
            ),
        }

    def clean_username(self):
        """
        Validate username uniqueness.
        """

        username = self.cleaned_data.get("username", "").strip()

        if not username:
            raise forms.ValidationError(
                "Username is required."
            )

        if User.objects.filter(
            username__iexact=username
        ).exists():
            raise forms.ValidationError(
                "This username is already in use."
            )

        return username

    def clean_email(self):
        """
        Validate email and prevent duplicate email accounts.
        """

        email = self.cleaned_data.get("email", "").strip()

        if not email:
            raise forms.ValidationError(
                "Email address is required."
            )

        if User.objects.filter(
            email__iexact=email
        ).exists():
            raise forms.ValidationError(
                "This email address is already in use."
            )

        return email

    def clean_password(self):
        """
        Basic password validation.
        """

        password = self.cleaned_data.get("password")

        if not password:
            raise forms.ValidationError(
                "Password is required."
            )

        if len(password) < 8:
            raise forms.ValidationError(
                "Password must contain at least 8 characters."
            )

        return password

    def save(self, commit=True):
        """
        Create the user with a hashed password
        and automatically assign TEAM_MEMBER role.
        """

        user = super().save(commit=False)

        user.role = User.Role.TEAM_MEMBER

        user.set_password(
            self.cleaned_data["password"]
        )

        if commit:
            user.save()

        return user

