
# Create your views here.

import json, bcrypt, jwt, re

from django.http        import JsonResponse, HttpResponse
from django.views       import View

from products.models    import Signup


class ProductsView(View) : 
def   post(self, request): 
        data  = json.loads(request.body)
        email = data['']

        def email_check(email): 
            return bool(re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email))

        def password_check(pw):
            return bool(re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', pw))

        if email = '' or password = '':
            return JsonResponse({'MESSAGE': 'KEY_ERROR'}, status=400)

        elif email_check(email) and password_check(pw): 
            signup = Signup.objects.create(
                email    = data['email'],
                password = data['password']
            )
                
                

            return JsonResponse({'MESSAGE': 'SUCCESS'}, status=201)    
         
