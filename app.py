# =====================#
# Importações#
# =====================#
from flask import Flask, render_template


# =====================#
# Configurações Iniciais#
# =====================#

# Cria uma instância da aplicação Flask.
app = Flask(__name__)

# Importa os dados dinâmicos do config.py
from config import CONFIGURACOES_DO_NEGOCIO, SERVICOS_INDIVIDUAIS, COMBOS_DE_SERVICOS


# =====================#
# Roteamento de Páginas#
# =====================#

# Define a rota para a página principal (home).
@app.route('/')
def pagina_inicial():
    '''
    Renderiza a página inicial do site.

    Retorna:
        Renderiza o template 'index.html' com as variáveis de contexto.
    '''
    # Passa todos os dados dinâmicos para o template 'index.html'.
    return render_template(
        'index.html',
        configuracoes=CONFIGURACOES_DO_NEGOCIO,
        servicos=SERVICOS_INDIVIDUAIS,
        combos=COMBOS_DE_SERVICOS
    )

# Rota para a página de serviços.
@app.route('/servicos')
def pagina_servicos():
    '''
    Renderiza a página dedicada a todos os serviços.

    Retorna:
        Renderiza o template 'servicos.html' com as variáveis de contexto.
    '''
    return render_template(
        'servicos.html',
        configuracoes=CONFIGURACOES_DO_NEGOCIO,
        servicos=SERVICOS_INDIVIDUAIS
    )

# Rota para a página de combos.
@app.route('/combos')
def pagina_combos():
    '''
    Renderiza a página dedicada aos combos.

    Retorna:
        Renderiza o template 'combos.html' com as variáveis de contexto.
    '''
    return render_template(
        'combos.html',
        configuracoes=CONFIGURACOES_DO_NEGOCIO,
        combos=COMBOS_DE_SERVICOS
    )

# Rota para a página "Sobre Nós".
@app.route('/sobre')
def pagina_sobre():
    '''
    Renderiza a página "Sobre Nós" com informações do negócio.

    Retorna:
        Renderiza o template 'sobre.html' com as variáveis de contexto.
    '''
    return render_template(
        'sobre.html',
        configuracoes=CONFIGURACOES_DO_NEGOCIO
    )

# Rota para a página de contato.
@app.route('/contato')
def pagina_contato():
    '''
    Renderiza a página de contato com um formulário simples.

    Retorna:
        Renderiza o template 'contato.html' com as variáveis de contexto.
    '''
    return render_template(
        'contato.html',
        configuracoes=CONFIGURACOES_DO_NEGOCIO
    )

# =====================#
# Execução Principal#
# =====================#

# Executa o servidor de desenvolvimento do Flask.
if __name__ == '__main__':
    app.run(debug=True)