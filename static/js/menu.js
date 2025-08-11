// =====================#
// Lógica do Menu Sanduíche#
// =====================#

document.addEventListener('DOMContentLoaded', function() {
    'Adiciona um ouvinte de evento para o carregamento completo do DOM.'
    
    // Obtém os elementos do DOM
    const botaoMenu = document.querySelector('.bt-menu-sanduiche');
    const menuNavegacao = document.getElementById('menu-navegacao');
    const menuOverlay = document.querySelector('.menu-overlay');
    const linksDoMenu = menuNavegacao.querySelectorAll('a');

    // Função para fechar o menu
    function FecharMenu() {
        'Remove as classes necessárias para ocultar o menu e o overlay.'
        document.body.classList.remove('menu-aberto');
        botaoMenu.setAttribute('aria-expanded', 'false');
    }

    // Adiciona um evento de clique ao botão para abrir o menu
    botaoMenu.addEventListener('click', function() {
        'Adiciona as classes necessárias para exibir o menu e o overlay.'
        document.body.classList.add('menu-aberto');
        this.setAttribute('aria-expanded', 'true');
    });

    // Adiciona eventos de clique para fechar o menu
    menuOverlay.addEventListener('click', FecharMenu);
    
    // Adiciona evento de clique em cada link do menu para fechar o painel e navegar.
    linksDoMenu.forEach(link => {
        link.addEventListener('click', function(event) {
            'Fecha o menu e garante que a navegação para a âncora ocorra.'

            // Obtém o destino da âncora (ex: "#servicos")
            const destino_ancora = this.getAttribute('href');

            // Fecha o menu primeiro
            FecharMenu();

            // Espera a transição do menu terminar antes de rolar a página
            setTimeout(function() {
                // Navega para a âncora
                window.location.href = destino_ancora;
            }, 300); // 300ms, o mesmo tempo da transição CSS
        });
    });

    // Fecha o menu ao redimensionar a tela para desktop
    window.addEventListener('resize', function() {
        if (window.innerWidth > 600 && document.body.classList.contains('menu-aberto')) {
            FecharMenu();
        }
    });
});