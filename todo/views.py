from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from todo.models import Task, Tag
from todo.forms import TaskForm, TagForm


# --- TASKS ---
class TaskListView(generic.ListView):
    model = Task
    template_name = "todo/index.html"
    context_object_name = "tasks"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo/task_confirm_delete.html"
    success_url = reverse_lazy("todo:index")

class TaskToggleStatusView(generic.View):
    def get(self, request, *args, **kwargs):
        # Get id from URL-paramiters (kwargs)
        task = get_object_or_404(Task, pk=self.kwargs['pk'])
        # Change the status to the opposite one
        task.is_done = not task.is_done
        task.save()
        return redirect('todo:index')

# --- TAGS ---
class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"
    context_object_name = "tags"


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo/tag_confirm_delete.html"
    success_url = reverse_lazy("todo:tag-list")
