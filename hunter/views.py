from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

from dbe.todo.models import *
from django.core.urlresolvers import reverse
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def item_action(request, action, pk):
    """Mark done, toggle onhold or delete a todo item."""
    if action == "done":
        item = Item.objects.get(pk=pk)
        item.done = True
        item.save()
    elif action == "onhold":
        item = Item.objects.get(pk=pk)
        if item.onhold: item.onhold = False
        else: item.onhold = True
        item.save()
    elif action == "delete":
        Item.objects.filter(pk=pk).delete()

