
var botaoAbrirModalText = document.getElementById("visualizar-text");

var modalText = document.getElementById("visualizar-post-text");

var botaoFecharModalText = document.getElementsByClassName("fechar-modalText")[0];

botaoAbrirModalText.onclick = function() {
  modalText.style.display = "block";
}

botaoFecharModalText.onclick = function() {
  modalText.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modalText) {
    modalText.style.display = "none";
  }
}
