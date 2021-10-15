from django import forms

class FormularioRegistro(forms.Form):
    email = forms.EmailField(max_length=30, label='Correo')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput())
    usuario = forms.CharField(max_length=16, label='Usuario')

class FormularioCambioCLave(forms.Form):
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput())