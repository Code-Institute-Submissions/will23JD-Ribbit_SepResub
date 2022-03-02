from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from .models import discussion, Categorys, Comment
from .forms import DiscussionForm, CommentForm


class DiscussionList(generic.ListView):
    model = discussion
    template_name = 'index.html'
    paginate_by = 9
    ordering = ['-created_on']

    
class DiscussionOpen(generic.DetailView):
    model = discussion
    template_name = 'discussion_open.html'

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(discussion, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['liked'] = liked

        return data


def DiscussionCatsList(request):

    cat_list = Categorys.objects.all()
    return render(request, 'cat_list.html', {'cat_list': cat_list})


def DiscussionCats(request, cats):

    discussion_cat = discussion.objects.filter(categorys=cats)
    paginator = Paginator(discussion_cat, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'view_by_cats.html', {'cats': cats, 
    'discussion_cat': discussion_cat, 'page_obj': page_obj})


def DiscussionLike(request, pk):
    dislike = get_object_or_404(discussion, id=request.POST.get('discussion_id'))
    liked = False
    if dislike.likes.filter(id=request.user.id).exists():
        dislike.likes.remove(request.user)
        liked = False
    else:
        dislike.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('disOpen', args=[str(pk)]))

class AddDiscussion(generic.CreateView):
    model = discussion
    form_class = DiscussionForm
    template_name = 'add_discussion.html'
    # fields = ('title', 'slug', 'author', 'featured_image', 'excerpt', 'content')


class Comments(generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments.html'
    
    def form_valid(self, form):
        form.instance.discussion_id = self.kwargs['pk']
        return super().form_valid(form)
    
    def get_success_url(self):

        return reverse_lazy('disOpen', kwargs={'pk': self.kwargs['pk']})


class Edit(generic.UpdateView):
    model = discussion
    form_class = DiscussionForm
    template_name = 'edit_discussion.html'

    def get_success_url(self):

        return reverse_lazy('disOpen', kwargs={'pk': self.kwargs['pk']})


class Delete(generic.DeleteView):
    model = discussion
    template_name = "delete_discussion.html"
    success_url = reverse_lazy('home')


class EditComment(generic.UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'edit_comment.html'
    success_url = reverse_lazy('home')


class DeleteComment(generic.DeleteView):
    model = Comment
    template_name = "delete_comment.html"
    success_url = reverse_lazy('home')
