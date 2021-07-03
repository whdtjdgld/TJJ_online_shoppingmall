from django.http.response import HttpResponse
from django.template import loader
from .models import Product
from django.views.decorators.csrf import csrf_exempt
from project2.settings import PAGE_SIZE, PAGE_BLOCK
import logging
logger = logging.getLogger(__name__)


@csrf_exempt
def necklace( request ):
    template = loader.get_template( "neckless.html" )
    memid = request.session.get( "memid" )
    count = Product.objects.filter(bcate="Necklace").count()
    pagenum = request.GET.get("pagenum")
    if not pagenum :
        pagenum = "1"
    pagenum = int( pagenum )
    start = ( pagenum -1 ) * int(PAGE_SIZE)
    end = start + int( PAGE_SIZE )
    prods = Product.objects.filter(bcate="Necklace")[start:end]
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
    context = {
        "prods":prods,
        "memid":memid,
        "count":count,
        "pagenum" : pagenum,
        "number" : number,
        "pages" : pages,
        "startpage" : startpage,
        "endpage" : endpage,
        "pageblock" : PAGE_BLOCK,
        "pagecount" : pagecount,
        }
    return HttpResponse( template.render( context, request ) )

@csrf_exempt
def earring( request ):
    template = loader.get_template( "earing.html" )
    memid = request.session.get( "memid" )
    count = Product.objects.filter(bcate="Earring").count()
    pagenum = request.GET.get("pagenum")
    if not pagenum :
        pagenum = "1"
    pagenum = int( pagenum )
    start = ( pagenum -1 ) * int(PAGE_SIZE)
    end = start + int( PAGE_SIZE )
    prods = Product.objects.filter(bcate="Earring")[start:end]
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
    context = {
        "prods":prods,
        "memid":memid,
        "count":count,
        "pagenum" : pagenum,
        "number" : number,
        "pages" : pages,
        "startpage" : startpage,
        "endpage" : endpage,
        "pageblock" : PAGE_BLOCK,
        "pagecount" : pagecount,
        }
    return HttpResponse( template.render( context, request ) )


@csrf_exempt
def ring( request ):
    template = loader.get_template( "ring.html" )
    memid = request.session.get( "memid" )
    count = Product.objects.filter(bcate="Ring").count()
    pagenum = request.GET.get("pagenum")
    if not pagenum :
        pagenum = "1"
    pagenum = int( pagenum )
        
    start = ( pagenum -1 ) * int(PAGE_SIZE)
    end = start + int( PAGE_SIZE )
    prods = Product.objects.filter(bcate="Ring")[start:end]
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
    context = {
        "prods":prods,
        "memid":memid,
        "count":count,
        "pagenum" : pagenum,
        "number" : number,
        "pages" : pages,
        "startpage" : startpage,
        "endpage" : endpage,
        "pageblock" : PAGE_BLOCK,
        "pagecount" : pagecount,
        }
    return HttpResponse( template.render( context, request ) )


@csrf_exempt
def bracelet( request ):
    template = loader.get_template( "bracelet.html" )
    memid = request.session.get( "memid" )
    
    count = Product.objects.filter(bcate="Bracelet").count()
    pagenum = request.GET.get("pagenum")
    if not pagenum :
        pagenum = "1"
    pagenum = int( pagenum )
    
    start = ( pagenum -1 ) * int(PAGE_SIZE)
    end = start + int( PAGE_SIZE )
    prods = Product.objects.filter(bcate="Bracelet")[start:end]
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
    
    context = {
        "memid":memid,
        "prods":prods,
        "count":count,
        "pagenum" : pagenum,
        "number" : number,
        "pages" : pages,
        "startpage" : startpage,
        "endpage" : endpage,
        "pageblock" : PAGE_BLOCK,
        "pagecount" : pagecount,
        }
    return HttpResponse( template.render( context, request ) )


@csrf_exempt
def plist( request ) :
    template = loader.get_template( "plist.html" )   
    pnum = request.GET.get( "pnum" )
    prod = Product.objects.get(pnum=pnum)
    memid = request.session.get( "memid" )
    context = {
        "memid":memid,
        "prod":prod,
        }
    logger.info("plist " + str(memid) + " " + str(pnum))
    return HttpResponse( template.render( context, request ) )
    