from django import forms
from .models import Item, Comment, DiscussionSchedule


INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image', 'image_secondary', 'image_tertiary',)
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image_secondary': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image_tertiary': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'rows': 3,
                'placeholder': 'Tulis komentar Anda...'
            })
        }


class DiscussionScheduleForm(forms.ModelForm):
    class Meta:
        model = DiscussionSchedule
        fields = ('title', 'agenda', 'scheduled_at', 'location_name', 'location_url',)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Judul diskusi'
            }),
            'agenda': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'rows': 4,
                'placeholder': 'Ringkasan topik atau catatan untuk diskusi'
            }),
            'scheduled_at': forms.DateTimeInput(attrs={
                'class': INPUT_CLASSES,
                'type': 'datetime-local'
            }),
            'location_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Lokasi diskusi (contoh: Ruang baca keluarga)'
            }),
            'location_url': forms.URLInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Tautan peta (Google Maps, dsb) opsional'
            }),
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image', 'image_secondary', 'image_tertiary', 'is_sold',)
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image_secondary': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image_tertiary': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }
