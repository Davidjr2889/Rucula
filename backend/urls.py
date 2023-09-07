from django.contrib import admin
from django.urls import path, include
from backoffice import views as bbk

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('_nested_admin/', include('nested_admin.urls')),

    ### Redirection to home backoffice ###
    path('', bbk.index, name='home'),
    #### call backoffice ####
    path('get_user_profile/', bbk.ProfileView.as_view(), name='get_user_profile'),

    ### import url to app ###

    path('app_log/', include('app.urls'))

]
