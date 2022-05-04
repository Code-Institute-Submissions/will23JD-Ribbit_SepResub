from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Discussion, Categorys, Comment
from .forms import DiscussionForm, CommentForm


class DiscussionList(generic.ListView):
    model = Discussion
    template_name = 'index.html'
    paginate_by = 12
    ordering = ['-created_on']


class YourDiscussions(generic.ListView):
    model = Discussion
    template_name = 'your_discussions.html'
    paginate_by = 12
    ordering = ['-created_on']


class DiscussionOpen(generic.DetailView):
    model = Discussion
    template_name = 'discussion_open.html'

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Discussion, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['liked'] = liked

        downvote_connected = get_object_or_404(
            Discussion, id=self.kwargs['pk'])
        downVoted = False
        if downvote_connected.down_vote.filter(id=self.request.user.id).exists():
            downVoted = True
        data['downVoted'] = downVoted

        return data


def DiscussionCatsList(request):

    cat_list = Categorys.objects.all()
    return render(request, 'cat_list.html', {'cat_list': cat_list})


def DiscussionCats(request, cats):

    discussion_cat = Discussion.objects.filter(category=cats)
    paginator = Paginator(discussion_cat, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'view_by_cats.html', {'cats': cats, 'discussion_cat': discussion_cat, 'page_obj': page_obj})


def DiscussionLike(request, pk):
    downVote = get_object_or_404(
        Discussion, id=request.POST.get('discussion_id'))
    dislike = get_object_or_404(
        Discussion, id=request.POST.get('discussion_id'))
    if dislike.likes.filter(id=request.user.id).exists():
        dislike.likes.remove(request.user)
    else:
        downVote.down_vote.remove(request.user)
        dislike.likes.add(request.user)

    return HttpResponseRedirect(reverse('disOpen', args=[str(pk)]))


def DiscussionDownVote(request, pk):
    dislike = get_object_or_404(
        Discussion, id=request.POST.get('discussion_id'))
    downVote = get_object_or_404(
        Discussion, id=request.POST.get('discussion_id'))
    if downVote.down_vote.filter(id=request.user.id).exists():
        downVote.down_vote.remove(request.user)
    else:
        dislike.likes.remove(request.user)
        downVote.down_vote.add(request.user)

    return HttpResponseRedirect(reverse('disOpen', args=[str(pk)]))


class AddDiscussion(generic.CreateView):
    model = Discussion
    form_class = DiscussionForm
    template_name = 'add_discussion.html'

    def form_valid(self, form):
        messages.success(self.request, 'New Discussion Created!')
        return super().form_valid(form)
    # fields = ('title', 'slug', 'featured_image', 'excerpt', 'content')


class Comments(generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments.html'

    def form_valid(self, form):
        messages.success(self.request, 'Comment Created Successfully')
        form.instance.Discussion_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):

        return reverse_lazy('disOpen', kwargs={'pk': self.kwargs['pk']})


class Edit(generic.UpdateView):
    model = Discussion
    form_class = DiscussionForm
    template_name = 'edit_discussion.html'

    def get_success_url(self):

        messages.success(self.request, 'Discussion Edited Successfully')
        return reverse_lazy('disOpen', kwargs={'pk': self.kwargs['pk']})


def Delete(request, pk):
    discussion = Discussion.objects.get(pk=pk)
    discussion.delete()
    messages.warning(request, 'Discussion deleted.')
    return redirect('home')


class EditComment(generic.UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'edit_comment.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Comment Edited Successfully')
        self.success_url = self.request.POST.get('previous_page')
        return super().form_valid(form)


def DeleteComment(request, pk):
    comment = Comment.objects.get(pk=pk)
    comment.delete()
    messages.warning(request, 'Comment deleted.')
    return redirect('home')


def page_404(request, exception):
    return render(request, 'page_404.html')
