from django.conf.urls import url

from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib.auth.views import password_reset
from django.contrib.auth.views import password_change
from django.contrib.auth.views import password_reset_done
from django.contrib.auth.views import password_change_done
from django.contrib.auth.views import password_reset_confirm
from django.contrib.auth.views import password_reset_complete

from accounts.views import register_user
from accounts.views import update_user


urlpatterns = [
    url(
        r'login/$', login,
        {
            'template_name': 'accounts/login.html'
        },
        name='login'
    ),

    url(
        r'logout/$', logout,
        {
            'next_page': 'accounts:login'
        },
        name='logout'
    ),

    url(
        r'password_reset/$', password_reset,
        {
            'template_name': 'accounts/password_reset.html',
            'email_template_name': 'accounts/password_reset_email.html',
            'post_reset_redirect': 'accounts:password_reset_done'
        },
        name="password_reset"
    ),

    url(
        r'password_reset_done/$', password_reset_done,
        {
            'template_name': 'accounts/password_reset_done.html'
        },
        name='password_reset_done'
    ),

    url(
        r'password_reset/(?P<uidb64>[0-9A-Za-z_\-]+)/\
            (?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm,
        {
            'post_reset_redirect': 'accounts:password_reset_complete',
            'template_name': 'accounts/password_reset_confirm.html'
        },
        name='password_reset_confirm'
    ),

    url(
        r'^password_done/$', password_reset_complete,
        {
            'template_name': 'accounts/password_reset_complete.html'
        },
        name='password_reset_complete'
    ),

    url(r'register_user/$', register_user, name='register_user'),

    url(r'update_profile/(?P<pk>[\d]+)/$', update_user, name='update_user'),

    url(
        r'change_password/$', password_change,
        {
            'template_name': 'accounts/password_change.html',
            'post_change_redirect': 'accounts:change_password_done'
        },
        name='change_password'
    ),

    url(
        r'change_password_done/$', password_change_done,
        name='change_password_done'
    ),
]
