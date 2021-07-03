$(document).ready(
   function() {
      $("form[name=joinform]").on(
         "submit",
         function(event) {
            if($("input[name=user_id]").val() == "") {
               alert("아이디를 입력하세요")
               return false
            }
            if($("input[name=password]").val() == ""
               || $("input[name=password1]").val() == "") {
               alert("비밀번호를 입력하세요")
               return false
            }
            if($("input[name=password]").val()
               != $("input[name=password1]").val()) {
               alert("비밀번호를 다시 확인하세요")
               return false
            }
         }
      )
      
       $("form[name=loginform]").on(
         "submit",
         function(event) {
            if($("input[name=user_id]").val() == "") {
               alert("아이디를 입력하세요")
               return false
            }
            if($("input[name=password]").val() == "") {
               alert("비밀번호를 입력하세요")
               return false
            }
         }
      )
      
      $(".confirm").on(
         "click",
         function(event) {
            if($("input[name=user_id]").val() == "") {
               alert("아이디를 입력하세요")
               return false
            } else {
               url = "confirm" + "?user_id=" + $("input[name=user_id]").val()
               open(url,"confirm","toolbar=no,menubar=no,scrollbar=no,status=no,width=400,height=200")
            } // else
         } // f(event)
      ) // confirm on
      
       $("form[name=passform]").on(
         "submit",
         function(event) {
            if($("input[name=password]").val() == "") {
               alert("비밀번호를 입력하세요")
               return false
            }
         }
      )
      
      $("form[name=modifyform").on(
       "submit",
       function(event) {
          if($("input[name=password]").val()==""){
             alert("비밀번호를 입력하세요")
             return false
          }
          if($("input[name=password]").val()
                != $("input[name=password1]").val()) {
             alert("비밀번호가 다릅니다")
             return false
          }
       }
      )
      
      $("#emailresult").html("&nbsp;이메일을 입력해주세요")
      $("#telresult").html("&nbsp;-는 제외하고 입력해주세요")
      $("input[name=email]").on(
          "keyup",
          function(event){
             $.ajax(
                {
                   url : "emailcheck",
                   type : "POST",
                   data : {
                       keyword:$("input[name=email]").val()
                   },
                    dataType : "text",
                    success : function(data){
                   $("#emailresult").html("&nbsp" + data)
                    },
                error : function() {
                }
             }
          )   
       }
     )
      
      $("input[name=hp]").on(
       "keydown",
       function(event){
          
          $("#telresult").html("&nbsp;전화번호 형식에 맞지않습니다")
       }
      )
      
      
      
   }// ready fun
) //ready

function setid(id){
   opener.document.registerform.user_id.value = id
   self.close()
} // setid