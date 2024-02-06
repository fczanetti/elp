from django.contrib.auth.forms import BaseUserCreationForm
from engplat.base.models import User


class MyUserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'email',)
