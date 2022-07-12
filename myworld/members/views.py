from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members

def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('myfirst.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))
  
def addrecord(request):
  a = request.POST['first']
  b = request.POST['last']
  c = request.POST['father']
  d = request.POST['age']
  e = request.POST['email']
  f = request.POST['address']
  g = request.POST['contact'] 
  h = request.POST['edu']  
  member = Members(firstname=a, lastname=b,fathername=c,age=d,email=e,address=f,contact=g,education=h)
  member.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))


    
def update(request, id):
  mymember = Members.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))
  
def addrecord(request):
  a = request.POST['first']
  b = request.POST['last']
  c = request.POST['father']
  d = request.POST['age']
  e = request.POST['email']
  f = request.POST['address']
  g = request.POST['contact']
  h = request.POST['edu']
  
  member = Members(firstname=a, lastname=b,fathername=c,age=d,email=e,address=f,contact=g,education=h)
  member.save()
  return HttpResponseRedirect(reverse('index'))
  
def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))
  
def update(request, id):
  mymember = Members.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
  
def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  father = request.POST['father']
  age = request.POST['age']
  email = request.POST['email']
  address = request.POST['address']
  contact = request.POST['contact']
  edu = request.POST['edu']
  
  member = Members.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.fathername = father
  member.age = age
  member.email = email
  member.address = address
  member.contact = contact
  member.education = edu
  member.save()
 