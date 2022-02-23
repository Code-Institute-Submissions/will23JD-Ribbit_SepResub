from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from .models import discussion
from .forms import DiscussionForm


class DiscussionList(generic.ListView):
    model = discussion
    template_name = 'index.html'
    paginate_by = 9


class DiscussionOpen(generic.DetailView):
    model = discussion
    template_name = 'discussion_open.html'


class AddDiscussion(generic.CreateView):
    model = discussion
    form_class = DiscussionForm
    template_name = 'add_discussion.html'
    # fields = ('title', 'slug', 'author', 'featured_image', 'excerpt', 'content')
