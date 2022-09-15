from django import forms  
#from django.contrib.auth.models import UserCreationForm
#from django.db import forms
from SignUp.models import SignUp,Adminlog
 
class SignUpForm(forms.ModelForm):  
    class Meta:  
        model = SignUp  
        fields = ('name','username','birthdate','gender','email','phone','password',)

class AdminlogForm(forms.ModelForm):  
    class Meta:  
        model = Adminlog  
        fields = ('username','password',)