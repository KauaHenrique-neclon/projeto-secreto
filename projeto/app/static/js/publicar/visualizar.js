document.getElementById("visualizar-foto").onclick = function() {
    const imageInput = document.getElementById("image");
    const descricaoInput = document.getElementById("descricao");
    const visualizacaoDiv = document.getElementById("visualizar-post-foto");

    const username = document.getElementById("username").value;
    const userImage = document.getElementById("userImage").value;

    const reader = new FileReader();
    
    reader.onload = function(e) {
        visualizacaoDiv.querySelector(".postes").innerHTML = `
            <div class="descricaoUsuario">
                <img class="user-photo" src="${userImage}" alt="Foto do Usuário">
                <h1>${username}</h1>
                <p>Data: ${new Date().toLocaleDateString()}</p>
            </div>
            <div class="postagem">
                <img src="${e.target.result}" alt="foto Usuário">
                <p>${descricaoInput.value}</p>
            </div>
        `;
    };

    if (imageInput.files.length > 0) {
        reader.readAsDataURL(imageInput.files[0]);
    }
    
    visualizacaoDiv.style.display = 'block';
};
const visualizacaoDiv = document.getElementById("visualizar-post-foto");
document.querySelector(".fechar-modalFoto").onclick = function() {
    visualizacaoDiv.style.display = 'none';
};