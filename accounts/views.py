from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from convert_numbers import persian_to_english
from .serializers import UserSerializer, UserLoginSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import authenticate


class UserRegisterView(APIView):

    def post(self, request):
        """
        parameters:
        1. first_name
        2. last_name
        3. phone_number
        4. national_code
        5. city
        6. email
        7. password
        """
        form = request.data
        ser_data = UserSerializer(data=form)
        if ser_data.is_valid():
            phone_number = persian_to_english(form['phone_number'])
            user = User.objects.filter(phone_number=phone_number).exists()
            if not user:
                User.objects.create_user(first_name=form['first_name'], last_name=form['last_name'],
                                         phone_number=phone_number, national_code=form['national_code'],
                                         city=form['city'], email=form['email'], password=form['password'])
                return Response(data=ser_data.data, status=status.HTTP_201_CREATED)
            else:
                return Response(data={'message': 'user with this Email already exists.'},
                                status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        else:
            return Response(data=ser_data.errors, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)


class UserLoginView(APIView):

    def post(self, request):
        """
        parameters:
        1. email
        2. password
        """
        form = request.POST
        ser_data = UserLoginSerializer(data=form)
        if ser_data.is_valid():
            try:
                user = authenticate(request, email=form['email'], password=form['password'])
                if user is not None:
                    user = User.objects.get(email=form['email'])
                    token_access = AccessToken.for_user(user)
                    token_refresh = RefreshToken.for_user(user)
                    return Response(data={'access': str(token_access), 'refresh': str(token_refresh)}, status=status.HTTP_200_OK)
                else:
                    return Response(data='user invalid', status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
            except:
                user = None

        return Response(data=ser_data.errors, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)


class UserLogout(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
