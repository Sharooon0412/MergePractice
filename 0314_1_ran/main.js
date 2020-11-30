window.onload=function(){
   // this.document.write("Hello JavaScript!");

};

$(document).ready(function(){
    $("input").click(function(){
        //alert("Hi");
        let number0fListItem = $("#choices li").length;
        let randomChildNumber = Math.floor(Math.random()*number0fListItem);
        $("#random-result").text($("#choices li").eq(randomChildNumber).text());
        $("#random-pic").attr("src", picture[randomChildNumber]);
        //document.write("<img src='\yo\3.jpg'>");
        //$("H1").text("Hello");
    });
});