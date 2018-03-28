from django.conf.urls import url
from django.contrib.auth.views import (login,
                                       logout,
                                       password_reset,
                                       password_reset_done,
                                       password_reset_confirm,
                                       password_reset_complete,
                                       )
from .views import home, register, profile, edit, passe_change

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^register/$', register, name="register"),
    url(r'^login/$', login, {'template_name': 'comptes/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'comptes/logout.html'}, name='logout'),
    url(r'^profile/$', profile, name="profile"),
    url(r'^profile/edit/$', edit, name="edit"),
    url(r'^passe_change/$', passe_change, name="passe_change"),
    url(r'^password-reset/$', password_reset, {'template_name': 'comptes/reset_password.html', 'post_reset_redirect':'comptes:password_reset_done', 'email_template_name':'comptes/reset_passe_email.html'}, name="password_reset"),
    url(r'^password-reset/done/$', password_reset_done, {'template_name': 'comptes/password_reset_done.html'}, name="password_reset_done"),
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,{'template_name': 'comptes/reset_password_confirm.html', 'post_reset_redirect':'comptes:password_reset_complete'},  name="password_reset_confirm"),
    url(r'^password-reset/complete/$',password_reset_complete,{'template_name': 'comptes/reset_password_complete.html'}, name="password_reset_complete"),
]