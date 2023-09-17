import json
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response

from dascat_utils.django.user_utils import get_client_ip

from rest_framework_jwt.views import obtain_jwt_token

from backoffice.models import LoginLog
from backoffice.models import InvalidLoginLog

# ------------------
# LOGIN
# ------------------

User = get_user_model()

@csrf_exempt
@never_cache
def check_login_ajax(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            return JsonResponse({"success": True})
        else:
            request.session.set_test_cookie()
            return JsonResponse({"success":False, "reason": "Dados Invalidos"})
    else:
        return HttpResponseNotAllowed(("POST",))
    
@csrf_exempt
@never_cache
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = request.data['username']
        password = request.data['password']
        email = request.get['email','']
        user = User.objects.create_user(username=username, email=email, password=password)
        return JsonResponse({'detail': 'user created successfull'})
    return JsonResponse({"message": "GET method not supported"}, status=405)  # Return a message for unsupported GET request.

    

@csrf_exempt
@never_cache
def api_login(request):

    response = obtain_jwt_token(request)
    st = response.status_code
    if st == 200:
        user = auth.authenticate(request=request)   
        if user is not None:
            auth.login(request, user)
            LoginLog.objects.create(
                user=request.user, 
                login_ip=get_client_ip(request))
    else:
        try:
                
            request_body_str = request.body.decode('utf-8')
            request_json = json.loads(request_body_str)
            print(request_json)
        except json.JSONDecodeError:
            return JsonResponse({"error":"Invalid JSON payload"})
        InvalidLoginLog.objects.create(
            username= request_json(User.USERNAME_FIELD),
            login_ip=get_client_ip(request)
            
        )
        
    return response