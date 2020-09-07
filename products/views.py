from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Comment
from django.contrib.auth.decorators import login_required

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

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('Product', pk=product_id)

@login_required
def product_like(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product_like, product_like_created = product.like_set.get_or_create(user=request.user)

    if not product_like_created:
                product_like.delete()

    # if request.user in product.like_user_set.all():
    #     product.like_user_set.remove(request.user)
    # else:
    #     product.like_user_set.add(request.user)

    if request.GET.get('redirect_to') =='show':
            return redirect('products:show', product_id)
    else:
            return redirect('products:main')

@login_required
def like_list(request):
    likes = request.user.like_set.all()
    return render(request,'products/like_list.html',{'likes':likes})