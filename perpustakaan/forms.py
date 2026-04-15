from django import forms
from .models import Perpustakaan

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class PerpustakaanForm(forms.ModelForm):
    class Meta:
        model = Perpustakaan
        fields = ('name', 'alamat', 'email', 'layanan', 'social_media')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Nama perpustakaan Anda'
            }),
            'alamat': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'rows': 4,
                'placeholder': 'Alamat lengkap perpustakaan'
            }),
            'email': forms.EmailInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Email perpustakaan'
            }),
            'layanan': forms.CheckboxSelectMultiple(choices=Perpustakaan.LAYANAN_CHOICES)
        }
