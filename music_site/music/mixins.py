from .models import Album
from django.core.paginator import Paginator
from django.core.cache import caches
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie


class CachePageVaryOnCookieMixin:
    cache_name = 'default'

    @classmethod
    def get_timeout(cls):
        if hasattr(cls,'timeout'):
            return cls.timeout
        cache = caches[cls.cache_name]
        return cache.default_timeout

    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super().as_view(*args,**kwargs)
        view = vary_on_cookie(view)
        view = cache_page(timeout=cls.get_timeout(),
                          cache=cls.cache_name)(view)
        return view

    def pagination(self,pages,*args,**kwargs):
        contact_list = Album.objects.order_by('-release_date')
        paginator = Paginator(contact_list,pages)
        page = self.request.GET.get('page')
        contacts = paginator.get_page(page)
        return contacts


