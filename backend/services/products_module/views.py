from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from services.products_module.forms import UpdateProductForm
from services.user_module.forms import RegistrationForm
from services.products_module.models import Currency, Product, User
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.template.defaulttags import register
from django.contrib.auth.decorators import login_required

@register.filter
def get_range(value):
    return range(1,value+1)

# Create your views here.
def index(request):
    if not request.user.is_aunthenticated():
        # get_object_or_404(Product,pk=1)
        # try:
        #     Product.objects.get(pk=1)
        # except Product.DoesNotExist:
        #     return HttpResponse(status=404)
        return redirect('auth')
    
    
    products = Product.objects.all()
    paginator = Paginator(products, 1)

    disable_previos=False
    disable_next=False
    p =request.GET.get('page')
    if p==None or p=='':
        p='1'
    page_number = int(p)
    page_obj = paginator.get_page(page_number)

    if page_number==1:
        disable_previos=True
    if page_number==paginator.num_pages:
        disable_next=True

    context = {'products': page_obj, 'pages_count': paginator.num_pages, 'page_number': page_number,'disable_previos':disable_previos,'disable_next':disable_next}
    return render(request, 'index.html', context)


def myinit(request):

    User = get_user_model()

    # User.objects.all().delete()
    # Currency.objects.all().delete()
    # Product.objects.all().delete()

    if len(User.objects.all()) == 0:
        user1 = User.objects.create(username='test', email='test@gmail.com', password='123')
        user2 = User.objects.create(username='test2', email='test2@gmail.com', password='123')
    else:
        user1 = User.objects.get(username='test')
        user2 = User.objects.get(username='test2')

    currency = Currency.objects.get(title='USD')
    if currency == None:
        currency = Currency.objects.create(title='USD', symbol='$', price=1)

    if Product.objects.all().count == 0:
        product1 = Product.objects.create(title="Мобильный телефон Samsung Galaxy S22 Ultra 12/512GB Phantom Black (SM-S908BZKHSEK)", 
                                        description= 'Экран (6.8", Dynamic AMOLED 2X, 3088x1440) / Samsung Exynos 2200 (2.8 ГГц + 2.5 ГГц + 1.8 ГГц) / основная квадро-камера: 108 Мп + 12 Мп + 10 Мп + 10 Мп, фронтальная 40 Мп / RAM 12 ГБ / 512 ГБ встроенной памяти / 3G / LTE / 5G / GPS / поддержка 2х SIM-карт (Nano-SIM) / Android 12 / 5000 мА*ч',
                                        price= 51099,
                                        currency=currency,
                                        owner=user1,
                                        img='https://content2.rozetka.com.ua/goods/images/big/253281756.jpg')
        product2 = Product.objects.create(title="Мобильный телефон Samsung Galaxy M13 4/64GB Light Blue (SM-M135FLBDSEK)", 
                                        description= 'Экран (6.6", PLS, 2408x1080) / Samsung Exynos 850 (2.0 ГГц) / тройная основная камера: 50 Мп + 5 Мп + 2 Мп, фронтальная камера: 8 Мп / RAM 4 ГБ / 64 ГБ встроенной памяти + microSD (до 1 ТБ) / 3G / LTE / GPS / поддержка 2х SIM-карт (Nano-SIM) / Android 12 / 5000 мА*ч',
                                        price= 6749,
                                        currency=currency,
                                        owner=user1,
                                        img='https://content2.rozetka.com.ua/goods/images/big/277025916.jpg')
        product3 = Product.objects.create(title="Мобильный телефон Nokia G10 3/32GB Blue (719901148421)", 
                                        description= 'Экран (6.5", IPS 1600x720) / MediaTek Helio G25 (2.0 ГГц) / тройная основная камера: 13 Мп + 2 Мп + 2 Мп, фронтальная 8 Мп / RAM 3 ГБ / 32 ГБ встроенной памяти + microSD (до 512 ГБ) / 3G / LTE / GPS / поддержка 2х SIM-карт (Nano-SIM) / Android 11 / 5050 мА*ч',
                                        price= 4499,
                                        currency=currency,
                                        owner=user1,
                                        img='https://content2.rozetka.com.ua/goods/images/big/175052344.jpg')
        product4 = Product.objects.create(title="Телевизор Samsung UE55AU7100UXUA", 
                                        description= 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Pariatur autem reprehenderit cum nemo! Voluptatum, sequi aliquid ratione eaque non vitae, id ipsum saepe esse qui dolorem soluta quasi necessitatibus laudantium.',
                                        price= 23999,
                                        currency=currency,
                                        owner=user1,
                                        img='https://content.rozetka.com.ua/goods/images/big/303985527.jpg')
        product5 = Product.objects.create(title="Телевизор Samsung QE65Q70BAUXUA", 
                                        description= '...',
                                        price= 62999,
                                        currency=currency,
                                        owner=user1,
                                        img='')

    return HttpResponse("Data were added")


def mytest(request):

    print (1+2)
    return HttpResponse("test page")



def index(request):
    products = Product.objects.all()
    paginator = Paginator(products,2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context ={'products': page_obj, 'pages_count': paginator.num_pages, 'page_number': page_number}
    return render(request, 'index.html', context)
  




# closed not auth user
def get_my_products(request):
    if not request.user.is_auntificated:
        return redirect('auth')
    
    products = Product.objects.filter(owner=request.user)
    paginator = Paginator(products,1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'products': page_obj, 'pages_count': paginator.num_pages, 'page_number':page_number}

    return render(request, 'my_products.html', context)


def get_product(request, pk):
    product = get_object_or_404(Product,pk=pk)
    return render(request, 'product.html', context={'product':product, 'is_my_product': True})

@login_required
def create_product(request):
   if request.method == 'POST':
    form = UpdateProductForm(request.POST)
    if form.is_valid():
        Product.objects.create(**form.data)
        return redirect('get_product', pk=product.pk)
    else:
        form = UpdateProductForm
    return render(request, 'create_update_product.html', context={'product':product, 'is_my_product': True})


def update_product(request, pk):
   product = get_object_or_404(Product, pk=pk)

   return render(request, 'create_update_product.html', context={'product':product, 'is_my_product': True})

def delete_product(request, pk):
   product = get_object_or_404(Product, pk=pk).delete()

   return redirect('get_my_products')
