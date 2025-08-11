# =====================#
# Configurações do Site#
# =====================#

# Dicionário contendo as informações básicas do negócio.
# A alteração dos valores aqui refletirá em todas as páginas que os utilizam.
CONFIGURACOES_DO_NEGOCIO = {
    "nome_da_empresa": "KB Soluções de TI",
    "descricao_curta": "Seu parceiro em tecnologia para soluções rápidas e eficientes.",
    "contato_instagram": "@eukevinbruno",
    "contato_whatsapp": "5547997064430",  # Exemplo: use o formato DDI + DDD + Número.
}


# =====================#
# Dados dos Serviços#
# =====================#

# Lista de dicionários para os serviços individuais.
# Cada dicionário representa um serviço com nome, descricao e preco_sugerido.
SERVICOS_INDIVIDUAIS = [
    {
        "nome_do_servico": "Formatação do Sistema",
        "descricao_do_servico": "Instalação e ativação do Windows e Pacote Office.",
        "preco_sugerido": "R$ 100 - 150",
    },
    {
        "nome_do_servico": "Limpeza Interna Física",
        "descricao_do_servico": "Limpeza de poeira, troca de pasta térmica e organização interna.",
        "preco_sugerido": "R$ 80 - 120",
    },
    {
        "nome_do_servico": "Diagnóstico de Hardware",
        "descricao_do_servico": "Identificação de falhas e problemas em componentes do computador.",
        "preco_sugerido": "Sob consulta",
    },
    {
        "nome_do_servico": "Troca de Componentes",
        "descricao_do_servico": "Instalação de SSD, memória RAM ou outros componentes.",
        "preco_sugerido": "Sob consulta",
    },
    {
        "nome_do_servico": "Otimização de Software",
        "descricao_do_servico": "Remoção de programas indesejados, otimização de inicialização e limpeza de arquivos.",
        "preco_sugerido": "R$ 50 - 80",
    },
]


# =====================#
# Dados dos Combos#
# =====================#

# Lista de dicionários para os combos de serviços.
# Cada combo possui um nome, descricao, preco_sugerido e uma lista de beneficios inclusos.
COMBOS_DE_SERVICOS = [
    {
        "nome_do_combo": "Otimização Essencial",
        "descricao_do_combo": "Ideal para dar um gás no seu PC sem formatar.",
        "beneficios": [
            "Limpeza interna completa",
            "Troca de pasta térmica",
            "Otimização de software"
        ],
        "preco_sugerido": "R$ 150 - 200",
    },
    {
        "nome_do_combo": "PC Novo de Novo",
        "descricao_do_combo": "O pacote completo para um computador como novo.",
        "beneficios": [
            "Formatação completa",
            "Limpeza interna completa",
            "Otimização de software"
        ],
        "preco_sugerido": "R$ 200 - 280",
    },
    {
        "nome_do_combo": "Manutenção Total",
        "descricao_do_combo": "A solução definitiva para segurança e desempenho.",
        "beneficios": [
            "Tudo do combo 'PC Novo de Novo'",
            "Instalação de antivírus",
            "Configuração de rotina de backup"
        ],
        "preco_sugerido": "R$ 250 - 350",
    },
]