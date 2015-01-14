from django.views.generic.base import TemplateView


class PageView(TemplateView):
    template_name = 'page.html'

    @classmethod
    def as_view(self, repository):
        self.repository = repository
        return super(PageView, self).as_view()

    def get_context_data(self, **kwargs):
        page = self.repository.get(kwargs['page'])
        return {'body': page}
