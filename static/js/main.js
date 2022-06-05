$(document).ready(()=>{
  const img = $("#captchaImg");
  const inputText = $("#inputText");
  $("#submit").click(()=>{
    if (inputText.val().toLowerCase()===img.data("text").toLowerCase()){
      alert("yess");
    }else {
      alert("you have -100000iq")
    }
    location.reload();
  });
});