from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import myform
# Create your views here.
#function_based_view
def myview(request):
    return HttpResponse('<h1>Function_Based_View</h1>')

#class_based_view
class MyView(View):
    name='ahsan'
    def get(self,request):
        #return HttpResponse('<h1>Class_Based_View____________GET</h1>')
        #also pass through urls
        return HttpResponse(self.name)

#child_class
class MychildView(MyView):
    def get(self,request):
       return HttpResponse(self.name)

#return render using function_view
def renderv(request):
    return render(request,'ahsan1.html')
#return render using class_based_view

class Myrender(View):
    def get(self,request):
        return render(request,'ahsan.html')

def conview(request):
    context={'name':'Welcome in function base view ahsan'}
    return render(request,'con_name.html',context)

class context_view(View):
    def get(self,request):
        context={'name':'Welcome in class base view ahsan'}
        return render(request,'con_name.html',context)

def myformview(request):
    if request.method=='POST':
        form=myform(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'],form.cleaned_data['no'])
            return HttpResponse('<h1>function_base_view____POST</h1>')
        
    else:
        form=myform()
    return render(request,'myform.html',{'form':form})


class myformvieW(View):
    def get(self,request):
        form=myform()
        return render(request,'myform.html',{'form':form})
    


    def post(self,request):
        form=myform(request.POST)
        if form.is_valid():
            a=form.cleaned_data['name']
            b=form.cleaned_data['no']
            print(a,b)
            return HttpResponse('<h1>Class_base_view____POST{{a}},{{b}}</h1>')
        

def news(request,template_name):
    template_name=template_name
    context={'about':'My name is ahsan taiq'}
    return render(request,template_name,context)

class newsbase(View):
    def get(self,request):
        context={'name':'Ahsan_Tariq(20-CSE-26)'}
        return render(request,'ahsannews.html',context)

class newsbaseN(View):
    template_name=''
    def get(self,request):
        
        context={'name':'Ahsan_Tariq(20-CSE-26) by any template'}
        return render(request,self.template_name,context)
        
        


        
  






