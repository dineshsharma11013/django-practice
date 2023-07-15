function saveData(frm, btn, pth)
{
    var formData = $("#"+frm).serialize(); 
    var submit_btn_text=$("#"+btn).html();   
    

    $.ajax({
                headers: { "X-CSRFToken": csrftoken },
                type:'post',  
                url:pth,
                data:formData,
                cache: false,
                beforeSend: function () {
               $("#"+btn).prop("disabled", true);
                $("#"+btn).html('Please wait...'); 
              },
                success:function(obj){
                console.log(obj)
               
                  },
          error : function(err)
          {
            console.log(err);
       
            
          },
          complete: function () {
                $("#"+btn).removeAttr("disabled"),jQuery("#"+btn).html(submit_btn_text); 
              }

        
    });  
}


function deleteData(pth)
{
    $.ajax({
                headers: { "X-CSRFToken": csrftoken },
                type:'delete',  
                url:pth,
                cache: false,
                success:function(obj){
                console.log(obj)
                  },
          error : function(err)
          {
            console.log(err); 
          }
    });  
}


