from django.contrib.auth.forms import BaseUserCreationForm
from django.forms import ModelForm

from engplat.base.models import User, File


class MyUserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "email",)


class FileModelForm(ModelForm):
    class Meta:
        model = File
        fields = ("title", "file",)
