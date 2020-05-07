from datetime import datetime
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from web.models import Publication
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, PublicationForm, CommentForm


def index(request):
    num_pubs = Publication.objects.all().count()
    num_users = User.objects.all().count()
    return render(
        request,
        'index.html',
        context={'num_pubs': num_pubs, 'num_users': num_users},
    )


def publications(request):
    all_pubs = Publication.objects.order_by('-publication_date')
    return render(
        request,
        'publications.html',
        context={'all_pubs': all_pubs},
    )


def publication(request, publication_id):
    try:
        pub_a = Publication.objects.get(id=publication_id)
    except:
        raise Http404('Publication Not Found')
    form = CommentForm()
    comments = pub_a.comment_set.order_by('-comment_date')
    return render(
        request,
        'publication.html',
        context={'publication': pub_a, 'comments': comments, 'form':form},
    )


def user(request, user_id):
    try:
        user_a = User.objects.get(id=user_id)
    except:
        raise Http404('User Not Found')

    list_user_pubs = user_a.publication_set.order_by('-publication_date')

    return render(
        request,
        'user.html',
        context={'user': user_a, 'list_user_pubs': list_user_pubs},
    )


def users(request):
    all_users = User.objects.all()
    return render(
        request,
        'users.html',
        context={'all_users': all_users},
    )


def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successful')
            return redirect('web:register')

    else:
        f = CustomUserCreationForm()
        return render(
            request,
            'register.html',
            context={'form': f},
        )


def new_publication(request):
    if request.method == 'POST':
        new_pub = PublicationForm(request.POST)
        if new_pub.is_valid():
            post = new_pub.save(commit=False)
            post.user = request.user
            post.publication_date = datetime.now()
            post.save()
            return redirect('web:publication', post.id)

    else:
        new_pub = PublicationForm()
        return render(
            request,
            'new_publication.html',
            context={'new_pub': new_pub}
        )


def add_comment(request, publication_id):
    pub_id = get_object_or_404(Publication, id=publication_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comm = form.save(commit=False)
            new_comm.user = request.user
            new_comm.publication = pub_id
            new_comm.comment_date = datetime.now()
            new_comm.save()
            return redirect('web:publication', publication_id)

    else:
        form = CommentForm()
        return render(
            request,
            'publication/add_comment.html',
            context={'form': form}
        )
