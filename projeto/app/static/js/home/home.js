
var botaoAbrirModal = document.getElementById("comentario");

var modal = document.getElementById("modal-comentarios");

var botaoFecharModal = document.getElementsByClassName("fechar-modal")[0];

botaoAbrirModal.onclick = function() {
  modal.style.display = "block";
}

botaoFecharModal.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
