var publicarFotos = document.getElementById("fotos")
var buttonPublicarFotos = document.getElementById("buttonPublicarFoto")
var publicarText = document.getElementById("text");
var buttonPublicarText = document.getElementById("buttoPublicarText");

buttonPublicarFotos.addEventListener("click",function(){
    var publicarFotos = document.getElementById("fotos")
    if(publicarFotos.style.display === "block"){
        publicarFotos.style.display = "block"
    }else{
        publicarFotos.style.display = "block"
        publicarText.style.display = "none"
    }
})
buttonPublicarText.addEventListener("click",function(){
    var publicarText = document.getElementById("text")
    if(publicarText.style.display === "block"){
        publicarText.style.display = "block"
    }else{
        publicarText.style.display = "block"
        publicarFotos.style.display = "none"
    }
})