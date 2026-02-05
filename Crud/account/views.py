from django.shortcuts import render,redirect
from django.views import View
from account.form import ProductsModelForm
from django.contrib import messages
from account.models import ProductModel

# Create your views here.

class HomeView(View):
    def get (self,request):
        return render(request,'home.html')

class AddProductView(View):
    def get(self,request):
        data=ProductsModelForm
        return render(request,'addproduct.html',{'form':data})
    def post(self,request):
        form_data=ProductsModelForm(data=request.POST,files=request.FILES)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,'Product Adedd succesfully')
            return redirect('home')
        return render('addproduct.html',{'form':form_data})

class ViewProductView(View):
    def get(self, request):
        products = ProductModel.objects.all()
        return render(request, 'viewproduct.html', {'products':products})

    
class FilterView(View):
    def get(self,request,**kwargs):
        category = kwargs.get('category')
        if category == 'all':
            products = ProductModel.objects.all()
            return render(request, 'viewproduct.html', {'products':products})
        elif category:
            products = ProductModel.objects.all()
            product = products.filter(category=category)
            return render(request, 'viewproduct.html', {'products':product})
        
    
class DeleteProductView(View):
    def get(self,request,**kwargs):
        pid=kwargs.get('pid')
        data=ProductModel.objects.get(id=pid)
        data.delete()
        return redirect('viewproduct')
    
class UpdateProductView(View):
    def get(self,request,**kwargs):
        eid=kwargs.get('eid')
        data=ProductModel.objects.get(id=eid)
        form=ProductsModelForm(instance=data)
        return render(request,'editproduct.html',{'form':form})
    def post(self,request,**kwargs):
        eid=kwargs.get('eid')
        data=ProductModel.objects.get(id=eid)
        form_data=ProductsModelForm(data=request.POST,files=request.FILES,instance=data)
        if form_data.is_valid():
            form_data.save()
            return redirect('viewproduct')
        return render('viewproduct.html',{'form':form_data})
    print("testing")
    print("third testing")
    print("Second Testing")


