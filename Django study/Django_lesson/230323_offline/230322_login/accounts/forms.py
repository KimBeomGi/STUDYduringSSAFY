# CustomUserCreationForm
# CustomUserChangeForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import User # 이렇게 안쓰고, Django가 추천하는 방법으로 사용
from django.contrib.auth import get_user_model

# 인증에 사용하는 User모델을 변경했기 때문에,
# UserCreationForm과 UserChangeForm을 그대로 사용하지 못함
# 얘네들은 기본적으로 auth.User를 사용하도록 구현되어 있음.
# User Model을 accounts.User를 사용하도록 변경
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')