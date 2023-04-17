from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Article, Comment
from .serializers import ArticleListSerializer, CommentSerializer, ArticleDetailSerializer
# from .forms import ArticleForm

# Create your views here.
# GET : 게시글 전체 목록 조회
# POST : 게시글 작성
@api_view(['GET','POST'])   
def article_list(request):
    if request.method =='GET':
        #게시글 전체 목록 가져오기
        articles = Article.objects.all()
        # JSON 으로 변환해서 응답
        serializer = ArticleListSerializer(articles,many=True)
        # serializer.data
        return Response(serializer.data)
    elif request.method == 'POST':
        # 요청으로 들어온 데이터를 DB에 저장하고, 생성된 객체를 반환
        # 이전 model form이 했던 역할을 serializer가 대신합니다.
        serializer = ArticleListSerializer(data=request.POST)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        # 저장되었는지 안되었는지만 알려줘도 되겠지만....
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        # return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)   #데이터 잘못됐다!
@api_view(['GET','DELETE','PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    if request.method=='GET':
        # serializer = ArticleListSerializer(article)
        serializer = ArticleDetailSerializer(article)
        # 게시글 하나 가져오기
        # JSON으로 변환해서 응답
        return Response(serializer.data)
    elif request.method=='PUT':
        # 요청에서 수정된 데이터 받아서 저장
        serializer = ArticleListSerializer(instance=article,data=request.POST)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # 결과 반환
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    elif request.method=='DELETE':
        # 해당 게시글 삭제후 결과반환
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def comment_list(request):
    #전체 댓글 목록 조회해서 반환 >> 댓글들을 직렬화 해서 반환 
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET','PUT','DELETE'])
def comment_detail(request,comment_pk):
    comment = get_object_or_404(Comment,pk=comment_pk)
    if request.method=='GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer = CommentSerializer(instance=comment,data=request.POST)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method=='DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 게시글에 달린 댓글 전체조회  + 댓글 작성
# http://127.0.0.1:8000/api/v1/articles/50/comments/
@api_view(['GET','POST'])
def article_comment_list(request,article_pk):
    article = get_object_or_404(Article,pk = article_pk)
    if request.method=='POST':
        # 댓글 작성
        serializer = CommentSerializer(data=request.POST)
        if serializer.is_valid(raise_exception=True):
            # 댓글이 참조하고 있는 article을 설정해주면 됩니다.
            # Serializer에 read_only_fields에 article을 설정해줬기 때문에
            # validataion 검사에서 article은 빠짐 
            serializer.save(article=article)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        # return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


