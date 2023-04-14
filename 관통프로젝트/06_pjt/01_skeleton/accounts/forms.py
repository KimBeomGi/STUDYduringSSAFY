from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'last_name','first_name',)
        # fields = '__all__'

class CustomUserChangeForm(UserChangeForm):
    # class Meta(UserCreationForm.Meta):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username')