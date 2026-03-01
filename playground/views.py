from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q, F, Value, Func, ExpressionWrapper
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Min
from store.models import Product, OrderItem, Order, Customer
from tags.models import TaggedItems

# Create your views here.
def say_hello(request):
    # query_set = Product.objects.all()
    
    # query_set's(the all method specifically) are lazy,
    # in the sense that they cann't be used in program directly and need to be accessed
    # query_set[0:5]
    # list(query_set)
    # for product in query_set:
    #     print(product)
    
    # try:    
    #     product = Product.objects.get(pk=1) #.get(unit_price__gt=20,filter(unit_price__range=(20,30)))
    #     .filter(title__icontains='coffee',last_update__year=2021.values("id","title","collection__title") #uses inner join for collection
    # except ObjectDoesNotExist:
    #     pass
    # or
    # product = Product.objects.filter(pk=1).first() #.exists() in which case boolean
    # product = Product.objects.filter(Q(unit_price__lt=20) | ~Q(inventory__lt=10)) # used for or operation
    # product = Product.objects.filter(inventory = F("collection_id"))
    # products = OrderItem.objects.values("product__title").distinct().order_by("product__title") #only("product__title").defer("title")
    # products = Order.objects.select_related("customer").prefetch_related("orderitem_set__product").order_by("-placed_at")[:5]
    # return render(request, 'hello.html', {"name": "Yon", "products":products})

    # order = Product.objects.aggregate(product_count=Count('id'))
    # order = Product.objects.annotate(new_id = Value(True)).annotate(new_id = F('id') + 1) # annotate means to add # or
    # order = Customer.objects.annotate(full_name = Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT'))
    #.annotate(full_name = Concat('first_name', Value(' '), 'last_name'))
    # order = Product.objects.annotate(discount = ExpressionWrapper(F('unit_price')* 0.8, output_field=DecimalField()))
    # return render(request, 'hello.html', {"name": "Yon", "order": order})

    Content_type = ContentType.objects.get_for_model(Product)
    tags = TaggedItems.objects.select_related('tag').filter(content_type=Content_type, object_id=1)

    return render(request, 'hello.html', {"name": "Yon", "tags": tags})
    