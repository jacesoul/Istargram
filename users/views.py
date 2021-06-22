import json, re, bcrypt, jwt

from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError

from .models       import Signup
from my_settings import SECRET_KEY


def email_check(email): 
    return bool(re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',email))

def password_check(password): 
    return bool(re.match('.{8,45}', password))

def create_bcrypt(password): # encode('utf-8')의 의미는 무엇인지?
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password

def bcrypt_check(password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return bcrypt.checkpw(password.encode('utf-8'),hashed_password)

def create_jwt(hashed_password, num):
    # 처음에는 SECRET을 hashed_password로 지정했지만 이 값은 고유하기 때문에 mysettings에 있는 SECRET_KEY로 해도 무방하다. 
    SECRET = SECRET_KEY
    access_token = jwt.encode({'id':num}, SECRET, algorithm = 'HS256')
    return access_token

def jwt_check(access_token):
    header = jwt.decode(access_token, SECRET, algorithms = 'HS256')
    user_id = header['id']
    return user_id



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
                
                hashed_password = create_bcrypt(password)
                # binary로 비밀번호를 설정해주면 나중에 프런트에서 받을때 binary화된 pw를 다시 스트링화로 하기 때문에 처음부터 decode를 해주는것이 좋다. 
                decoded_password = hashed_password.decode('utf-8')
                signup = Signup.objects.create(
                    email    = email,
                    password = decoded_password
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
                    return JsonResponse({'MESSAGE':'INVALID_USER_EMAIL_INCORRECT'},status=401)

                # if not Signup.objects.filter(password).exists():
                #     return JsonResponse({'MESSAGE':'INVALID_USER_PASSWORD_INCORRECT'},status=401)
            
                if not bcrypt_check(password):
                    return JsonResponse({'MESSAGE':'INVALID_USER_PASSWORD_INCORRECT'},status=401)
                id_num = Signup.objects.get(email=email).id
                access_token = create_jwt(password,id_num)

                return JsonResponse({"ACCESS_TOKEN":access_token},status=200)
        
        except KeyError:
            return JsonResponse({'MESSAGE': 'KEY_ERROR'}, status=400)
