from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer


@api_view(['GET'])
def director_list_view(request):
    directors = Director.objects.all()
    data = DirectorSerializer(directors, many=True).data
    return Response(data=data)


@api_view(['GET'])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not Found!'},
                        status=status.HTTP_404_NOT_FOUND)
    data = DirectorSerializer(director).data
    return Response(data=data)


@api_view(['GET'])
def movie_list_view(request):
    directors = Movie.objects.all()
    data = MovieSerializer(directors, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movie_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Movie not Found!'},
                        status=status.HTTP_404_NOT_FOUND)
    data = DirectorSerializer(movie).data
    return Response(data=data)


@api_view(['GET'])
def review_list_view(request):
    reviews = Review.objects.all()
    data = DirectorSerializer(reviews, many=True).data
    return Response(data=data)


@api_view(['GET'])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Review not Found!'},
                        status=status.HTTP_404_NOT_FOUND)
    data = DirectorSerializer(review).data
    return Response(data=data)
