document.getElementById("visualizar-text").onclick = function(event) {
    event.preventDefault(); 
    const descricaoInput = document.getElementById("descricao");
    const visualizacaoDiv = document.getElementById("visualizar-post-text");

    const username = document.getElementById("username").value;
    const userImage = document.getElementById("userImage").value;

    visualizacaoDiv.querySelector(".postes").innerHTML = `
        <div class="descricaoUsuario">
            <img class="user-photo" src="${userImage}" alt="Foto do Usuário">
            <h1>${username}</h1>
            <p>Data: ${new Date().toLocaleDateString()}</p>
        </div>
        <div class="postagem">
            <p>${descricaoInput.value}</p>
        </div>
    `;

    visualizacaoDiv.style.display = 'block';
};
const visualizacaoDiv = document.getElementById("visualizar-post-text");
document.querySelector(".fechar-modalText").onclick = function() {
    document.getElementById("visualizar-post-text").style.display = 'none';
};
