from django.shortcuts import render
import random
from bisheapp import models
import time
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import user
from .form import ArticleForm,ArticleForm2,ArticleForm3
# Create your views here.
def index(request):
    return render(request,'bisheindex.html')
def login_action(request):
    if request.method == 'POST':
        # 如果登录成功，绑定参数到cookie中，set_cookie
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 查询用户是否在数据库中
        if models.user.objects.filter(user=username).exists():
            user = models.user.objects.get(user=username)
            if password==user.password:
                response = HttpResponseRedirect('/event_manage/')
                # max_age 存活时间(秒)
                response.set_cookie('username',username,3600)
                # 存在服务端
                return response
            else:
                # return HttpResponse('用户密码错误')
                return render(request, '404.html', {'password': '用户密码错误'})
        else:
            # return HttpResponse('用户不存在')
            return render(request, '404.html', {'name': '用户不存在'})
def rootlogin(request):
    return render(request, "rootlogin.html")
def backindex(request):
    return render(request, "bisheindex.html")
def event_manage(request):
    username = request.COOKIES.get('username', '')
    infolist = models.Topic.objects.all()
    # user=models.user.objects.filter(user__icontains=username)
    # if user:
    #     username = user[0]
    # return render_to_response('successfullogin.html', {'username': username})
    return render(request, "successfullogin.html",{"username":username,"infolist":infolist})
def register(request):
    if request.method == 'POST':
        regname=request.POST.get('username')
        regpwd=request.POST.get('password')
        regphone=request.POST.get('phone')
        regemail=request.POST.get('email')
        models.user.objects.create(user=regname, password=regpwd,phone=regphone,email=regemail)
        return render(request,'bisheindex.html')
def rootlogin_action(request):
    if request.method == 'POST':
        # 如果登录成功，绑定参数到cookie中，set_cookie
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 查询用户是否在数据库中
        if models.rootuser.objects.filter(user=username).exists():
            user = models.rootuser.objects.get(user=username)
            if password==user.password:
                response = HttpResponseRedirect('/rootevent_manage/')
                # max_age 存活时间(秒)
                response.set_cookie('username',username,3600)
                # 存在服务端
                return response
            else:
                # return HttpResponse('用户密码错误')
                return render(request, '404.html', {'password': '用户密码错误'})
        else:
            # return HttpResponse('用户不存在')
            return render(request, '404.html', {'name': '用户不存在'})
def rootevent_manage(request):
    username=request.POST.get('username','')
    user=models.rootuser.objects.filter(user__icontains=username)
    return render(request, "rootsuccessfullogin.html")
def rootindex(request):
    return render(request, "rootsuccessfullogin.html")
def successfullogin(request):
    username = request.COOKIES.get('username', '')
    infolist = models.Topic.objects.all()
    return render(request, "successfullogin.html",{"username":username,"infolist":infolist})
def yonghuyemian(request):
    username = request.COOKIES.get('username', '')
    return render(request, "yonghuyemian.html",{"username":username})
def yonghuyemian2(request):
    username = request.COOKIES.get('username', '')
    return render(request, "yonghuyemian2.html",{"username":username})
def yonghuyemian3(request):
    username = request.COOKIES.get('username', '')
    return render(request, "putongyonghuxiugai.html",{"username":username})
def wodetiezi(request):
    username = request.COOKIES.get('username', '')
    infolist = models.Topic.objects.all()
    userlist=models.user.objects.all()
    return render(request, "wodetiezi.html",{"username":username,"infolist":infolist,"userlist":userlist})
def gonggao(request):
    username = request.COOKIES.get('username', '')
    gonggaolist=models.Announcement.objects.last()
    title=gonggaolist.a_title
    content=gonggaolist.a_content
    return render(request, "gonggao.html",{"username":username,"title":title,"content":content})
def map_google(request):
    username = request.COOKIES.get('username', '')
    return render(request, "map-google.html",{"username":username})
def fatieyemian(request):
    username = request.COOKIES.get('username', '')
    kinds = models.Kind.objects.filter()
    return render(request, "fatieyemian.html",{"username":username,"kinds":kinds})
def cuowuyemian(request):
    username = request.COOKIES.get('username', '')
    return render(request, "404.html",{"username":username})
def edit_article(request):
  # 查询到指定的数据
  username = request.COOKIES.get('username', '')
  userinfo = models.user.objects.get(user=username)
  if request.method != 'POST':
   # 如果不是post,创建一个表单，并用instance=article当前数据填充表单
    form = ArticleForm(instance=userinfo)
  else:
      form = ArticleForm(request.POST)
      if form.is_valid():
  # 如果是post,instance=article当前数据填充表单，并用data=request.POST获取到表单里的内容
        form = ArticleForm(instance=userinfo, data=request.POST)
        form.save() # 保存
        if form.is_valid(): # 验证
            return HttpResponseRedirect('/') # 成功跳转
      return render(request, 'successfullogin.html', {'form':form,'username':username})
