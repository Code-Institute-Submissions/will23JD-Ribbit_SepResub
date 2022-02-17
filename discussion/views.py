from django.shortcuts import render
from django.views import generic
from .models import discussion

class DiscussionList(generic.ListView):
    model = discussion
    template_name = 'index.html'
    paginate_by = 9


class DiscussionOpen(generic.DetailView):
    model = discussion
    template_name = 'discussion_open.html'
