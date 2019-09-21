from django.views.generic import (DetailView,
                                  CreateView,
                                  TemplateView,
                                  ListView,
                                  UpdateView
                                  )
from django.core.exceptions import PermissionDenied
from .models import (Album,
                     SongsAlbum,
                     Vote,
                     Comments)
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import (render,
                              redirect,
                              get_object_or_404)
from .forms import (VoteForm)
from .mixins import CachePageVaryOnCookieMixin
from django.core.cache import cache
from django.db.models import Q
import django


#on home page added last added music albums for last week

class HomePage(TemplateView):
    template_name = 'music/home_page.html'
    model = Album

    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,context=self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['image'] = self.model.objects.all()
        return context



class AlbumList(CachePageVaryOnCookieMixin,ListView):
    model = Album
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        search_query = self.request.GET.get('search', '')
        if search_query:
            album = self.model.objects.filter(Q(name_album__icontains=search_query) | Q(genre__icontains=search_query) |
                                              Q(author_album__icontains=search_query))
        else:
            album = self.model.objects.all()
        contact_list = album.order_by('-release_date')
        paginator = Paginator(contact_list, self.paginate_by)
        page = self.request.GET.get('page')
        contacts = paginator.get_page(page)
        context = {'contacts': contacts}
        return render(request, 'music/album_list.html', context)


class TopAlbum(CachePageVaryOnCookieMixin, ListView):
    template_name = 'music/top_album.html'

    def get_queryset(self):
        limit = 10
        key = 'top_albums_%s' % limit
        cached_queryset = cache.get(key)
        if cached_queryset:
            same_django = cached_queryset._django_version == django.get_version()
            if same_django:
                return cached_queryset
        queryset = Album.objects.top_album(limit=limit)
        cache.set(key,queryset)
        return queryset



class Categories(CachePageVaryOnCookieMixin,ListView):
    model = Album
    template_name = 'music/categories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Rap'] = self.model.objects.classification('Rap')
        context['Rock'] = self.model.objects.classification('Rock')
        return context



class SongAlbum(DetailView):
    queryset = Album.objects.all_with_related_persons_and_score()
    template_name = 'music/song.html'
    is_favourite = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['songs'] = SongsAlbum.objects.all()
        context['album_id'] = Album.objects.get(id=self.object.id)
        context['comments'] = Comments.objects.all()
        songs = SongsAlbum.objects.filter(album__name_album=self.object)
        if self.request.user.is_authenticated:
            vote = Vote.objects.get_vote_or_unsaved_blank_vote(album=self.object,user=self.request.user)
            if vote.id:
                vote_form_url = reverse('music:UpdateVote',
                                        kwargs={
                                            'album_id': vote.album.id,
                                            'pk': vote.id
                                        })

            else:
                vote_form_url = reverse('music:CreateVote',
                                        kwargs={
                                            'album_id': self.object.id
                                        })
            for s in songs:
                if s.favourite.filter(id=self.request.user.id).exists():
                    self.is_favourite = True
            vote_form = VoteForm(instance=vote)
            context['vote_form'] = vote_form
            context['vote_form_url'] = vote_form_url
            context['is_favourite'] = self.is_favourite
        return context



class CreateVote(LoginRequiredMixin,CreateView):
    form_class = VoteForm

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user.id
        initial['album'] = self.kwargs['album_id']
        return initial

    def get_success_url(self):
        album_id = self.object.album.id
        return reverse('music:SongAlbum',
                       kwargs={
                           'pk': album_id
                       })

    def render_to_response(self, context, **response_kwargs):
        album_id = context['object'].id
        album_detail_url = reverse('music:SongAlbum',
                                   kwargs={
                                       'pk':album_id
                                   })
        return redirect(to=album_detail_url)



class UpdateVote(LoginRequiredMixin, UpdateView):
    form_class = VoteForm
    queryset = Vote.objects.all()

    def get_object(self, queryset=None):
        vote = super().get_object(queryset)
        user = self.request.user
        if vote.user != user:
            raise PermissionDenied(
                'cannot change another '
                'users vote')
        return vote

    def get_success_url(self):
        album_id = self.object.album.id
        return reverse(
            'music:SongAlbum',
            kwargs={'pk': album_id})

    def render_to_response(self, context, **response_kwargs):
        album_id = context['object'].id
        album_detail_url = reverse(
            'music:SongAlbum',
            kwargs={'pk': album_id})
        return redirect(
            to=album_detail_url)


def favourite(request, pk):
    song = get_object_or_404(SongsAlbum, pk=pk)
    if song.favourite.filter(id=request.user.id).exists():
        song.favourite.remove(request.user)
    else:
        song.favourite.add(request.user)
    return HttpResponseRedirect(song.get_absolute_url())


def favourite_list(request):
    user = request.user
    favourite_songs = user.favourite.all()
    context = {'favourite_songs': favourite_songs}
    return render(request, 'users/favourite.html', context)





