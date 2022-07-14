from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import EmailField
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic


class CustomUserForm(UserCreationForm):
    email = EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SignUpView(generic.CreateView):
    """ Sign up view. """
    # form_class = UserCreationForm
    form_class = CustomUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        self.object = form.save()
        # user = User.objects.get(id=self.object.pk)
        return redirect('login')
