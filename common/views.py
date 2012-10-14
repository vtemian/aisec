from django.template.context import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from discussion.views import SearchFormMixin
from django.contrib.auth.decorators import login_required

class ProtectedView(TemplateView):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProtectedView, self).dispatch(*args, **kwargs)

    def render_to_response(self, context, **kwargs):
        return super(ProtectedView, self).render_to_response(
            RequestContext(self.request,
                context),
            **kwargs)

class HomeView(SearchFormMixin, ProtectedView):
    template_name = 'index.html'
