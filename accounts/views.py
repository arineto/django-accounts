from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.base import RedirectView

from braces.views import LoginRequiredMixin

from accounts.mixins import SuccessMixin
from accounts.forms import RegisterUserForm
from accounts.forms import UpdateUserForm


class RegisterUserView(SuccessMixin, CreateView):

    model = User
    form_class = RegisterUserForm
    success_message = 'User created with success!'
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/register_user.html'


register_user = RegisterUserView.as_view()


class UpdateUserView(LoginRequiredMixin, SuccessMixin, UpdateView):

    model = User
    form_class = UpdateUserForm
    success_message = 'Profile updated with success!'
    success_url = getattr(settings, 'LOGIN_REDIRECT_URL', None)
    template_name = 'accounts/update_user.html'


update_user = UpdateUserView.as_view()


class PasswordChangeDone(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        messages.success(self.request, "Password changed with success!")
        return reverse_lazy(getattr(settings, 'LOGIN_REDIRECT_URL', None))


password_change_done = PasswordChangeDone.as_view()
