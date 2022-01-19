from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from apps.users.models import User
from apps.users.serializers import UserSerializer, UserUpdateSerializer, ChangePasswordSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response(serializer.data, status = status.HTTP_200_OK)

class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

class UserListView(APIView): 
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        users = User.objects.all()

        paginator = PageNumberPagination()
        paginator.page_size = 10
        result_page = paginator.paginate_queryset(users, request)
        serializer = UserSerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)

class UserDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        user = User.objects.filter(id = pk).first()
        if user:
            user_serializer = UserSerializer(user)    
            return Response(user_serializer.data, status = status.HTTP_200_OK)

        return Response({'message': f'User with id: {pk} does not exists.'}, status = status.HTTP_400_BAD_REQUEST)

class UpdateUserView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, pk):
        user = User.objects.filter(id = pk).first()
        if user:
            user_serializer = UserUpdateSerializer(user, data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status = status.HTTP_200_OK)

            return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        return Response({'message': f'User with id: {pk} does not exists.'}, status = status.HTTP_400_BAD_REQUEST)

class DeleteUserView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, pk):
        user = User.objects.filter(id = pk).first()
        if user:
            user.delete()
            return Response({'message': 'User deleted successfully!'}, status = status.HTTP_204_NO_CONTENT)

        return Response({'message': f'User with id: {pk} does not exists.'}, status = status.HTTP_400_BAD_REQUEST)

