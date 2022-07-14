from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView
from .models import Challenge
from .forms import ChallengeForm, ChallengeUpdateForm
from django.shortcuts import render


def ChallengeIndex(request):
    """ Stand list view. """
    template_name = 'challenges-fbv/index.html'
    context = {
        'challenges_context': Challenge.objects.all(),
        'challenge_distinct': Challenge.objects.values('challenge').distinct()
    }

    challenge = Challenge.objects.values('challenge').distinct()

    # print(challenge)

    return render(request, template_name, context)


def add_challenge(request):
    """ Create a challenge. """
    template = 'challenges-fbv/add.html'

    if request.method == "POST":
        form = ChallengeForm(request.POST)
        if form.is_valid():

            if 1 == 1:
                # commit=False  > we don't want to save this yet.
                post = form.save(commit=False)
                post.start_date = form.cleaned_data['start_date']
                post.author = request.user
                post.save()
                # console
                print(post.id, post.start_date, post.status, post.author)
                return redirect('challenges-index')
            else:
                print('error')

    else:
        form = ChallengeForm()

    context = {
        'challenges_context': Challenge.objects.all(),
        'form': form
    }

    return render(request, template, context)


def ChallengeUpdate(request, pk):
    """ Update a challenge. """
    # challenge_obj = get_object_or_404(Challenge, pk=pk)
    template = 'challenges-fbv/update.html'
    context = {
        'challenge_obj': get_object_or_404(Challenge, pk=pk)
    }
    return render(request, template, context)


class ChallengesListView(ListView):
    """Challenges ListView."""
    context_object_name = 'challenge_list'
    model = Challenge
    paginate_by = 10
    template_name = 'challenges/index.html'

    # test

    def get_queryset(self):
        return Challenge.objects.all().filter(author=self.request.user).order_by('-start_date')

    def get_context_data(self, *args, **kwargs):
        context = super(ChallengesListView, self).get_context_data(*args, **kwargs)
        context['challenge_list_chart'] = Challenge.objects.all().filter(author=self.request.user).order_by(
            'start_date')
        return context


class ChallengesCreateView(CreateView):
    """Create challenge."""
    model = Challenge
    template_name = 'challenges/add.html'
    fields = ('start_date', 'challenge')

    def get_context_data(self, *args, **kwargs):
        context = super(ChallengesCreateView, self).get_context_data(*args, **kwargs)
        return context


class ChallengeUpdateView(UpdateView):
    model = Challenge
    form_class = ChallengeUpdateForm
    template_name = 'challenges/update.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
