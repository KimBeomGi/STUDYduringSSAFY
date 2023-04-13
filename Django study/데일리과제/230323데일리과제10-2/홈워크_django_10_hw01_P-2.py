from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST
from django.shortcuts import redirect
# 이 부분 수정함
from django.contrib.auth import update_session_auth_hash

@require_POST
def delete(request):
    if request.user.is_authenticated:
        auth_logout(request)
        request.user.delete()
        # 이 부분 수정함
        update_session_auth_hash(request)
    return redirect('articles:index')
