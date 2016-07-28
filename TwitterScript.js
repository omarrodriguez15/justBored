//Twitter Script to remove Followers
setInterval(function(){
    t=$(".Grid .Grid--withGutter").find(".user-actions-follow-button");
    for(i=0;true;i++){
        if(i>=t.length){
            window.scrollTo(0,$(document).height());
            return
        }
        $(t[i]).trigger("click").remove()
    }
},2000);