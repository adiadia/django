from django.shortcuts import render,get_object_or_404,Http404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q
from .forms import PostModalForm,SearchForm
from .models import PostModel
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.core.exceptions import MultipleObjectsReturned


def post_create(request):
    form=PostModalForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        obj=form.save(commit=False)
        obj.save()
        messages.success(request,'Form created Successfull')
        context = {'form': PostModalForm(request.POST or None)}
    template = 'blog/create-view.html'
    return render(request, template, context)


def searchform(request):
    form=SearchForm(request.POST or None)
    if(form.is_valid()):
        print(request.POST)
    context={'form' : form}
    template_name='blog/form1.html'
    return render(request, template_name, context)


class LoginRequired(object):
    # @classmethod
    # def as_view(cls,**kwargs):
    #     view=super(LoginRequired,cls).as_view(**kwargs)
    #     return login_required(view)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequired,self).dispatch(request,*args,**kwargs)


class MultipleObjectMix(object):
    def get_object(self, queryset=None, *args, **kwargs):
        slug=self.kwargs.get('slug')
        if slug:
            try:
                obj=self.model.objects.get(slug=slug)
            except self.model.MultipleObjectsReturned:
                obj=self.get_queryset().first()
            except:
                obj=Http404
            return obj
        return Http404

class PostDelete(DeleteView):
    model = PostModel
    template_name = 'blog/delete-view.html'
    def get_success_url(self):
        return reverse('list')



class PostUpdate(UpdateView):
    model = PostModel
    template_name = 'blog/create-view.html'
    fields = ['title', 'content']



class PostCreate(CreateView):
    model = PostModel
    template_name = 'blog/create-view.html'
    fields = ['title','content']
    success_url = '/'

class PostList(ListView):
    model = PostModel

class PostDetail(DetailView):
    model = PostModel

    def get_object(self, queryset=None, *args, **kwargs):
        slug=self.kwargs.get('slug')
        if slug:
            try:
                obj=self.model.objects.get(slug=slug)
            except self.model.MultipleObjectsReturned:
                obj=self.get_queryset().first()
            except:
                obj=None
            return obj
        return None


class DashboardTemplateView(LoginRequired,TemplateView):
    template_name = 'blog/about.html'

    def dispatch(self, request, *args, **kwargs):
        return super(DashboardTemplateView,self).dispatch(request,*args,**kwargs)

























def post_create(request):
    form=PostModalForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        obj=form.save(commit=False)
        obj.save()
        messages.success(request,'Form created Successfull')
        context = {'form': PostModalForm(request.POST or None)}
    template = 'blog/create-view.html'
    return render(request, template, context)


def post_delete(request,id=None):
    qs = get_object_or_404(PostModel, id=id)
    if request.method=="POST":
        qs.delete()
        messages.success(request,'Form deleted successfull')
        return HttpResponseRedirect('/blog/')

    context={
        'text':qs,
    }
    template = 'blog/delete-view.html'
    return render(request, template, context)

def post_update(request,id=None):
    qs = get_object_or_404(PostModel, id=id)
    form=PostModalForm(request.POST or None,instance=qs)
    context = {'form': form}
    if form.is_valid():
        obj=form.save(commit=False)
        obj.save()
        messages.success(request,'Form Updated Successfull')
        context = {'form': PostModalForm(request.POST or None)}
    template = 'blog/create-view.html'
    return render(request, template, context)


def post_model_list_view(request):
    query=request.GET.get('text',None)
    qs=PostModel.objects.all()
    if query is not None:
        qs=qs.filter(Q(title=query) |
                     Q(content=query) |
                     Q(slug=query)
                     )
    template='blog/list-view.html'
    context={'text': qs}
    return  render(request,template,context)

def post_model_detail_view(request,id):
    qs=get_object_or_404(PostModel,id=id)
    template='blog/detail-view.html'
    context={'text':qs}
    return  render(request,template,context)



# @login_required(login_url='/login')
# def post_model_list_view(request):
#     qs=PostModel.objects.all()
#     print(request.user.is_authenticated)
#     if request.user.is_authenticated:
#         template='blog/list-view.html'
#         context={'text': qs}
#     else:
#         return HttpResponse("<h1>Please Login</h1>")
#
#     return  render(request,template,context)