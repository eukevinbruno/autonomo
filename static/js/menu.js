// =====================#
// Lógica do Menu Sanduíche#
// =====================#

document.addEventListener('DOMContentLoaded', function() {
    'Adiciona um ouvinte de evento para o carregamento completo do DOM.'
    
    // Obtém os elementos do DOM
    const Bt_menu_sanduiche = document.querySelector('.bt-menu-sanduiche');
    const Menu_de_navegacao = document.getElementById('menu-navegacao');
    const Overlay_do_menu = document.querySelector('.menu-overlay');
    const Links_do_menu = Menu_de_navegacao.querySelectorAll('a');

    // Função para fechar o menu
    function Fechar_menu() {
        'Remove as classes necessárias para ocultar o menu e o overlay.'
        document.body.classList.remove('menu-aberto');
        Bt_menu_sanduiche.setAttribute('aria-expanded', 'false');
    }

    // Função para abrir o menu
    function Abrir_menu() {
        'Adiciona as classes necessárias para exibir o menu e o overlay.'
        document.body.classList.add('menu-aberto');
        Bt_menu_sanduiche.setAttribute('aria-expanded', 'true');
    }

    // Adiciona evento de clique para abrir o menu
    Bt_menu_sanduiche.addEventListener('click', Abrir_menu);

    // Adiciona eventos de clique para fechar o menu
    Overlay_do_menu.addEventListener('click', Fechar_menu);
    
    // Adiciona evento de clique em cada link do menu para fechar o painel e navegar.
    Links_do_menu.forEach(link => {
        link.addEventListener('click', Fechar_menu);
    });

    // Fecha o menu ao redimensionar a tela para desktop
    window.addEventListener('resize', function() {
        if (window.innerWidth > 600 && document.body.classList.contains('menu-aberto')) {
            Fechar_menu();
        }
    });
});