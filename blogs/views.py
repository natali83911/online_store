from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from django.utils import timezone

class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blogs/blog_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return BlogPost.objects.filter(status='published', published_at__lte=timezone.now())

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blogs/blog_detail.html'
    context_object_name = 'blogs'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save(update_fields=['views_count'])
        return obj

class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'content', 'preview', 'status']
    template_name = 'blogs/blog_form.html'
    success_url = reverse_lazy('blogs:blog_list')

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'preview', 'status']
    template_name = 'blogs/blog_form.html'

    def get_success_url(self):
        return reverse('blogs:blog_detail', kwargs={'pk': self.object.pk})

class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blogs/blog_confirm_delete.html'
    success_url = reverse_lazy('blogs:blog_list')
