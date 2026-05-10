from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from urllib.parse import quote
from .models import Perpustakaan
from .forms import PerpustakaanForm

def perpustakaan_list_public(request):
    """Public view showing list of all perpustakaan"""
    perpustakaans = Perpustakaan.objects.all().order_by('-created_at') if hasattr(Perpustakaan, 'created_at') else Perpustakaan.objects.all().order_by('-id')
    
    return render(request, 'perpustakaan/public_list.html', {
        'perpustakaans': perpustakaans,
    })

def perpustakaan_public_detail(request, pk):
    """Public view showing perpustakaan detail with all books"""
    perpustakaan = get_object_or_404(Perpustakaan, pk=pk)
    
    return render(request, 'perpustakaan/public_detail.html', {
        'perpustakaan': perpustakaan,
    })

@login_required
def perpustakaan_list(request):
    # If user is not logged in, show message to login
    if not request.user.is_authenticated:
        return render(request, 'perpustakaan/public_required.html', {
            'message': 'Silakan login untuk melihat detail perpustakaan.'
        })
    
    # Get or create Perpustakaan for the current user
    perpustakaan, created = Perpustakaan.objects.get_or_create(
        user=request.user,
        defaults={'name': f'Perpustakaan {request.user.username}'}
    )
    
    # Generate share links
    perpustakaan_url = request.build_absolute_uri(reverse('perpustakaan:list'))
    
    # WhatsApp share
    whatsapp_text = f"Lihat koleksi buku di {perpustakaan.name} - {perpustakaan_url}"
    whatsapp_link = f"https://wa.me/?text={quote(whatsapp_text)}"
    
    # Facebook share
    facebook_link = f"https://www.facebook.com/sharer/sharer.php?u={quote(perpustakaan_url)}"
    
    # Twitter share
    twitter_text = f"Kunjungi {perpustakaan.name} - koleksi buku menarik di Rak Nusantara"
    twitter_link = f"https://twitter.com/intent/tweet?text={quote(twitter_text)}&url={quote(perpustakaan_url)}"
    
    return render(request, 'perpustakaan/detail.html', {
        'perpustakaan': perpustakaan,
        'whatsapp_link': whatsapp_link,
        'facebook_link': facebook_link,
        'twitter_link': twitter_link,
        'total_books': perpustakaan.items.count(),
        'available_books': perpustakaan.items.filter(is_sold=False).count(),
    })

@login_required
def edit_perpustakaan(request):
    perpustakaan, created = Perpustakaan.objects.get_or_create(
        user=request.user,
        defaults={'name': f'Perpustakaan {request.user.username}'}
    )
    
    if request.method == 'POST':
        form = PerpustakaanForm(request.POST, instance=perpustakaan)
        if form.is_valid():
            # Handle social media data
            social_media = {}
            social_fields = ['instagram', 'facebook', 'twitter', 'youtube']
            for field in social_fields:
                field_name = f'social_media_{field}'
                if field_name in request.POST and request.POST[field_name].strip():
                    social_media[field] = request.POST[field_name].strip()
            
            # Save form first
            perpustakaan = form.save(commit=False)
            # Update social media
            perpustakaan.social_media = social_media if social_media else None
            perpustakaan.save()
            
            messages.success(request, 'Informasi perpustakaan berhasil diperbarui!')
            return redirect('perpustakaan:list')
    else:
        form = PerpustakaanForm(instance=perpustakaan)
    
    return render(request, 'perpustakaan/edit.html', {'form': form, 'perpustakaan': perpustakaan})
