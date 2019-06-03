from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .forms import PostModalForm
from .models import PostModel


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