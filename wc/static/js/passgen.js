var passwordlength = 8;
document.getElementById("size").value =passwordlength;
function buttonclickup(){
    passwordlength ++;
    document.getElementById("size").value =passwordlength;
}
function buttonclickdown(){
  passwordlength --;
  document.getElementById("size").value =passwordlength;
  if(passwordlength <6){
    alert("Password Length Should Be Minimum 6 value");
  }
}
function getpassword(){
    var chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_-+=?|<>{}[]:";
    var newpassword="";
    for(var i =0;i<passwordlength;i++){
      var randnum = Math.floor(Math.random()*chars.length);
      newpassword += chars[randnum];
    }
    if (passwordlength<6) {
      alert("Password Length Should Be Minimum 6 value");
    }
    document.getElementById("show").value = newpassword;
  }
  function clicked(){
    var copytext =document.getElementById("show");
    copytext.select();
    copytext.setSelectionRange(0,99999);
    document.execCommand("copy");
  }