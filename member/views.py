from django.http.response import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist
from member.models import Sign
from django.views.decorators.csrf import csrf_exempt
from product.models import Product
from order.models import Buy
from order.models import Order
from order.models import Recommend
from django.shortcuts import redirect, render
from project2.settings import PAGE_SIZE, PAGE_BLOCK
import logging
from django.contrib.auth.forms import AuthenticationForm

logger = logging.getLogger(__name__)

# app패키지의 urls에서 건거 여기로 온다
@csrf_exempt
def confirm( request ) :
    template = loader.get_template( "confirm.html" )
    user_id = request.GET["user_id"]
    try :
        Sign.objects.get( user_id=user_id ) 
        result = 1
    except ObjectDoesNotExist :
        result = 0        
    context = {
        "result":result,
        "user_id":user_id
        }
    return HttpResponse( template.render( context, request ) )


def main( request ) :    
    template = loader.get_template( "main.html" )
    memid = request.session.get( "memid" )
    rec = Recommend.objects.filter(member=memid)
    count = Product.objects.filter(best="등록").count()
    pagenum = request.GET.get("pagenum")
    if not pagenum :
        pagenum = "1"
    pagenum = int( pagenum )
    
    start = ( pagenum -1 ) * int(PAGE_SIZE)
    end = start + int( PAGE_SIZE )
    prods = Product.objects.filter(best="등록")[start:end]
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
        "rec":rec,
        }
    return HttpResponse( template.render( context, request ) )


def mypage( request ) :    
    template = loader.get_template( "mypage.html" )
    user_id = request.GET["user_id"]
    memid = request.session.get( "memid" )
    dto = Sign.objects.get(user_id=user_id)
    context = {
        "memid":memid,
        "dto":dto,
        }
    return HttpResponse( template.render( context, request ) )

@csrf_exempt
def join( request ) :
    if request.method == "POST" :   
        dto = Sign(
            user_id = request.POST["user_id"],
            password = request.POST["password"],
            email = request.POST["email"],
            tel = request.POST["tel"],
            name = request.POST["name"],
            birth = request.POST["birth"],
            gender = request.POST["gender"],
            address = request.POST["address"],
            style = request.POST["style"],
            job = request.POST["job"],
            )
        dto.save()              # insert 호출
        return redirect( "login" )
    else :
        template = loader.get_template( "join.html" )
        context = {}
        return HttpResponse( template.render( context, request ) )
    
@csrf_exempt    
def login( request ) :
    if request.method == "POST" : 
        user_id = request.POST["user_id"]
        password = request.POST["password"]
        template = loader.get_template( "login.html" )
        try :
            dto = Sign.objects.get( user_id=user_id )
            # 아이디가 있는 경우     
            if password == dto.password :
                # 비밀번호가 같다 - 로그인 처리
                request.session["memid"] = user_id  # 쿠키      
                return redirect( "main" )
            else :    
                message = "입력한 비밀번호가 다릅니다"
        except ObjectDoesNotExist :
            # 아이디가 없는 경우
            message = "입력한 아이디가 없습니다"
        context = {
            "message": message,
            }    
        return HttpResponse( template.render( context, request ) )
    else :
        template = loader.get_template( "login.html" )
        context = {}
        return HttpResponse( template.render( context, request ) )
            
def logout( request ) :
    memid = request.session.get( "memid" )
    del( request.session["memid"] )
    return redirect( "main" )
    logger.info("logout : " + str(memid))

@csrf_exempt   
def modify( request ) :
    if request.method == "POST" : 
        user_id = request.session.get( "memid" )
        password = request.POST["password"]
        dto = Sign.objects.get( user_id=user_id )    
        if password == dto.password :
            context = {
                "dto":dto,
                }
            return redirect( "modifypro" )
        else :
            template = loader.get_template( "modify.html" )
            context = { 
               "message" : "비밀번호가 다릅니다",
               }
        return HttpResponse( template.render( context, request ) ) 
    else :
        template = loader.get_template( "modify.html" )
        context = {}
        return HttpResponse( template.render( context, request ) )
    
def modifypro( request ) :
    template = loader.get_template( "modifyview.html" )
    user_id = request.session.get( "memid" )
    dto = Sign.objects.get( user_id = user_id)
    if request.method == "POST" :
        dto = Sign(
            user_id = dto.user_id,
            password = request.POST["password"],
            email = request.POST["email"],
            tel = request.POST["tel"],
            name = request.POST["name"],
            birth = dto.birth,
            gender = dto.gender,
            address = request.POST["address"],
            style = request.POST["style"],
            job = request.POST["job"],
            )
        dto.save()              # insert 호출
        return redirect( "login" )
    else :
        template = loader.get_template( "modifyview.html" )
        context = {
            "dto":dto,
            }
        return HttpResponse( template.render( context, request ) )

@csrf_exempt
def emailcheck( request ) : 
    user_id = request.session.get( "memid" )
    keyword = request.POST["keyword"]
    dtos = Sign.objects.all()
    check = False
    for dto in dtos :
        if keyword == dto.email and user_id != dto.user_id :
            check = True
            break;
    if check == True :
        return HttpResponse( "존재하는 이메일입니다" )    
    else :
        return HttpResponse( "사용 가능한 이메일입니다" )
    
def delete( request ) :
    if request.method == "POST" : 
        user_id = request.session.get( "memid" )
        password = request.POST["password"]
        dto = Sign.objects.get( user_id=user_id )
        if password == dto.password :
            dto.delete()  # delete 호출
            del( request.session["memid"] )
            return redirect( "main" )
        else :
            template = loader.get_template( "delete.html" )
            context = { 
               "message" : "비밀번호가 다릅니다",
               }
            return HttpResponse( template.render( context, request ) ) 
    else :        
        template = loader.get_template( "delete.html" )
        context = {}
        return HttpResponse( template.render( context, request ) )

def orderlist(request) :
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