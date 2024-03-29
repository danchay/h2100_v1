from django import forms 

class ContactForm(forms.Form):
	full_name = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'  Your full name'}), required=True)
	email = forms.EmailField( widget=forms.TextInput(attrs={'placeholder':'  Your email'}), required=True)
	message = forms.CharField( widget=forms.Textarea(attrs={'cols':40, 'rows': 10, 'placeholder': '  Your message'}))



# from .models import SignUp

# class SignUpForm(forms.ModelForm):
# 	class Meta:
# 		model = SignUp
# 		fields = ['full_name', 'email'] 

# 	# Validate with clean_fieldname, which is an override of function for cleaning that data

# 	# def clean_email(self):
# 	# 	email = self.cleaned_data.get('email')
# 	# 	email_base, provider = email.split("@")
# 	# 	domain, extension = provider.split('.')
# 	# 	if not extension == "edu":
# 	# 		raise forms.ValidationError("Please use a valid .edu email address")
# 	# 	return email

# 	# def clean_full_name(self):
# 	# 	full_name = self.cleaned_data.get('full_name')
# 	# 	# Write validation code
# 	# 	return full_name