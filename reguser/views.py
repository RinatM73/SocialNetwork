from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView, UpdateView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.contrib.auth.views import LoginView

# Create your views here.

class UserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'accounts/reg.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.username = form.cleaned_data['username']
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        if 'image_profile' in self.request.FILES:
            user.image_profile = self.request.FILES['image_profile']
        user.save()
        login(self.request, user)
        return super().form_valid(form)

class UserLogin(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    # success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect('home')



class ProfileView(TemplateView):
    template_name = 'profile.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class ProfileUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'sign/profile_update.html'
    success_url = reverse_lazy('profile')
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

