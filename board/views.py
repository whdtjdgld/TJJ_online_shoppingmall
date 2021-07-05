from django.shortcuts import render, redirect
from django.template import loader
from django.http.response import HttpResponse
from board.models import Board

import logging
from django.utils.dateformat import DateFormat
from datetime import datetime
from project2.settings import PAGE_SIZE, PAGE_BLOCK
from django.views.decorators.csrf import csrf_exempt
from member.models import Sign
logger = logging.getLogger(__name__)

def boardlist( request ) :            
    template = loader.get_template( "boardlist.html" )
    memid = request.session.get( "memid" )
    count = Board.objects.all().count()
    pagenum = request.GET.get("pagenum")
    if not pagenum :
        pagenum = "1"
    pagenum = int( pagenum )    
        
    start = ( pagenum -1 ) * int(PAGE_SIZE)    # ( 3 - 1 ) * 10     20
    end = start + int( PAGE_SIZE )             # 20 + 10            30
    if end > count : 
        end = count    
    dtos = Board.objects.order_by("-ref", "restep")[start:end]
    number = count - ( pagenum - 1 ) * int(PAGE_SIZE)
    
    startpage = pagenum // PAGE_BLOCK * PAGE_BLOCK + 1
                # 9 // 10 * 10 + 1     1
                # 19 // 10 * 10 + 1    11
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
        "count" : count,
        "dtos" : dtos,
        "pagenum" : pagenum,
        "number" : number,
        "pages" : pages,
        "startpage" : startpage,
        "endpage" : endpage,
        "pageblock" : PAGE_BLOCK,
        "pagecount" : pagecount,
        }            
    return HttpResponse( template.render( context, request ) )

def write( request ) :
    memid = request.session.get( "memid" )
    member = Sign.objects.get(user_id=memid)
    if request.method == "POST" :
        pass
    else :
        # GET 
        # 글목록 - num ref restep relevel X    제목글 작성
        # 글보기 - num ref restep relevel O    답글 작성

        ref = 1         # 그룹화 아이디
        restep = 0      # 글순서
        relevel = 0     # 글레벨
        
        num = request.GET.get("num")
        if num == None :
            # 제목글
            try :
                # 글이 있는 경우
                maxnum = Board.objects.order_by('-num').values()[0]["num"]
                logger.info( "maxnum" + str( maxnum ))
                ref = maxnum + 1    # 글번호 최대값 + 1
            except IndexError :
                # 글이 없는 경우
                ref = 1            
        else :
            # 답변글
            num = request.GET.get("num")
            ref = request.GET.get("ref")
            restep = request.GET.get("restep")
            relevel = request.GET.get("relevel")
            
            #            ref    restep    relevel
            # 제목글             8        0        0
            # ㄴ 답글            8        1        1
            #   ㄴ 재답글      8        2        2
            # ㄴ 답글            8        0        0

            #            ref    restep    relevel
            # 제목글             8        0        0
            # ㄴ 답글            8        2        1
            #   ㄴ 재답글      8        3        2
            # ㄴ 답글            8        1        1            
            
            #            ref    restep    relevel
            # 제목글             8        0        0
            # ㄴ 답글            8        1        1   
            # ㄴ 답글            8        2        1
            #   ㄴ 재답글      8        3        2
            
            res = Board.objects.filter( restep__gte=restep and ref==ref )
            for re in res :
                re.restep = int( re.restep ) + 1
                re.save()
            restep = int( restep ) + 1
            relevel = int( relevel ) + 1
       
        template = loader.get_template( "write.html" )
           
        context = {
            "memid":memid,
            "num":num,
            "ref":ref,
            "restep":restep,
            "relevel":relevel,
            "member":member,            
            }
        return HttpResponse( template.render( context, request ) )

