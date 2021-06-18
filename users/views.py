
# Create your views here.

import json, re

from django.http        import JsonResponse
from django.views       import View

from users.models       import Signup


class UsersView(View):

    def post(self, request): 

        data  = json.loads(request.body)
        p = re.compile( '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$' )

        email = data['email']
        password    = data['password']

        
        
        def email_check(email): 
            return bool(re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',email))

        def password_check(pw): 
            return bool(re.match('.{8,45}', pw))

        if email == '' or password == '':
            return JsonResponse({'MESSAGE': 'KEY_ERROR'}, status=400)

        elif email_check(email) and password_check(password): 
            signup = Signup.objects.create(
                email    = email,
                password = password
            )
                
        
            return JsonResponse({'MESSAGE': 'SUCCESS'}, status=201)    
         
