
var botaoAbrirModalFoto = document.getElementById("visualizar-foto");

var modalFoto = document.getElementById("visualizar-post-foto");

var botaoFecharModalFoto = document.getElementsByClassName("fechar-modalFoto")[0];

botaoAbrirModalFoto.onclick = function() {
  modalFoto.style.display = "block";
}

botaoFecharModalFoto.onclick = function() {
  modalFoto.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modalFoto) {
    modalFoto.style.display = "none";
  }
}
