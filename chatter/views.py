"""send values to html"""
from django.shortcuts import render, redirect
from chatter.models import Chat
from . import forms
from django.core.context_processors import csrf
from django.utils import timezone
# Create your views here.

def chatter(request):
    """send data d"""
    c = {}
    c.update(csrf(request))
    title_id = request.GET.get("title")
    text_data = request.POST.get("text")
    name_data = request.POST.get("name")
    if(not name_data):
        name_data = "名無しさん"
    if (not not text_data) and (not not name_data):
        add_data = Chat(data_type="chat_text",parent=title_id,name_text=name_data,chat_text=text_data, pub_date=timezone.now())
        add_data.save()
        print("valid!")
        url = "/chatter/done/?url=" + "/chatter/chat/?title=" + title_id
        return redirect(url)
    else:
        print("not valid...")
        chat_data = Chat.objects.filter(parent=title_id)
        d = {
            "form": forms.Name(),
            "chat_data": chat_data,
            "title": Chat.objects.get(id=title_id),
        }
        return render(request, "chat.html", d)

def tagSelector(request):
    c = {}
    c.update(csrf(request))
    tag_data = Chat.objects.filter(parent="all")
    text_data = request.POST.get("text")
    name_data = request.POST.get("name")
    if (not not text_data) and (not not name_data):
        if( not tag_data.filter(name_text=name_data)):
            add_data = Chat(data_type="tag",parent="all",name_text=name_data,chat_text=text_data, pub_date=timezone.now())
            add_data.save()
            print("create new tag : name=" + name_data + " info=" + text_data)
        print("valid!")
    else:
        print("not valid...")
    d = {
        "form": forms.Name(),
        "tag_data": tag_data,
    }
    return render(request, "home.html", d)

def titleSelector(request):
    c = {}
    c.update(csrf(request))
    text_data = request.POST.get("text")
    name_data = request.POST.get("name")
    tag = request.GET.get("tag")
    tag_data = Chat.objects.get(data_type="tag",name_text=tag)
    titles = Chat.objects.filter(parent=tag)

    if (not not text_data) and (not not name_data):
        add_data = Chat(data_type="title",parent=tag,name_text=name_data,chat_text=text_data, pub_date=timezone.now())
        add_data.save()
        print("create new title : tag="+ tag + " name=" + name_data + " info=" + text_data)
        print("valid!")
        url = "/chatter/done/?url=" + "/chatter/titles/?tag=" + tag
        return redirect(url)
    else:
        print("not valid...")
        d = {
            "form": forms.Name(),
            "tag": tag_data,
            "titles": titles,
        }
        return render(request, "title.html", d)

def done(request):
    comeFrom = request.GET.get("url")
    print(comeFrom)
    return redirect(comeFrom)
