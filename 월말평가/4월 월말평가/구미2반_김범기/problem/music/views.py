from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Music, Review
from .serializers import (MusicListSerializer, MusicReviewCntSerializer,
                          MusicSerializer, ReviewSerializer)


@api_view(['GET', 'POST'])
def music_list(request):
    if request.method == 'GET':
        music_all = Music.objects.all()
        serializer = MusicListSerializer(music_all, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # 문제 2. MusicSerializer를 이용하여 유효성 검사 후 음악 정보를 생성할 수 있도록 코드를 완성하시오.
    elif request.method == 'POST':
        serializer = MusicSerializer(data=request.POST)
        # 유효성 검사!
        if serializer.is_valid(raise_exception=True):
            serializer.save()   # 유효성 검사했으니 저장!
            return Response(serializer.data) # 왜안되는거지......


@api_view(['GET', 'DELETE', 'PUT'])
def music_detail(request, music_pk):
    # 문제 3. 찾으려는 데이터가 없으면 404 상태 코드를 반환할 수 있도록 아래 코드를 완성하시오.
    # music = Music.objects.get(pk=music_pk)
    music = get_object_or_404(Music, pk=music_pk)   # get_object_or_404이용하였음.
    if request.method == 'GET':
        serializer = MusicReviewCntSerializer(data=music)
        return Response(serializer.data)
    
    # 문제 4. 음악 데이터를 삭제하고 {'delete': 삭제되는음악pk} 형태의 JSON으로 반환하도록 코드를 완성하시오.
    elif request.method == 'DELETE':
        music.delete()
        value = { 'delete' : music_pk }
        # return Response(value, status=status.HTTP_204_NO_CONTENT)
        return Response(value)

    # 문제 5. 음악 데이터를 수정할 수 있도록 아래 코드를 완성하시오.
    # 수정이 정상적으로 완료되었다면 수정된 데이터를 JSON 형태로 반환합니다.
    elif request.method == 'PUT':
        serializer = MusicSerializer(instance=music, data=request.POST)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.data)


# 문제 7. 모든 리뷰 정보를 반환하도록 review_list 코드를 완성하시오.
@api_view(['GET'])
def review_list(request):
    # reviews = Review.objects.all()    # 이 방법도 있고
    reviews = get_list_or_404(Review)   # 이 방법도 있고
    serializer = ReviewSerializer(reviews)
    return Response(serializer.data)



# 문제 8. 리뷰를 생성할 수 있도록 아래 코드를 완성하시오.
# 유효성 검사를 통과하지 못하면 정보와 400 상태코드를 반환합니다.
# 작성된 리뷰의 JSON과 함께 201 상태 코드를 반환합니다.
@api_view(['POST'])
def review_create(request, music_pk):
    serializer = ReviewSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=False):
        serializer(pk=music_pk)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET', 'DELETE'])
def review_detail(request, review_pk):
    # 문제 9. 리뷰 정보를 조회할 수 있도록 아래 코드를 완성하시오.
    # 찾는 리뷰가 없으면 404 상태 코드를 반환합니다.

    if request.method == 'GET':
        review = get_object_or_404(Review, pk=review_pk)
        serializer = ReviewSerializer(data=review)
        return Response(serializer.data)
    
    # 문제 10. DELETE 로 요청오는 경우 해당 리뷰가 삭제될 수 있도록 아래에 코드를 완성하시오.
    # 삭제하려는 리뷰가 없으면 404 상태 코드를 반환합니다.
    # 삭제가 정상적으로 완료되면 {'delete': 삭제된리뷰PK} 형태인 JSON이 204 상태코드와 함께 반환됩니다.
    elif request.method == 'DELETE':
        review = get_object_or_404(Review, pk=review_pk)
        review.delete()
        value = {'delete' : review_pk}
        return Response(value, status=status.HTTP_204_NO_CONTENT)