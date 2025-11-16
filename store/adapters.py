from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.exceptions import ImmediateHttpResponse
from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect
from django.utils.text import slugify
from django.contrib.auth.hashers import make_password

User = get_user_model()

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        """
        Automatically log in and connect existing user if email matches.
        """
        email = sociallogin.account.extra_data.get('email')
        if email:
            try:
                existing_user = User.objects.get(email=email)

                # Link the social account
                sociallogin.connect(request, existing_user)

                # Set backend and log the user in
                existing_user.backend = 'allauth.account.auth_backends.AuthenticationBackend'
                login(request, existing_user)

                # 🎉 Add welcome message
                messages.success(request, f"Welcome back, {existing_user.username}!")

                raise ImmediateHttpResponse(redirect('/'))  # Redirect to home
            except User.DoesNotExist:
                pass  # Continue normal signup

    def populate_user(self, request, sociallogin, data):
        """
        Generate unique username from email.
        """
        user = super().populate_user(request, sociallogin, data)
        email = data.get('email')

        if email:
            base_username = slugify(email.split('@')[0])
            new_username = base_username
            counter = 0
            while User.objects.filter(username=new_username).exists():
                counter += 1
                new_username = f"{base_username}{counter}"
            user.username = new_username

        return user
    
    def save_user(self, request, sociallogin, form=None):
        """
        Ensure a hashed password is set during Google signup.
        """
        user = super().save_user(request, sociallogin, form)

        # Set random usable password if user has none
        if not user.has_usable_password():
            from django.utils.crypto import get_random_string
            random_password = get_random_string(12)
            user.password = make_password(random_password)
            user.save()

        return user
