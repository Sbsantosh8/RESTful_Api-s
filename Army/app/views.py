from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from django.contrib.auth.models import User


class RegisterUserAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User registered successfully"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListUserAPIView(APIView):
    def get(self, request, username=None):
      
        
        if username is not None:
            queryset = User.objects.get(username=username)
            serializer = RegisterSerializer(queryset)
            return Response(serializer.data)

        else:
            queryset = User.objects.all()
            serializer = RegisterSerializer(queryset, many=True)

            return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateUserAPIView(APIView):

    def put(self, request, username=None):

        if username is not None:
            queryset = User.objects.get(username=username)
            serializer = RegisterSerializer(instance=queryset, data=request.data)

            if serializer.is_valid():
                # Save the updated user
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class DeleteUserAPIView(APIView):

    def delete(self, request, username=None):
        if username is not None:
            try:
                # Try to get the user by username
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                # Return 404 if the user is not found
                return Response(
                    {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
                )

            # If user is found, delete the user
            user.delete()
            return Response(
                {"message": f"User {username} deleted successfully."},
                status=status.HTTP_200_OK,
            )

        # Return 400 Bad Request if username is not provided
        return Response(
            {"error": "Username is required"}, status=status.HTTP_400_BAD_REQUEST
        )
