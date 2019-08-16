from .models import List
from .forms import ListForm
from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView, DetailView


# Class based view for home page
class Home(ListView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return List.objects.all()
        
    def post(self, *args, **kwargs):
        request = self.request
        print(request.POST)
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item has been added')
        return redirect('/')


# Class based view for about section
class About(ListView):
    template_name = 'about.html'

    def get_context_data(self, *args, **kwargs):
        context = super(About, self).get_context_data(*args, **kwargs)
        return context


# Class based view for deleting an item in the list
class Delete(DeleteView):

    def delete(self, request, *args, **kwargs):
        print(request.POST)
        id = request.POST.get('id')
        try:
            qs = List.objects.get(id=id)
            print(qs)
            qs.delete()
            messages.success(request, 'Item deleted successfully')
            return redirect('/')
        except:
            messages.error(request, 'Deletion failed')

        return redirect('/')



class Cross(ListView):

    def post(self, request, *args, **kwargs):
        id = request.POST.get('id')
        try:
            item = List.objects.get(id=id)
            item.completed = True
            item.save()
            messages.success(request, 'Status changed successfully')
            return redirect('/')
        except:
            messages.error(request, 'Internal server error')

        return redirect('/')

class Uncross(ListView):

    def post(self, request, *args, **kwargs):
        id = request.POST.get('id')
        try:
            item = List.objects.get(id=id)
            item.completed = False
            item.save()
            messages.success(request, 'Status changed successfully')
            return redirect('/')
        except:
            messages.error(request, 'Internal server error')

        return redirect('/')


def edit(request, list_id):
    id = list_id
    if request.method == "POST":
        item = List.objects.get(pk=id)
        form = ListForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item Edited')
            return redirect('/')

    else:
        items = List.objects.get(id=id)
        return render(request, 'snippets/edit.html', {"item": items})
        