def writepro( request ) :
    memid = request.session.get("memid")
    member = Sign.objects.get(user_id=memid)
    num = Board.objects.all().count()
    if num == None :
        num = 100
    else :    
        num += 1
    request.session["num"] = num    
    if request.method == "POST" :
        dto = Board(
            num = num,
            writer = member.user_id,
            subject = request.POST["subject"],
            passwd = request.POST["passwd"],
            content = request.POST["content"],
            readcount = 0,
            ref = request.POST["ref"],
            restep = request.POST["restep"],
            relevel = request.POST["relevel"],
            regdate = DateFormat( datetime.now()).format( "Ymd" ),
            ip = request.META.get( "REMOTE_ADDR" )
            )
        dto.save()
        return redirect( "boardlist" )

# 글보기
def detail( request ) :
    num = request.GET.get( "num" )
    pagenum = request.GET.get( "pagenum" )
    number = request.GET.get( "number" )
    template = loader.get_template( "detail.html" )
    memid = request.session.get( "memid" )
    dto = Board.objects.get(num=num)
    if dto.ip != request.META.get("REMOTE_ADDR" ) :                  
        dto.readcount += 1
        dto.save()    
    context = {
        "dto":dto,
        "pagenum":pagenum,
        "number":number,
        "memid":memid
        }
    return HttpResponse( template.render( context, request ) )

# 글수정
@csrf_exempt
def boardmodify( request ) :   
    if request.method == "POST" :
        num = request.POST.get( "num" )
        pagenum = request.POST.get( "pagenum" )
        number = request.POST.get( "number" )        
        passwd = request.POST.get( "passwd" )
        memid = request.session.get( "memid" )
        dto = Board.objects.get( num=num )        
        if passwd == dto.passwd : 
            template = loader.get_template( "boardview.html" )
            context = {
                "num" : num,
                "pagenum" : pagenum,
                "number" : number,
                "dto" : dto,
                "memid":memid
                }  
            return HttpResponse( template.render( context, request ) )           
        else :
            template = loader.get_template( "boardmodify.html" )
            context = {
                "num" : num,
                "pagenum" : pagenum,
                "number" : number,
                "memid":memid,
                "message" : "비밀번호가 다릅니다",
                }        
            return HttpResponse( template.render( context, request ) )       
    else :
        num = request.GET.get( "num" )
        pagenum = request.GET.get( "pagenum" )
        number = request.GET.get( "number" )
        memid = request.session.get( "memid" )
        template = loader.get_template( "boardmodify.html" )
        context = {
            "num" : num,
            "pagenum" : pagenum,
            "number" : number,
            "memid":memid
            }        
        return HttpResponse( template.render( context, request ) )

@csrf_exempt    
def boardview( request ) :
    num = request.POST.get( "num" )
    pagenum = request.POST.get( "pagenum" )
    subject = request.POST.get( "subject" )
    content = request.POST.get( "content" )
    passwd = request.POST.get( "passwd" )
    memid = request.session.get( "memid" )
    dto = Board.objects.get( num=num )
    dto.subject = subject
    dto.content = content
    dto.passwd = passwd  
    dto.save()
                
    return redirect( "boardlist" )
    
@csrf_exempt    
def boarddelete( request ) :
    if request.method == "POST" :
        num = request.POST.get( "num" )
        pagenum = request.POST.get( "pagenum" )
        passwd = request.POST.get( "passwd" )
        memid = request.session.get( "memid" )
        dto = Board.objects.get( num=num )
        if dto.passwd == passwd :
            dto.subject = "삭제된 글입니다."    
            dto.readcount = -1
            dto.save()
            return redirect( "boardlist" ) 
        else :
            # 비밀번호가 다르다
            template = loader.get_template( "boarddelete.html" )
            context = {
                "num" : num,
                "pagenum" : pagenum,                
                "message" : "비밀번호가 다릅니다",
                "memid":memid
                }        
            return HttpResponse( template.render( context, request ) )
    else :
        num = request.GET.get( "num" )
        pagenum = request.GET.get( "pagenum" )
        memid = request.session.get( "memid" )
        template = loader.get_template( "boarddelete.html" )
        context = {
            "num" : num,
            "pagenum" : pagenum,
            "memid":memid
            }        
        return HttpResponse( template.render( context, request ) )