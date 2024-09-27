document.addEventListener('DOMContentLoaded', () => {
    const adicionarCampos = document.getElementById('adicionar-campo');
    const camposContainer = document.getElementById('campos-container');

    let index = 1;

    
    adicionarCampos.addEventListener('click', () => {
        const campoDiv = document.createElement('div');
        campoDiv.className = 'campo';
        campoDiv.id = `campo-${index}`

        campoDiv.innerHTML = `
                    <input type="text" class="titulo-campo-form" name="campos-${index}-titulo_campo" placeholder="Título do Campo" required>
                    <select name="campos-${index}-tipo_resposta" class="caixa-selecao" required>
                        <option value="resposta_curta">Resposta Curta</option>
                        <option value="resposta_longa">Resposta Longa</option>
                        <option value="multi_escolha">Múltipla Escolha</option>
                        <option value="caixa_selecao">Caixa de Seleção</option>
                    </select>
                    <div id="resposta-container-${index}">
                        <input class="campo-resposta" type="text" name="resposta-${index}" placeholder="Digite sua resposta aqui" disabled>
                    </div>
                    <button type="button" class="del-campo" onclick="deletarCampo(${index})">Deletar Campo</button>
                
        `;
        camposContainer.appendChild(campoDiv);
        index++;
    });
    
    window.deletarCampo = (campoIndex) => {
        const campo = document.getElementById(`campo-${campoIndex}`);
        if (campo) {
            campo.remove();
        } else {
            console.error(`Campo com ID 'campo-${campoIndex}' não encontrado.`);
        }
    };
});
