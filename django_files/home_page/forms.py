from django import forms
from django.forms import ModelForm, Form


from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from home_page.models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserProfile
        fields = UserCreationForm.Meta.fields + ('user_mobile', 'stars')

class UserProfileForm(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'first_name', 'last_name', 'user_mobile')

class GameForm(Form):
	code = forms.CharField(max_length = 20, required=False)
# from .models import SignUp

# class ContactForm(forms.Form):
# 	full_name = forms.CharField(required=False)
# 	email = forms.EmailField()
# 	message = forms.CharField()


# class SignUpForm(forms.ModelForm):
# 	class Meta:
# 		model = SignUp
# 		fields = ['full_name', 'email']
# 		### exclude = ['full_name']
	
# 	def clean_email(self):
# 		email = self.cleaned_data.get('email')
# 		email_base, provider = email.split("@")
# 		domain, extension = provider.split('.')
# 		# if not domain == 'USC':
# 		# 	raise forms.ValidationError("Please make sure you use your USC email.")
# 		if not extension == "edu":
# 			raise forms.ValidationError("Please use a valid .EDU email address")
# 		return email

# 	def clean_full_name(self):
# 		full_name = self.cleaned_data.get('full_name')
# 		#write validation code.
# 		return full_name