from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Paragraph, CustomUser
from django.db.models import Count, Q
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Paragraph
from django.db.models import Q
from .models import CustomUser


@api_view(['POST'])
def create_user(request):
    data = request.data
    try:
        user = CustomUser.objects.create(
            name=data['name'],
            email=data['email'],
            dob=data.get('dob')
        )
        return Response("User created successfully", status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user(request, user_id):
    try:
        user = CustomUser.objects.get(pk=user_id)
        user_data = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'dob': user.dob,
            'created_at': user.created_at,
            'modified_at': user.modified_at
        }
        return Response(user_data)
    except CustomUser.DoesNotExist:
        return Response("User not found", status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def create_paragraph(request):
    text = request.data.get('text', '')
    user_email = request.data.get('user_email', '')

    if not text:
        return Response("Text cannot be empty", status=400)

    text = text.lower()

    paragraphs = text.split('\n\n')

    paragraph_dict = {}
    word_index_dict = {}
    token_dict = {}

    for idx, paragraph_text in enumerate(paragraphs, start=1):
        paragraph_text = paragraph_text.strip()

        paragraph_dict[idx] = paragraph_text

        words = paragraph_text.split()
        token_dict[idx] = words

        for word in words:
            word = word.strip(',.?!')
            if word not in word_index_dict:
                word_index_dict[word] = []
            word_index_dict[word].append(idx)

    user = CustomUser.objects.get(email=user_email)
    try:
        user = CustomUser.objects.get(email=user_email)
        
    except CustomUser.DoesNotExist:
        return Response("User not found", status=404)

    paragraph = Paragraph.objects.create(
        text=paragraph_dict,
        word_index=word_index_dict,
        user=user,
        token_data=token_dict
    )

    return Response("Paragraph created successfully", status=201)


@api_view(['GET'])
def get_paragraph(request, paragraph_id):
    try:
        paragraph = Paragraph.objects.get(pk=paragraph_id)
        paragraph_data = {
            'id': paragraph.id,
            'text': paragraph.text,
            'user_id': paragraph.user_id,
            'created_at': paragraph.created_at,
            'token_data': paragraph.token_data,
            'word_index': paragraph.word_index
        }
        print("paragraph_data['word_index']")
        print(paragraph_data['word_index'])
        return Response(paragraph_data)
    except Paragraph.DoesNotExist:
        return Response("Paragraph not found", status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def search_word_in_paragraph(request):
    user_id = request.query_params.get('user_id')
    word = request.query_params.get('word')
    paragraph_id = request.query_params.get('paragraph_id')

    if not user_id or not word or not paragraph_id:
        return Response("User ID, word, and paragraph ID are required parameters", status=status.HTTP_400_BAD_REQUEST)

    try:
        paragraph = Paragraph.objects.get(user_id=user_id, id=paragraph_id)
        paragraph_text = paragraph.text

        matching_paragraph_keys = []

        word_found = False

        for key, value in paragraph_text.items():
            if word_found:
                matching_paragraph_keys.append(key)
                continue

            words = value.split()
            words = [word.lower() for word in words]
            if word.lower() in words:
                matching_paragraph_keys.append(key)
                word_found = True
        
        if matching_paragraph_keys:
            return Response({'matching_paragraph_keys': matching_paragraph_keys})
        else:
            return Response("Word not found in any paragraph", status=status.HTTP_404_NOT_FOUND)
    
    except Paragraph.DoesNotExist:
        return Response("Paragraph not found", status=status.HTTP_404_NOT_FOUND)


