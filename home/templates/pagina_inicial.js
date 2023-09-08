// by Clécio, duvidas é só chamar e perguntar


// capturar os eventos de click nos itens e deixar o ckeditor vazio
document.addEventListener('DOMContentLoaded', function () {
    // Inicializar o CKEditor no campo 'conteudo_atividade'
    CKEDITOR.replace('conteudo_atividade', { height: '60vh' });

    // Capturar o evento de clique nos botões de atividade
    const botoesAtividade = document.querySelectorAll('.pastel-button3');
    botoesAtividade.forEach(function (botao) {
        botao.addEventListener('click', function () {
            const conteudoAtividade = botao.getAttribute('data-conteudo'); // Conteúdo da atividade
            if (conteudoAtividade == 'None') { // FUNCIONANDO!!!!!!!! Deixando o CKeditor vazio caso não tenha nada de texto, antes ele colocava um "None"
                CKEDITOR.instances.conteudo_atividade.setData('');
            } else {
                CKEDITOR.instances.conteudo_atividade.setData(conteudoAtividade); // Atualizar o CKEditor
            }


            const listaId = botao.getAttribute('data-item-id'); // Obtém o ID da lista
            document.getElementById('item_id').value = listaId; // Define o valor do campo oculto
            document.getElementById('object_type').value = 'atividade';
        });
    });

    // Capturar o evento de clique nos botões de lista
    const botoesLista = document.querySelectorAll('.pastel-button2');
    botoesLista.forEach(function (botao) {
        botao.addEventListener('click', function () {
            const conteudoLista = botao.getAttribute('data-conteudo'); // Conteúdo da lista
            if (conteudoLista == 'None') {
                CKEDITOR.instances.conteudo_atividade.setData('');
            } else {
                CKEDITOR.instances.conteudo_atividade.setData(conteudoLista); // Atualizar o CKEditor
            }


            const listaId = botao.getAttribute('data-item-id'); // Obtém o ID da lista
            document.getElementById('item_id').value = listaId; // Define o valor do campo oculto
            document.getElementById('object_type').value = 'lista';
        });
    });

    // Capturar o evento de clique nos botões de tarefa
    const botoesTarefa = document.querySelectorAll('.pastel-button4');
    botoesTarefa.forEach(function (botao) {
        botao.addEventListener('click', function () {
            const conteudoTarefa = botao.getAttribute('data-conteudo'); // Conteúdo da tarefa
            if (conteudoTarefa == 'None') {
                CKEDITOR.instances.conteudo_atividade.setData('');
            } else {
                CKEDITOR.instances.conteudo_atividade.setData(conteudoTarefa); // Atualizar o CKEditor
            }

            const listaId = botao.getAttribute('data-item-id'); // Obtém o ID da lista
            document.getElementById('item_id').value = listaId; // Define o valor do campo oculto
            document.getElementById('object_type').value = 'tarefa';
        });
    });
});


// ------------------------------------------------------------------------------------------

// Script JS para manter o texto no editor...  (tipo, se estiver navegando na hierarquia o texto do item selecionado continua ai)
const editorTextarea = document.getElementById('conteudo_atividade');
const itemButtons = document.querySelectorAll('[data-conteudo]');

itemButtons.forEach(button => {
    button.addEventListener('click', () => {
        const conteudo = button.getAttribute('data-conteudo');
        if (conteudo == 'None') {
            editorTextarea.value = '';
        } else {
            editorTextarea.value = conteudo;
        }

    });
});



// ------------------------------------------------------------------------------------------

// Para mudar a cor do botao em aberto 

// Desatualizada, agora eu mudo a propria row e seus botoes, nao os botoes separados
// let listaAberta = null; // Armazena o botão da lista aberta anteriormente

// function marcarListaAberta(botao) {
//     if (listaAberta !== null) {
//         listaAberta.classList.remove('lista-aberta'); // Remove a classe da lista aberta anterior
//     }

//     listaAberta = botao; // Atualiza o botão da lista aberta
//     botao.classList.add('lista-aberta'); // Adiciona a classe à lista aberta atual
// }

//

let listaAbertarow = null; // Armazena o botão da lista aberta anteriormente

function marcarListaAbertarow(botao) {
    mostrarCKEditor(); // chamando a func para mostrar o editor
    if (listaAbertarow !== null) {
        listaAbertarow.classList.remove('lista-aberta-row'); // Remove a classe da lista aberta anterior
        
    }


    listaAbertarow = botao; // Atualiza o botão da lista aberta
    botao.classList.add('lista-aberta-row'); // Adiciona a classe à lista aberta atual
}

// -------------------------------------------------------------------------------------------


// script para capturar o ID da lista quando for criar atividade... foda 

document.addEventListener('DOMContentLoaded', function () {
    const botoesCriarAtividade = document.querySelectorAll('.btn-criar-atividade');

    botoesCriarAtividade.forEach(function (botao) {
        botao.addEventListener('click', function () {
            const listaID = botao.getAttribute('data-lista-id');
            document.getElementById('lista_id').value = listaID;
        });
    });
});

