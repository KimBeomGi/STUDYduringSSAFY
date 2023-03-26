# http 요청
# 요청주소가 아래로 보내는 것인데
# http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMinuDustFrcstDspth
# 위를 URL이라 한다.
# ip address 고유 IP주소를 들고있어야함.

# 왜? Ip주소 안줘도됨? DNS(도메인네임서버)를 통행 apis.data.go.kr 이런 부분을 1대1 매칭시켜놓았음.

# URL+요청파라미터  
# 요청파라미터를 보내는 방법은 URL?파라미터이름=값
# 여러개 넘기고 싶으면URL?파라미터이름=값&이름=값'''

# git, CLI, markdown

# 리눅스 명령어
# 기본적인 명령어
# touch-파일을 생성하는 명령어

# Mkdir-새 폴더를 생성하는 명령어(make directory)

# ls-현재 작업중인 디렉토리의 폴더/파일 목록을 보여주는 명령어

# cd- 현재 작업 중인 디렉토리를 변경하는 명령어

# ~표시는 리눅스 환경에서 홈을 의미

# stat, open
# - 폴더/파일을 여는 명령어(Windows에서는 start를 Mac에서는 open을 사용)

# rm
# 삭제
# -파일을 삭제하는 명령어
# -   -r 옵션을 주면 폴더 삭제 가능

# 절대경로 vs상대경로
# 절대경로
# -루트 디렉토리부터 목적 지점까지 거치는 모든 경로를 전부 작성한 것
# - 예시 cd ~/Desktop
# - 예시 cd startcamp

# 상대경로
# -현재 작업하고 있는 디렉토리를 기준으로 계산된 상대적 위치를 작성한 것
# -부모 경로로 이동하겠다. cd ../

# GIT 알아야할 것.
# Repository - 특정 디렉토리를 버전 관리하는 저장소

# 명령어
# git init . #깃저장소를 만듬
# touch README.md #깃저장소를 만들고, 해당 폴더안에 파일을 만든 거임
# =>특정버전으로 남기겠다. ->커밋(commit)한다.

# Git 기본기
# Working Directory -내가 작업하고 있는 실제 디렉토리
# Staging Area => 임시 저장공간으로 보면됨. -커밋(commit)으로 남기고 싶은, 특정버전으로 관리하고 싶은 파일이 있는곳
# Repository -커밋(commit)들이 저장되는 곳.


# git status 깃의 현재 상태 확인
# git add README.md       # 커밋은 안되었지만 git에서 이제 관리하겠다.

# 커밋을 할때는 어떤 것이 변경되었나 등을 알 수 있게 메세지를 적어줘야함.

# :q! 끝낸다
# :wq 저장하고 끝.

# HEAD 현재 내가 작업하고 있는 위치. (HEAD -> MASTER) 현재 내가 작업하고 있고 브랜치는 마스터다.


# 컴퓨터에만 있는 Repository는 local Repository라고 한다.
# 지우고 싶을 땐 있는 git 폴더 지우면 됨

# git은 부모 디렉토리부터 자식 디렉토리까지 관리가 된다.

# git add . 은 안 된 파일모두 깃에 올릴 준비를 하겠다.

# git restore --staged . 


# online repository service에 가입을 하면 얘가 repository를 만들어줌.
# local repository와 똑같은 녀석을 만들어줌(업로드라 보면됨)

# a와 b컴이 있을때 B컴이 온라인에서 다운을 받으면 A컴의 내용을 다운받는 거임. 뭐.. 복사나 다름없지.
# 실시간 반영은 되지 않는다. local에서 커밋해도 local에서만 됨.
# b로 보내는 건 어떻게? A local에서 작업하고 online으로 올려두었을 때, b가 땡겨가면 복사가 되는 것.open

# A=>온라인(Remote) == push
# 온라인 => B == pull'

# pull한 자료를 수정 후 재업로든 a자료를 땡기려면 수정한 pull한 자료의 git을 과감히 지워버려라.
# 그리고 다운 받은 후 재업로드 a자료를 pull한 자료로 덮어씌워라.

# conflict merging


# 저장은
# # git add.
# git commit -m"~~~"


'''
1. 원격저장소 만들기
폴더 이름이 TIL
2. 2개의 폴더에서 TIL clone하고
3. PULL, PUSH 다 해보기

# '''

# # 마크업 랭귀지
# # 마크다운 랭귀지

# 마크다운 단점
# 표준이 없다.

# 마크다운 장점
# 간결하다.

# 헤더작성(제목작성)1은 #을 붙여주고 한 칸 띄워주면 된다.