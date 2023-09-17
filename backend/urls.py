from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views

from django.conf import settings

from .views import check_login_ajax, api_login, register
from backoffice import views as bbk

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('_nested_admin/', include('nested_admin.urls')),

    #####################
    #### AUTH & MAIN ####
    #####################
    
    path('check_login/', check_login_ajax),
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name="admin/login.html"), name='login'),
    path('account/logout/', auth_views.logout_then_login, name='logout'),
    path('lbb-api-token-auth/', api_login),

    # --------------------
    # REGISTER USER
    # --------------------

    path('register/', register, name='register'),

    ### Redirection to home backoffice ###
    path('', bbk.index, name='home'),
    #### call backoffice ####
    path('get_user_profile/', bbk.ProfileView.as_view(), name='get_user_profile'),

    ### import url to app ###

    path('app_log/', include('app.urls'))

]
# if settings.DEBUG:
#     from django.views import static

#     urlpatterns += (
#         re_path(r'^site_media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT}),
#     )
