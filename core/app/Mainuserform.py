from django import forms
from  .models import Mainuser

class Salim(forms.ModelForm):
    name=forms.CharField(label="Username",widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    phone=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
   
   

    class Meta:
        model=Mainuser
        fields=['name','email','phone','address','images']

class loginf(forms.ModelForm):
    name=forms.CharField(label="Username",widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Mainuser
        fields = ['name', 'email']