def publish(request):
    if request.method == 'GET':
        kinds = models.Kind.objects.filter()
        response = {
            'kinds': kinds
        }
        return render(request, 'fatieyemian.html', response)
    elif request.method == 'POST':
        # session获取uid
        uid  = request.COOKIES.get('username', '')
        # 提交发布的文章
        t_title = request.POST.get('t_title')
        t_introduce = request.POST.get('t_introduce')
        t_content = request.POST.get('t_content')
        t_kind = request.POST.get('t_kind')
        print(t_title, t_introduce)

        obj = models.Topic.objects.create(t_title=t_title, t_introduce=t_introduce,
                                          t_content=t_content, t_kind=t_kind, t_uid=uid)
        t_id = obj.id

        # 存帖子图片
        t_photo = request.FILES.get('t_photo', None)
        t_photo_path = 'static/img/t_photo/' + str(t_id) + '_' + t_photo.name

        if t_photo:
            # 保存文件
            import os
            f = open(os.path.join(t_photo_path), 'wb')
            for line in t_photo.chunks():
                f.write(line)
            f.close()

        # 吧图片路径存入数据库
        models.Topic.objects.filter(id=t_id).update(t_photo='/'+t_photo_path)

        return redirect('/successfullogin')
def edit_article2(request):
  # 查询到指定的数据
  username = request.COOKIES.get('username', '')
  userinfo = models.rootuser.objects.get(user=username)
  if request.method != 'POST':
   # 如果不是post,创建一个表单，并用instance=article当前数据填充表单
    form = ArticleForm2(instance=userinfo)
  else:
      form = ArticleForm2(request.POST)
      if form.is_valid():
  # 如果是post,instance=article当前数据填充表单，并用data=request.POST获取到表单里的内容
        form = ArticleForm2(instance=userinfo, data=request.POST)
        form.save() # 保存
        if form.is_valid(): # 验证
            return HttpResponseRedirect('/') # 成功跳转
      return render(request, 'successfullogin.html', {'form':form,'username':username})
def edit_article3(request):
  # 查询到指定的数据
  username = request.COOKIES.get('username', '')
  replaceusername=request.POST.get('olduser', '')
  userinfo = models.user.objects.get(user=replaceusername)
  if request.method != 'POST':
   # 如果不是post,创建一个表单，并用instance=article当前数据填充表单
    form = ArticleForm(instance=userinfo)
  else:
      form = ArticleForm(request.POST)
      if form.is_valid():
  # 如果是post,instance=article当前数据填充表单，并用data=request.POST获取到表单里的内容
        form = ArticleForm(instance=userinfo, data=request.POST)
        form.save() # 保存
        if form.is_valid(): # 验证
            return HttpResponseRedirect('/') # 成功跳转
      return render(request, 'successfullogin.html', {'form':form,'username':username})
def gengxingonggao(request):
    username = request.COOKIES.get('username', '')
    return render(request, "gengxingonggao.html",{"username":username})
def gengxingonggao2(request):
    if request.method == 'GET':
        gonggaoinfo = models.Announcement.objects.filter()
        response = {
            'gonggaolist': gonggaoinfo
        }
        return render(request, 'rootsuccessfullogin.html', response)
    elif request.method == 'POST':
        # session获取uid
        uid  = request.COOKIES.get('username', '')
        # 提交发布的文章
        a_title = request.POST.get('a_title')
        a_content = request.POST.get('gonggaoneirong')
        print(a_title, a_content)

        models.Announcement.objects.create(a_title=a_title, a_content=a_content,
                                          )
        return redirect('/rootevent_manage')
def qingchugonggao(request):
    username = request.COOKIES.get('username', '')
    return render(request, "qingchugonggao.html",{"username":username})
def qingchugonggao2(request):
    if request.method == 'GET':
        gonggaoinfo = models.Announcement.objects.filter()
        response = {
            'gonggaolist': gonggaoinfo
        }
        return render(request, 'rootsuccessfullogin.html', response)
    elif request.method == 'POST':
        # 删除所选公告
        a_title = request.POST.get('a_title')
        print(a_title)
        gonggaolist=models.Announcement.objects.filter(a_title=a_title).first()
        if gonggaolist:
            gonggaolist.delete()
        return redirect('/rootevent_manage')


