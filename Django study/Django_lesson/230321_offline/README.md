1. app 만들기 articles
  python manage.py startapp articles
  setting.py app 등록
2.  url 설정
    path('articles/', include('articles.urls')),
3. Article 모델 작성
      makemigrations , migrate
4. template 설정하기 
      app/template 폴더 생성
      1. 게시글 목록을 보여줄 화면
      2. 게시글 하나의 상세를 보여줄 화면
      3. 새로운 게시글을 작성하기 위한 화면
      4. 게시글 수정을 위한 화면
      base.html  생성후 template DIR(settings.py) 설정


5. form 요소 작성하기
  form 요소의 input요소의 name 속성은 서버로 데이터를 전달할 때 필요하다.
  <form action="">
    <label for="title">제목 : </label>
    <input type="text" id="title" name="title"> 
  </form>


