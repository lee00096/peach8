from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Comment

def new(request):
    return render(request, 'products/new.html')

def create(request):
    if request.method == "POST":
        product_title = request.POST.get('title')
        product_content = request.POST.get('content')
        image = request.FILES.get('image')
        user = request.user
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        Product.objects.create(title=product_title, content=product_content, image=image, stock=stock, user=user, price=price)
    return redirect('products:main')

def main(request):
    all_products = Product.objects.all()
    return render (request, 'products/main.html', {'products': all_products})

def show(request, id):
    product = Product.objects.get(pk=id)
    increased_view_count = product.view_count + 1
    product.view_count = increased_view_count
    product.save()
    all_comments = product.comments.all().order_by('-created_at')
    return render (request, 'products/show.html', {'product': product, 'comments': all_comments})

def update(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        product.title = request.POST['title']
        product.content = request.POST['content']
        product.image = request.FILES.get('image')
        product.save()
        return redirect('products:show', product.id)
    return render(request, 'products/edit.html', {"product": product})

def delete (request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect('products:main')

def create_comment(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_id)
        current_user = request.user
        comment_content = request.POST.get('content')
        Comment.objects.create(content=comment_content, user=current_user, product=product)
    return redirect('products:show', product_id)