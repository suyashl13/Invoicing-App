import json
import re

from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes, authentication_classes, api_view
from rest_framework.permissions import IsAuthenticated

from .models import CustomUser
from django.views.decorators.csrf import csrf_exempt
from .serializers import CustomUserSerializer


@csrf_exempt
def user(request):
    if request.method not in ['POST']:
        return JsonResponse({'err': 'invalid request method.'}, status=405)

    nu_data = json.loads(request.body)

    # Validations
    try:
        if (not nu_data['first_name'].isalpha()) or (not nu_data['last_name'].isalpha()):
            return JsonResponse({'err': 'Name cannot be alpha numeric'}, status=401)

        if len(nu_data['phone']) != 12 or not nu_data['phone'].isdigit():
            return JsonResponse({'err': 'Invalid phone'}, status=401)

        if not re.fullmatch(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", nu_data['email']):
            return JsonResponse({'err': 'Invalid email'}, status=401)

        if len(nu_data['password']) < 6:
            return JsonResponse({'err': 'invalid password. Expected (< 6)'})

        nu_data['is_email_verified'] = False
        nu_data['is_phone_verified'] = False

    except Exception as e:
        return JsonResponse({'err': "Missing : " + str(e)}, status=401)

    # Validate and save user.
    usr = CustomUser()
    for k, v in nu_data.items():
        if k == 'password':
            usr.set_password(v)
        else:
            setattr(usr, k, v)
    try:
        usr.save()
    except Exception as e:
        return JsonResponse({'err': str(e)})

    return JsonResponse(CustomUserSerializer(usr).data)


@csrf_exempt
@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_id(request: WSGIRequest, id: int):
    edit_data = json.loads(request.body)

    # Validations
    if request.user.id != id:
        return JsonResponse({'err': "Invalid action"})

    try:
        if edit_data['first_name'] or edit_data['last_name']:
            if (not edit_data['first_name'].isalpha()) or (not edit_data['last_name'].isalpha()):
                return JsonResponse({'err': 'Name cannot be alpha numeric'}, status=401)

    except Exception as e:
        pass

    # Validate and save user.
    try:
        usr = CustomUser.objects.get(id=id)
        usr.first_name = edit_data['first_name']
        usr.last_name = edit_data['last_name']
        usr.save()
    except Exception as e:
        return JsonResponse({'err': str(e)})

    return JsonResponse(CustomUserSerializer(usr).data)