// Captura o evento de clique no botão "Criar Tarefa"
document.querySelectorAll('.btn-criar-tarefa').forEach(function (button) {
    button.addEventListener('click', function (event) {
        // Obtém o ID da atividade associado ao botão clicado
        var atividadeId = button.getAttribute('data-atividade-id');

        // Preenche o campo oculto "atividade_id" no formulário do modal
        document.getElementById('atividade_id').value = atividadeId;
    });
});

//     FIM DOS SCRIPTS PARA PEGAR O ID NA HORA DE CRIAR LISTAS, ATIVIDADES OU TAREFAS            

// ----------------------------------------------------------------------------------------------


// func para deletar um item

function deletarItem(item) {
    const objectType = item.getAttribute('data-object-type');
    const itemId = item.getAttribute('data-item-id');

    const confirmation = confirm('Tem certeza que deseja realizar a exclusão?');

    if (confirmation) {
        const objectTypeInput = document.getElementById('objectTypeInput');
        const itemIdInput = document.getElementById('itemIdInput');

        objectTypeInput.value = objectType;
        itemIdInput.value = itemId;

        // Submit the form
        document.getElementById('deleteForm').submit();
    }
}

// ----------------------------------------------------------------------------------------------

// Isso aqui é pra abrir o modal de att já com os dados do item
function atualizarItem(item) {
    // Obtenha os dados do item a partir dos atributos data-
    const objectType = item.getAttribute('data-object-type');
    const itemId = item.getAttribute('data-item-id');
    const nomeTarefa = item.getAttribute('data-nome-tarefa');
    const descricao = item.getAttribute('data-descricao');
    const dataInicio = item.getAttribute('data-data-inicio');
    const dataFim = item.getAttribute('data-data-fim');
    const prioridade = item.getAttribute('data-prioridade');

    //console.log('Data de Início:', dataInicio);    //       SHIT!!

    let dataInicioFormatada = '';
    let dataFimFormatada = '';
    
    if (dataFim == 'None') {
        dataFimFormatada = dataFim;
    } else {
        dataFimFormatada = formatarData(dataFim);
    }
    
    if (dataInicio == 'None') {
        dataInicioFormatada = dataInicio;
    } else {
        dataInicioFormatada = formatarData(dataInicio);
    }
    
    const atualizarModal = new bootstrap.Modal(document.getElementById('atualizarModal'));
    // Preencha os campos do formulário de atualização com os dados do item
    document.getElementById('updateObjectTypeInput').value = objectType;
    document.getElementById('updateItemIdInput').value = itemId;
    document.getElementById('nome_tarefaatt').value = nomeTarefa; // POHA VELHO, ERA SÓ MUDAR O NOME DO ELEMENTO Pro CODE NAO CONFUNDIR COM OUTRO MODAL
    document.getElementById('descricaoatt').value = descricao;
    document.getElementById('dataInicioatt').value = dataInicioFormatada;
    document.getElementById('dataFimatt').value = dataFimFormatada;
    document.getElementById('prioridadeatt').value = prioridade;

    // Abre o modal de atualização
    atualizarModal.show();
}

// formatacao... ele pega a data como string none, e nao no formato que deviar ser AAAA-MM-DD
function formatarData(data) {
    const partesData = data.split(' '); // Divide a data em partes
    const mes = partesData[0]; // Obtém o mês
    const dia = partesData[1].replace(',', ''); // Obtém o dia (removendo a vírgula)
    const ano = partesData[2]; // Obtém o ano

    // Mapeia os nomes dos meses em inglês para números de mês
    const meses = {
        'Jan.': '01',
        'Feb.': '02',
        'Mar.': '03',
        'Apr.': '04',
        'May': '05',
        'Jun.': '06',
        'Jul.': '07',
        'Aug.': '08',
        'Sept.': '09',
        'Oct.': '10',
        'Nov.': '11',
        'Dec.': '12'
    };

    // Obtém o número do mês formatado
    const numeroMes = meses[mes];

    // Formata a data como "AAAA-MM-DD"
    const dataFormatada = `${ano}-${numeroMes}-${dia}`;

    return dataFormatada;
}

// ... foda


// -----------------------------------------------------------------

// SCRIPT PARA O CLIQUE DIREITO: ESSA VAI CHAMAR O MENU CONTEXTO (ABAIXO)

// Seletor para os elementos que terão o menu de contexto (por exemplo, os botões de lista, atividade e tarefa)
const itemButton = document.querySelectorAll('.pastel-button2, .pastel-button3, .pastel-button4');

itemButton.forEach(button => {
    button.addEventListener('contextmenu', function (event) {
        event.preventDefault(); // Evitar o menu de contexto padrão do navegador

        // Mostrar o menu de contexto personalizado
        mostrarMenuContexto(event.clientX, event.clientY, button);
    });
});


// FUNÇÃO QUE CRIA OS BUTÕES DE MENU CONTEXTO (CLIQUE DIREITO)

