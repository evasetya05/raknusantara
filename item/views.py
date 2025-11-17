from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.urls import reverse
from django.utils import timezone

from urllib.parse import quote

from .models import Item, Category, Comment, DiscussionSchedule
from .forms import (
    NewItemForm,
    EditItemForm,
    CommentForm,
    DiscussionScheduleForm,
)


def browse_items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request=request, template_name='item/items.html', context={
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
    })


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    comments = item.comments.filter(parent__isnull=True).select_related('created_by').prefetch_related('replies__created_by')
    comment_form = CommentForm()
    upcoming_discussions = item.discussion_schedules.filter(scheduled_at__gte=timezone.now()).select_related('created_by').order_by('scheduled_at')

    for schedule in upcoming_discussions:
        detail_url = reverse('item:discussion_schedule_detail', args=[schedule.pk])
        absolute_detail_url = request.build_absolute_uri(detail_url)
        location_text = f" di {schedule.location_name}" if schedule.location_name else ""
        share_message = (
            f"Halo! Yuk gabung diskusi santai '{schedule.title}' untuk buku {item.name} pada "
            f"{schedule.scheduled_at.strftime('%d %B %Y %H:%M')} WIB{location_text}. "
            f"Buka {absolute_detail_url} untuk detailnya. Jika kamu belum punya akun, daftar dulu ya!"
        )
        schedule.detail_url = detail_url
        schedule.absolute_detail_url = absolute_detail_url
        schedule.whatsapp_link = f"https://wa.me/?text={quote(share_message)}"

    return render(request=request, template_name='item/detail.html', context={
        'item': item,
        'related_items': related_items,
        'comments': comments,
        'comment_form': comment_form,
        'upcoming_discussions': upcoming_discussions,
    })


@login_required
def new_item(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)

    else:
        form = NewItemForm()

    return render(request=request, template_name='item/form.html', context={
        'form': form,
        'title': 'New item'
    })


@login_required
def edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)

    else:
        form = EditItemForm(instance=item)

    return render(request=request, template_name='item/form.html', context={
        'form': form,
        'title': 'Edit item'
    })


@login_required
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')


@login_required
def add_comment(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if request.method != 'POST':
        return redirect('item:detail', pk=pk)

    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.item = item
        comment.created_by = request.user
        parent_id = request.POST.get('parent_id')
        if parent_id:
            parent = item.comments.filter(pk=parent_id).first()
            if parent:
                comment.parent = parent
        comment.save()
        messages.success(request, 'Komentar berhasil ditambahkan.')
    else:
        messages.error(request, 'Komentar tidak dapat disimpan. Pastikan semua isian benar.')

    return redirect(f"{reverse('item:detail', args=[pk])}#komentar")


@login_required
def create_discussion_schedule(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if request.method == 'POST':
        form = DiscussionScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.item = item
            schedule.created_by = request.user
            schedule.save()
            messages.success(request, 'Diskusi santai berhasil dijadwalkan.')
            return redirect('item:discussion_schedule_detail', pk=schedule.pk)
    else:
        form = DiscussionScheduleForm()

    return render(request=request, template_name='item/discussion_form.html', context={
        'form': form,
        'item': item,
        'title': 'Jadwalkan Diskusi Santai'
    })


def discussion_schedule_detail(request, pk):
    schedule = get_object_or_404(DiscussionSchedule.objects.select_related('item', 'created_by'), pk=pk)
    schedule_url = request.build_absolute_uri(reverse('item:discussion_schedule_detail', args=[pk]))
    message = (
        f"Hai! Yuk ikut diskusi santai '{schedule.title}' untuk koleksi {schedule.item.name} pada "
        f"{schedule.scheduled_at.strftime('%d %B %Y %H:%M')} WIB. "
        f"Kunjungi {schedule_url} untuk detail. Jika belum memiliki akun, daftar terlebih dahulu ya!"
    )
    whatsapp_link = f"https://wa.me/?text={quote(message)}"

    return render(request=request, template_name='item/discussion_detail.html', context={
        'schedule': schedule,
        'schedule_url': schedule_url,
        'whatsapp_link': whatsapp_link,
    })
