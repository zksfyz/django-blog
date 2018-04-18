#-*-coding:utf-8-*-
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from myblog.models import Article
from datetime import datetime
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  #添加包
from django.shortcuts import render_to_response
import sys,os

# Create your views here.

#@login_required
#def home(request):
#    return HttpResponse("Hello World")


#@login_required
def home(request):
    #post_list = Article.objects.all()
    posts = Article.objects.all()
    #return render(request, 'home.html', {'post_list': post_list})
    paginator = Paginator(posts, 10) #每页显示两个
    page = request.GET.get('page')
    try :
        post_list = paginator.page(page)
    except PageNotAnInteger :
        post_list = paginator.page(1)
    except EmptyPage :
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'home.html', {'post_list' : post_list})

def detail(request,id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
	raise Http404
        #str = ("tiles = %s,category = %s,date_time = %s,content = %s " %(post.title,post.category,post.date_time,post.content))
        #return HttpResponse("You're looking at my_args %s." % my_args)
    return render(request,'post.html',{'post':post})
    

def test(request):
    return render(request,'test.html',{'current_time': datetime.now()})

def archives(request) :
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'archives.html', {'post_list' : post_list,'error' : False})
def about_me(request) :
    return render(request, 'aboutme.html')

def search_tag(request, tag) :
    try:
        post_list = Article.objects.filter(category__iexact = tag) #contains
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'tag.html', {'post_list' : post_list})

def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request,'home.html')
        else:
            post_list = Article.objects.filter(title__icontains = s)
            if len(post_list) == 0 :
                return render(request,'archives.html', {'post_list' : post_list,'error' : True})
            else :
                return render(request,'archives.html', {'post_list' : post_list,'error' : False})
    return redirect('/')
#def home(request):
#    post_list = Article.objects.all()
#    return render(request, 'home.html', {'post_list': post_list})


def page_not_found(request):
    return render_to_response('404.html')

def page_error(request):
    return render_to_response('500.html')

#以下代码暂不使用
def download(request):
    the_file_name = request.path.split('/')[3]
    def readFile(fn,buf_size=262144):
	f = open(fn,"rb")
	while True:
	    c = f.read(buf_size)
	    if c:
	        yield c
	    else:
		break
	f.close()
    response = HttpResponse(readFile(file_name))
    #response = HttpResponse(readFile(sys.path[0]+'/display/paper/'+the_file_name),content_type = 'APPLICATION/OCTET-STREAM')
    #response['Content-Disposition'] = 'attachment;filename = '+the_file_name.encode('utf-8')
    #response['Content-Length'] = os.path.getsize(sys.path[0]+'/display/paper/'+the_file_name)
    return response


def downloadFile(req):
  filename=basePath+req.GET['url']
  def file_iterator(file_name, chunk_size=5120):
    with open(file_name) as f:
      while True:
        c = f.read(chunk_size)
        if c:
          yield c
        else:
          break
  response = StreamingHttpResponse(file_iterator(filename))
  response['Content-Type'] = 'application/octet-stream'
  response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filename)
  return response

def file_download(request, filename):  
  
    filepath = os.path.join(settings.MEDIA_ROOT, filename)    
      
    print (filepath)   
    wrapper = FileWrapper(open(filepath, 'rb'))  
    content_type = mimetypes.guess_type(filepath)[0]  
    response = HttpResponse(wrapper, mimetype='content_type')  
    response['Content-Disposition'] = "attachment; filename=%s" % filename  
    return response    