function mostrarMenuContexto(x, y, item) {
    const menuExistente = document.querySelector('.context-menu'); // caso ja tenha um menu, apaga ele
    if (menuExistente) {
        menuExistente.remove();
    }

    const menu = document.createElement('div');
    menu.classList.add('context-menu');
    menu.style.position = 'absolute';
    menu.style.left = `${x}px`;
    menu.style.top = `${y}px`;

    const deleteButton = document.createElement('button');
    deleteButton.textContent = 'Deletar';
    deleteButton.classList.add('context-menu-item');
    deleteButton.addEventListener('click', function () {
        // Chame a função de exclusão passando o item como parâmetro
        deletarItem(item);
        menu.remove(); // Remova o menu após o clique
    });

    const updateButton = document.createElement('button');
    updateButton.textContent = 'Atualizar';
    updateButton.classList.add('context-menu-item');
    updateButton.addEventListener('click', function () {
        // Chame a função de atualização passando o item como parâmetro
        atualizarItem(item);
        menu.remove(); // Remova o menu após o clique
    });

    menu.appendChild(updateButton);
    menu.appendChild(deleteButton);
    document.body.appendChild(menu);

    // Adicionar event listener de clique ao documento para fechar o menu quando o usuário clicar fora dele
    document.addEventListener('click', function (event) {
        const clickedElement = event.target;
        if (!menu.contains(clickedElement) && !item.contains(clickedElement)) {
            menu.remove(); // Remova o menu se o clique não estiver dentro dele nem no botão
        }
    });
}


// --------------------------------------------------------------


// Func pra checar se tem algum item aberto


// Função para mostrar a mensagem de boas-vindas e ocultar o CKEditor
function mostrarMensagemBoasVindas() {
    document.getElementById('boasVindas').style.display = 'block';
    document.getElementById('ckeditor-id').style.display = 'none';
    document.getElementById('divCalendario').style.display = 'none';
}

// Função para mostrar o CKEditor e ocultar a mensagem de boas-vindas
function mostrarCKEditor() {
    document.getElementById('boasVindas').style.display = 'none';
    document.getElementById('ckeditor-id').style.display = 'block';
    document.getElementById('divCalendario').style.display = 'none';
}

// func para mostrar o calendario
function mostrarDiv(botao) {
    var div = document.getElementById('divCalendario');
    div.style.display = 'block';
    document.getElementById('boasVindas').style.display = 'none';
    document.getElementById('ckeditor-id').style.display = 'none';

    inicializarCalendario();
}

// // Obtém o botão por ID
// var botaocal = document.getElementById('mostrarCalendarioBtn');

// // Adiciona um ouvinte de evento de clique ao botão
// botaocal.addEventListener('click', function () {
//     mostrarDiv(this); // Passa o próprio botão como parâmetro
// });


// -------------------------------------------------------------------------------

// Função para exibir a data atual no formato desejado
function exibirDataAtual() {
    const dataAtual = new Date();
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    const dataFormatada = dataAtual.toLocaleDateString('pt-BR', options);
    document.getElementById('dataAtual').textContent = dataFormatada;
}

// Chamando a função para exibir a data atual quando a página for carregada
document.addEventListener('DOMContentLoaded', exibirDataAtual);


// ----------------------------------------------------------------------------


// Função para chamar o calendario

function inicializarCalendario() {
    var calendarEl = document.getElementById('calendario');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',

        events: criarEventosAPartirDeAtividades(),
        locale: 'pt-br' // Configurar o idioma para português do Brasil
    });
    calendar.render();
}


function criarEventosAPartirDeAtividades() {
    const eventos = [];

    // Função para criar um evento a partir de um elemento com atributos de dados
    function criarEvento(elemento) {
        const nome = elemento.getAttribute('data-nome-tarefa');
        const dataInicio = elemento.getAttribute('data-data-inicio');
        const dataFim = elemento.getAttribute('data-data-fim');
        let dataInicioFormatada = '';
        let dataFimFormatada = '';
        let cor = '';

        const tipoItem = elemento.getAttribute('data-object-type');
        if (tipoItem === 'atividade') {
            cor = '#444444'; 
        } else if (tipoItem === 'lista') {
            cor = '#646464'; 
        } else if (tipoItem === 'tarefa') {
            cor = '#262626'; 
        }

        if (nome && dataInicio && dataFim) {
            if (dataFim == 'None') {
                dataFimFormatada = dataFim;
            } else {
                dataFimFormatada = formatarData(dataFim);
            }
            
            if (dataInicio == 'None') {
                dataInicioFormatada = dataInicio;
            } else {
                dataInicioFormatada = formatarData(dataInicio);
            }

            console.log(nome);
            console.log(dataInicioFormatada);
            console.log(dataFimFormatada);

            eventos.push({
                title: nome,
                start: dataInicioFormatada,
                end: dataFimFormatada,
                color: cor // Defina a cor do evento
            });
        }
    }

    // Percorra as atividades e crie eventos
    const atividades = document.querySelectorAll('[data-object-type="atividade"]');
    atividades.forEach(criarEvento);

    // Percorra as listas e crie eventos
    const listas = document.querySelectorAll('[data-object-type="lista"]');
    listas.forEach(criarEvento);

    // Percorra as tarefas e crie eventos
    const tarefas = document.querySelectorAll('[data-object-type="tarefa"]');
    tarefas.forEach(criarEvento);

    return eventos;
}
