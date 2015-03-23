from django.shortcuts import redirect

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from centers.models.center import Center
from reviews.models import Review

from reviews.forms import ReviewForm

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods


class CenterList(ListView):
    template_name = 'centers/list.html'
    context_object_name = 'centers'

    def get_queryset(self):
        search_query = self.request.GET.get('search') or str()
        return Center.objects.filter(name__contains=search_query)


class CenterDetail(DetailView):
    model = Center
    template_name = 'centers/detail.html'
    context_object_name = 'center'
    slug_field = 'hash_id'

    def get_context_data(self, **kwargs):
        context = super(CenterDetail, self).get_context_data(**kwargs)
        context['review_form'] = ReviewForm()
        return context


@login_required
@require_http_methods(["POST"])
def reviews(request, slug):
    user = request.user
    center = Center.objects.get(hash_id=slug)

    review = Review.objects.create(
        user=user,
        center=center,
        content=request.POST['content'],
    )

    return redirect("centers:detail", slug=slug)
