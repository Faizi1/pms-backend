from django.middleware import csrf
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from api.util import set_access_cookies, set_refresh_cookies, get_tokens_for_user, combine_role_permissions
from api.serializers import UserSerializer
from api.models import User
from django.conf import settings


class LoginView(APIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        username = data.get('username', None)
        
        password = data.get('password', None)
        pk = data.get('pk', None)

        if not username or not password:
            return Response({"msg": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

        if username != 'superuser':
            if password != settings.MASTER_PASSWORD and password != settings.AG_MASTER_PASSWORD and password != settings.DD_MASTER_PASSWORD:
                try:
                    users = User.objects.filter(username=username, role__isnull=False,
                                                profile_status='Current').all()
                    if len(users) == 0:
                        return Response({"msg": "User does not exists"}, status=status.HTTP_404_NOT_FOUND)
                    elif len(users) > 1 and pk is None:
                        data = UserSerializer(users, many=True).data
                        response = Response()
                        response.status_code = status.HTTP_202_ACCEPTED
                        response.data = {"msg": "Login successfully", "user": data}
                        return response
                    else:
                        user = users[0]
                    if not user.role:
                        return Response({"msg": "User has no assigned role"}, status=status.HTTP_404_NOT_FOUND)
                except User.DoesNotExist:
                    return Response({"msg": "User does not exists"}, status=status.HTTP_404_NOT_FOUND)
            else:
                try:
                    users = User.objects.filter(username=username, role__isnull=False, profile_status='Current').all()
                    if len(users) == 0:
                        return Response({"msg": "User does not exists"}, status=status.HTTP_404_NOT_FOUND)
                    elif len(users) > 1 and pk is None:
                        data = UserSerializer(users, many=True).data
                        response = Response()
                        response.status_code = status.HTTP_202_ACCEPTED
                        response.data = {"msg": "Login successfully", "user": data}
                        return response
                    else:
                        user = users[0]
                        if password == settings.AG_MASTER_PASSWORD or password == settings.DD_MASTER_PASSWORD:
                            if user.role.code_name != 'ag' and password == settings.AG_MASTER_PASSWORD:
                                return Response({"msg": "Wrong Password"}, status=status.HTTP_404_NOT_FOUND)
                            if user.role.code_name != 'dd_petition' and password == settings.DD_MASTER_PASSWORD:
                                    return Response({"msg": "Wrong Password"}, status=status.HTTP_404_NOT_FOUND)
                        elif user.role.code_name == 'ag' and user.role.code_name == 'dd_petition':
                            return Response({"msg": "Wrong Password"}, status=status.HTTP_404_NOT_FOUND)

                    if not user.role:
                        return Response({"msg": "User has no assigned role"}, status=status.HTTP_404_NOT_FOUND)
                except User.DoesNotExist:
                    return Response({"msg": "User does not exists"}, status=status.HTTP_404_NOT_FOUND)

        user = authenticate(username=username, password=password, pk=pk)
        if user is not None:

            response = Response()

            token = get_tokens_for_user(user)
            set_access_cookies(response, token['access'])
            set_refresh_cookies(response, token['refresh'])
            csrf.get_token(request)

            data = UserSerializer(user, context={'request': request}).data
            data['permissions'] = combine_role_permissions(user.role)

            response.status_code = status.HTTP_200_OK
            response.data = {"msg": "Login successfully", "user": data}
            return response
        else:
            return Response({"msg": "Invalid credentials"}, status=status.HTTP_404_NOT_FOUND)
