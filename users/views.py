
# Create your views here.

import json, re

from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError

from .models       import Signup

def email_check(email): 
    return bool(re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',email))
def password_check(pw): 
    return bool(re.match('.{8,45}', pw))

class UsersView(View):
    def post(self, request): 

        try:
            data  = json.loads(request.body)
            email = data['email']
            password    = data['password']
            
            if email and password:
                if Signup.objects.filter(email=email).exists():
                    return JsonResponse({'MESSAGE': 'EMAIL_ALREADY_EXISTS'}, status=400)

                if Signup.objects.filter(password=password).exists():
                    return JsonResponse({'MESSAGE': 'PASSWORD_ALREADY_EXISTS'}, status=400)

                # if '@' not in email or '.' not in email:
                #     return JsonResponse({'MESSAGE' : 'INVALID_EMAIL'},status=400)
                # if len(password) < 8: 
                #     return JsonResponse({'MESSAGE' : 'INVALID_PASSWORD'},status=400)
                if not email_check(email):
                    return JsonResponse({'MESSAGE' : 'INVALID_EMAIL'},status=400)

                if not password_check(password):
                    return JsonResponse({'MESSAGE' : 'INVALID_PASSWORD'},status=400)
                    
                signup = Signup.objects.create(
                    email    = email,
                    password = password
                )
            return JsonResponse({'message': 'SUCCESS'}, status=200)
        
        except KeyError:
            return JsonResponse({'MESSAGE': 'KEY_ERROR'}, status=400)
         

class LoginsView(View):  
    def post(self, request):

        try: 
            data        = json.loads(request.body)
            email       = data['email']
            password    = data['password']
            
            if email and password: 

                if not Signup.objects.filter(email=email).exists():
                    return JsonResponse({'MESSAGE':'INVALID_USER'},status=401)

                if not Signup.objects.filter(password=password).exists():
                    return JsonResponse({'MESSAGE':'INVALID_USER'},status=401)

                return JsonResponse({"MESSAGE":"SUCCESS"},status=200)
        
        except KeyError:
            return JsonResponse({'MESSAGE': 'KEY_ERROR'}, status=400)

    



