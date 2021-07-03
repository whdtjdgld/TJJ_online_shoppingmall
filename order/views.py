from product.models import Product
from order.models import Order
from member.models import Sign
from order.models import Buy
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from project2.settings import PAGE_SIZE, PAGE_BLOCK

import logging
logger = logging.getLogger(__name__)


def cart(request) :
    template = loader.get_template( "cart.html" )
    memid = request.session.get("memid")
    pnum = request.GET.get("pnum") # GET으로 넘어오는 값
    user_id = request.GET.get("user_id") # GET으로 넘어오는 값
    product = Product.objects.get(pnum=pnum)
    try : 
        # 장바구니는 user를 FK 참조 save()를 위해 user가 누구인지도 알아야함
        cart = Order.objects.get(order_id_id = user_id, prod_num_id = pnum)
        if cart :
            if cart.prod_num.pnum == product.pnum :
                cart.save()
    except ObjectDoesNotExist :
        user = Sign.objects.get(user_id=user_id)
        cart = Order(
            order_id = user,
            prod_num = product,
            quan = 1,
            )
        cart.save()
    j = Order.objects.filter(order_id_id = user_id)
    total_price = 0
    for a in j :
        total_price += a.prod_num.price * a.quan
    logger.info("cart " + str(memid) + " " + str(pnum))
    context = {
        "cart":cart,
        "pnum":pnum,
        "user_id":user_id,
        "product":product,
        "memid":memid,
        "j":j,
        "total_price":total_price,
        }
    
    return HttpResponse( template.render( context, request ) )

def cart_view(request) :
    template = loader.get_template( "cart_view.html" )
    memid = request.session.get("memid")
    cart = Order.objects.filter(order_id_id = memid)
    member = Sign.objects.get(user_id = memid)
    j = Order.objects.filter(order_id_id = memid)
    total_price = 0
    for a in j :
        total_price += a.prod_num.price * a.quan
    context = {
        "memid":memid,
        "cart":cart,
        "member":member,
        "total_price":total_price,
        }
    
    return HttpResponse( template.render( context, request ) )

def del_cart(request) :
    onum = request.GET.get("onum")
    cart = Order.objects.get(onum=onum)
    cart.delete()  # delete 호출
    return redirect( "del_cart_pro" )

def del_cart_pro(request) :
    memid = request.session.get( "memid" )
    cart = Order.objects.filter(order_id_id = memid)
    member = Sign.objects.get(user_id = memid)
    template = loader.get_template("cart_view.html")
    j = Order.objects.filter(order_id_id = memid)
    total_price = 0
    for a in cart :
        total_price += a.prod_num.price * a.quan
    context = {
        "memid":memid,
        "cart":cart,
        "member":member,
        "total_price":total_price,
        "j":j
        }
    return HttpResponse( template.render( context, request ) )

def add_cart(request) :
    pnum = request.GET.get("pnum")
    product = Product.objects.get(pnum=pnum)
    memid = request.session.get( "memid" )
    try:
        cart = Order.objects.get(prod_num=pnum, order_id=memid)
        if cart:
            if cart.prod_num.pname == product.pname:
                cart.quan += 1
                cart.save()
    except Order.DoesNotExist:
        user_id = Sign.objects.get(user_id=memid)
        cart = Order(
            user_id=user_id,
            product=product,
            # 장바구니에 해당 상품이 없을 경우 int 1을 선언
            quan=1,
        )
        cart.save()
    return redirect('add_cart_pro')

def add_cart_pro(request):
    memid = request.session.get( "memid" )
    cart = Order.objects.filter(order_id_id = memid)
    member = Sign.objects.get(user_id = memid)
    j = Order.objects.filter(order_id_id = memid)
    total_price = 0
    for a in cart :
        total_price += a.prod_num.price * a.quan
    template = loader.get_template("cart_view.html")
    context = {
        "memid":memid,
        "cart":cart,
        "member":member,
        "total_price":total_price,
        "j":j
        }
    return HttpResponse( template.render( context, request ) )

def minus_cart(request) :
    pnum = request.GET.get("pnum")
    product = Product.objects.get(pnum=pnum)
    memid = request.session.get( "memid" )
    try:
        cart = Order.objects.get(prod_num=pnum, order_id=memid)
        if cart:
            if cart.prod_num.pname == product.pname:
                cart.quan -= 1
                cart.save()
            if cart.quan < 1:
                cart.quan = 1
                cart.save()
    except Order.DoesNotExist:
        user_id = Sign.objects.get(user_id=memid)
        cart = Order(
            user_id=user_id,
            product=product,
            # 장바구니에 해당 상품이 없을 경우 int 1을 선언
            quan=1,
        )
        cart.save()
    return redirect('minus_cart_pro')

def minus_cart_pro(request):
    memid = request.session.get( "memid" )
    cart = Order.objects.filter(order_id_id = memid)
    member = Sign.objects.get(user_id = memid)
    template = loader.get_template("cart_view.html")
    j = Order.objects.filter(order_id_id = memid)
    total_price = 0
    for a in cart :
        total_price += a.prod_num.price * a.quan
    context = {
        "memid":memid,
        "cart":cart,
        "member":member,
        "total_price":total_price,
        "j":j
        }
    return HttpResponse( template.render( context, request ) )

def buy(request):
    # cart중 아이디가 같은것들 들고와서 buy에다가 저장
    memid = request.session.get( "memid" )
    order = Order.objects.filter(order_id_id=memid)
    for i in order :
        buy = Buy(
            member = memid,
            pnum = i.prod_num.pnum,
            pname = i.prod_num.pname,
            price = i.prod_num.price,
            quan = i.quan
            )
        buy.save()
        logger.info("buy " + str(buy.member) + " " + str(buy.pnum)+ " " +str(buy.price)+ " " +str(buy.quan))
    
    order.delete()
    return redirect('buy_pro')

def buy_pro(request):
    memid = request.session.get( "memid" )
    member = Sign.objects.get(user_id = memid)
    count = Buy.objects.filter(member=memid).count()
    pagenum = request.GET.get("pagenum")
    if not pagenum :
        pagenum = "1"
    pagenum = int( pagenum )
    start = ( pagenum -1 ) * int(PAGE_SIZE)
    end = start + int( PAGE_SIZE )
    buy = Buy.objects.filter(member = memid)[start:end]
    if end > count : 
        end = count
    number = count - ( pagenum - 1 ) * int(PAGE_SIZE)    
    startpage = pagenum // PAGE_BLOCK * PAGE_BLOCK + 1

    if pagenum % PAGE_BLOCK == 0 :
        startpage -= PAGE_BLOCK            
                
    endpage = startpage + PAGE_BLOCK - 1
                # 1 + 10 - 1           10                
    pagecount = ( count // PAGE_SIZE ) 
    if count % PAGE_SIZE > 0 :
        pagecount += 1  
    if endpage > pagecount :
        endpage = pagecount    
    
    pages = range( startpage, endpage+1 )

    template = loader.get_template("orderlist.html")
    context = {
        "memid":memid,
        "buy":buy,
        "member":member,
        "count":count,
        "pagenum" : pagenum,
        "list" : list,
        "number" : number,
        "pages" : pages,
        "startpage" : startpage,
        "endpage" : endpage,
        "pageblock" : PAGE_BLOCK,
        "pagecount" : pagecount,
        }
    return HttpResponse( template.render( context, request ) )

# submit을 누르면 장바구니 정보들이 결제로 넘어간다