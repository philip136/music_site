from django.views.generic import (DetailView,
                                  CreateView,
                                  TemplateView,
                                  ListView,
                                  UpdateView)
from django.core.exceptions import PermissionDenied
from .models import (Album,
                     SongsAlbum,
                     Vote)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import (render,
                              redirect)
from .forms import VoteForm
from .mixins import CachePageVaryOnCookieMixin
from django.core.cache import cache
import django





class HomePage(TemplateView):
    template_name = 'music/base.html'


class AlbumList(CachePageVaryOnCookieMixin,ListView):
    model = Album
    paginate_by = 3

    def get(self, request, *args, **kwargs):
        mixin_data = super(AlbumList, self)
        pagination = mixin_data.pagination(self.paginate_by)
        context = {'contacts': pagination}
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


class SongAlbum(DetailView):
    queryset = Album.objects.all_with_related_persons_and_score()
    template_name = 'music/song.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['songs'] = SongsAlbum.objects.all()
        context['images'] = Album.objects.get(id=self.object.id)
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
            vote_form = VoteForm(instance=vote)
            context['vote_form'] = vote_form
            context['vote_form_url'] = vote_form_url
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






