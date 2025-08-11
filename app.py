# =====================#
# Importações#
# =====================#
from flask import Flask, render_template
from config import CONFIGURACOES_DO_NEGOCIO, SERVICOS_INDIVIDUAIS, COMBOS_DE_SERVICOS


# =====================#
# Configurações Iniciais#
# =====================#

# Cria uma instância da aplicação Flask.
app = Flask(__name__)

# =====================#
# Roteamento de Páginas#
# =====================#

# Define a rota para a página principal (home).
@app.route('/')
def pagina_inicial():
    '''
    Renderiza a página inicial do site.

    Passa os dados dinâmicos do negócio, serviços e combos para o template.

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


# =====================#
# Execução Principal#
# =====================#

# Executa o servidor de desenvolvimento do Flask.
# O modo de debug é ativado para facilitar o desenvolvimento.
if __name__ == '__main__':
    app.run(debug=True)