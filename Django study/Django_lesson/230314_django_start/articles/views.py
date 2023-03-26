from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# 여기 들어가는 함수는 모양이 정해져 있슴.
# 파라미터가 하나 있어야합니다. 이름은 상관없지만 request라고 통일
# 응답(HttpResponse)을 반환해야한다. 
def hello(request):
    # html = '<html>'
    # html += '<head>'
    # html += '<body>'
    # html += '<h1>'
    # html += '안녕하세요!'
    # html += '</h1>'
    # html += '</body>'
    # html += '</head>'
    # html += '</html>'
    # return HttpResponse(html)
    # ########
    # 내가 템플릿을 가지고 있는데.. 그것 이용해서 html 만들어
    # 템플릿에 데이터 넘겨주기
    # 템플릿에 데이터를 넘겨줄때는 dictionary형태로 전달

    context={
        'name':'김범기'
    }

    return render(request, 'articles/hello.html', context) # 함수 호출 결과가 HttpResponse
    # return render(request, 템플릿 이름)