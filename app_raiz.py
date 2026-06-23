# 1. INSTALAÇÃO DO MOTOR WEB, GRÁFICOS (PLOTLY) E ROTEADOR CLOUDFLARE
!pip install streamlit pandas plotly -q
!wget -q -O cloudflared-linux-amd64 https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64
!chmod +x cloudflared-linux-amd64

# 2. ESCRITA AUTOMATIZADA DO CÓDIGO-FONTE (ÍNDICE RAIZ COM GRÁFICO DE TEIA)
conteudo_app = '''
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ==============================================================================
# CONFIGURAÇÃO DE PÁGINA E IDENTIDADE VISUAL EDITORIAL
# ==============================================================================
st.set_page_config(
    page_title="Índice RAIZ | IASC",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Estrutural Focado em Legibilidade e Estabilidade
st.markdown("""
    <style>
    .stApp { background-color: #FDFBF7; color: #1A1A1A; }
    h1, h2, h3 { color: #A64B2A !important; font-family: 'Georgia', serif; }
    hr { border-top: 2px solid #DCDCDC; }
    
    [data-testid="stSidebar"] {
        background-color: #1A1A1A;
        border-right: 4px solid #A64B2A;
    }
    [data-testid="stSidebar"] * { color: #FDFBF7 !important; }
    [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 { color: #D99126 !important; }
    
    .stButton>button {
        background-color: #A64B2A;
        color: #FDFBF7;
        border: none;
        border-radius: 4px;
        font-weight: bold;
        width: 100%;
        padding: 15px;
        margin-top: 20px;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #1A1A1A; color: #D99126; }
    
    .caixa-resultado {
        padding: 30px;
        border-radius: 8px;
        text-align: center;
        margin-top: 20px;
        border: 2px solid #1A1A1A;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# BARRA LATERAL
# ==============================================================================
with st.sidebar:
    st.markdown("## Instituto Amefricano de Sociologia Crítica")
    st.markdown("### Revista Amefricana")
    st.markdown("---")
    st.markdown("""
    **MÉTRICA E MATERIALISMO AMEFRICANO**
    
    A Ferramenta RAIZ transcende a mera constatação binária do fazer burocrático. Este painel materializa as proposições analíticas que desnudam o *Banzo Institucional*, exigindo que a máquina pública quantifique o seu impacto direto sobre os corpos e territórios marginalizados. 
    """)
    st.markdown("---")
    st.markdown("""
    **ESCALA DE AVALIAÇÃO:**
    * **[-1.0]** Retrocesso Ativo
    * **[-0.5]** Insuficiente / Excludente
    * **[ 0.0]** Omissão Institucional
    * **[+0.5]** Avanço Tímido
    * **[+1.0]** Transformação Radical
    """)

# ==============================================================================
# ÁREA CENTRAL
# ==============================================================================
st.markdown("<h1>ÍNDICE RAIZ: Auditoria Cívica</h1>", unsafe_allow_html=True)
st.markdown("### Mensuração Estrutural de Violência Institucional e Políticas Públicas", unsafe_allow_html=True)
st.write("A aplicação deste instrumento metodológico exige do pesquisador e do ativista uma leitura arguta da materialidade do serviço público. Avalie cada dimensão sabendo que valores negativos denunciarão o desmonte, enquanto positivos validarão o avanço estrutural contundente na reparação e redistribuição de poder.")
st.divider()

# ==============================================================================
# MATRIZ AVALIATIVA
# ==============================================================================
eixos = {
    "Eixo 1: Território e Memória": [
        ("Memória: A lei protege ativamente e fomenta a preservação de espaços de memória afro-brasileira e indígena.", 0.4),
        ("Distribuição: Os recursos e serviços previstos pela norma são distribuídos de forma rigorosamente equitativa.", 0.3),
        ("Acesso: O ato normativo elimina barreiras financeiras e burocráticas, assegurando a proximidade física de direitos.", 0.3),
        ("Capilaridade Física: A execução alcança efetivamente as áreas mais precarizadas (encostas, ruas sem asfalto, vielas).", 0.5),
        ("Capilaridade Estrutural: O Estado descentraliza operações investindo nas infraestruturas comunitárias já existentes.", 0.5)
    ],
    "Eixo 2: Corpos e Vivências": [
        ("Interseccionalidade: A legislação atende de forma resolutiva às necessidades de sujeitos na encruzilhada de vulnerabilidades.", 0.4),
        ("Proteção: A aplicação da norma protege concretamente a integridade física e mental da população racializada.", 0.3),
        ("Escuta: As demandas e percepções orgânicas da comunidade foram validadas e incorporadas de forma decisiva.", 0.3),
        ("Capilaridade Cotidiana: A mudança estrutural melhora efetivamente a exaustiva rotina diária da classe trabalhadora.", 0.5),
        ("Capilaridade Social: A norma possui mecanismos de busca ativa para proteger pessoas em extrema invisibilidade.", 0.5)
    ],
    "Eixo 3: Poder e Representação": [
        ("Participação: Lideranças comunitárias periféricas exerceram poder material de veto e alteração significativa no texto.", 0.4),
        ("Decisão: Conselhos responsáveis pela execução possuem mecanismos obrigatórios (cotas/paridade) para presença negra.", 0.3),
        ("Narrativa: Campanhas e textos oficiais constroem narrativas que valorizam a cultura marginalizada.", 0.3),
        ("Capilaridade Fiscalizadora: A norma garante financiamento de canais para moradores fiscalizarem resultados.", 0.5),
        ("Capilaridade Decisória: O Estado transfere recursos e repassa o poder de gestão para associações comunitárias.", 0.5)
    ],
    "Eixo 4: Estado e Responsabilidade": [
        ("Discricionariedade: A lei estabelece protocolos humanizados que impedem margens de interpretação preconceituosas na ponta.", 0.4),
        ("Responsabilização: Existem canais blindados que garantem punição real a servidores envolvidos em racismo.", 0.3),
        ("Formação: A norma prevê orçamento específico, contínuo e obrigatório para letramento antirracista dos servidores.", 0.3),
        ("Capilaridade Burocrática: O processo para obtenção do benefício é desburocratizado e viável para populações sem conectividade.", 0.5),
        ("Capilaridade de Infraestrutura: Os equipamentos públicos nas periferias receberam o aporte material indispensável.", 0.5)
    ],
    "Eixo 5: Conhecimento e Linguagem": [
        ("Valorização do Saber: A legislação valida, incorpora formalmente e remunera saberes e tecnologias sociais da comunidade.", 0.4),
        ("Violência Simbólica: O texto normativo e o atendimento utilizam linguagem emancipatória, abdicando de jargões.", 0.3),
        ("Transparência: A lei impõe a coleta e a divulgação transparente de dados desagregados por raça, cor, gênero e território.", 0.3),
        ("Capilaridade Comunicacional: Informações chegam à população através de meios populares (rádios, carros de som).", 0.5),
        ("Capilaridade Epistêmica: O Estado contrata lideranças da própria comunidade para implementar ações.", 0.5)
    ]
}

opcoes_escala = [
    "[-1.0] Retrocesso Ativo",
    "[-0.5] Insuficiente / Excludente",
    "[ 0.0] Omissão Institucional",
    "[+0.5] Avanço Tímido",
    "[+1.0] Transformação Radical"
]
valores_escala = [-1.0, -0.5, 0.0, 0.5, 1.0]

pontuacao_eixos = {}
pontuacao_total = 0.0

# ==============================================================================
# FORMULÁRIO ESTÁVEL
# ==============================================================================
with st.form(key='auditoria_form_final'):
    for nome_eixo, perguntas in eixos.items():
        st.markdown(f"<h3 style='color: #D99126;'>{nome_eixo}</h3>", unsafe_allow_html=True)
        score_eixo = 0.0
        
        for idx, (pergunta, peso) in enumerate(perguntas):
            st.markdown(f"**{pergunta}** *(Peso Ponderado: {peso})*")
            escolha = st.radio(
                "Selecione a avaliação normativa:",
                options=opcoes_escala,
                index=2,
                key=f"{nome_eixo}_{idx}",
                label_visibility="collapsed"
            )
            indice = opcoes_escala.index(escolha)
            score_eixo += valores_escala[indice] * peso
            st.markdown("<br>", unsafe_allow_html=True)
            
        pontuacao_eixos[nome_eixo] = score_eixo
        pontuacao_total += score_eixo
        st.divider()

    submit_button = st.form_submit_button(label="PROCESSAR AUDITORIA CÍVICA E GERAR DOSSIÊ")

# ==============================================================================
# VEREDITO E GRÁFICO DE TEIA
# ==============================================================================
if submit_button:
    st.markdown("<h2 style='text-align: center; font-size: 2.2em;'>VEREDITO INSTITUCIONAL</h2>", unsafe_allow_html=True)
    
    if pontuacao_total <= -5.0:
        cor_fundo, cor_texto, diag = "#8B0000", "#FFFFFF", "ALERTA CRÍTICO DE NECROPOLÍTICA: A normativa auditada atua como instrumento ativo de epistemicídio e exclusão territorial."
    elif -5.0 < pontuacao_total < 0.0:
        cor_fundo, cor_texto, diag = "#D99126", "#1A1A1A", "RETROCESSO INSTITUCIONAL: A lei aprofunda o racismo estrutural e opera ativamente contra as populações vulneráveis."
    elif pontuacao_total == 0.0:
        cor_fundo, cor_texto, diag = "#787878", "#FFFFFF", "INÉRCIA ABSOLUTA: A norma é paliativa e falha integralmente em alterar o status quo hegemônico da máquina estatal."
    elif 0.0 < pontuacao_total <= 5.0:
        cor_fundo, cor_texto, diag = "#FDFBF7", "#1A1A1A", "AVANÇO LIMITADO: A política traz vitórias conceituais, mas esbarra na falta de capilaridade e orçamento material."
    else:
        cor_fundo, cor_texto, diag = "#1A1A1A", "#D99126", "TRANSFORMAÇÃO RADICAL: A legislação consolida a reestruturação do poder e assegura a reparação histórica capilarizada."

    st.markdown(f"""
    <div class='caixa-resultado' style='background-color: {cor_fundo}; color: {cor_texto};'>
        <p style='margin:0; font-size: 1.2em; text-transform: uppercase;'>Score Global do Índice RAIZ</p>
        <h1 style='color: {cor_texto} !important; font-size: 3.5em; margin: 10px 0;'>{pontuacao_total:+.2f}</h1>
        <p style='font-size: 1.3em; font-weight: bold;'>{diag}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # RENDERIZAÇÃO DO GRÁFICO RADAR (TEIA)
    st.markdown("<br><h3 style='text-align: center; color: #A64B2A;'>Mapeamento Multidimensional de Impacto</h3>", unsafe_allow_html=True)
    
    categorias = [eixo.split(':')[0] for eixo in pontuacao_eixos.keys()]
    valores = list(pontuacao_eixos.values())
    categorias_loop = categorias + [categorias[0]]
    valores_loop = valores + [valores[0]]
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=valores_loop,
        theta=categorias_loop,
        fill='toself',
        fillcolor='rgba(217, 145, 38, 0.45)', # Mostarda Queimada
        line=dict(color='#A64B2A', width=3),  # Terracota
        marker=dict(color='#1A1A1A', size=8)  # Preto
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[-2.0, 2.0], tickmode='linear', dtick=1.0, gridcolor='#DCDCDC', linecolor='#1A1A1A'),
            angularaxis=dict(gridcolor='#DCDCDC', linecolor='#1A1A1A', tickfont=dict(size=14, color='#1A1A1A', family='Georgia')),
            bgcolor='#FDFBF7'
        ),
        paper_bgcolor='#FDFBF7',
        showlegend=False,
        margin=dict(t=40, b=40, l=40, r=40)
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("<br><h3>Detalhamento Numérico por Eixo</h3>", unsafe_allow_html=True)
    cols = st.columns(len(pontuacao_eixos))
    for i, (eixo, score) in enumerate(pontuacao_eixos.items()):
        nome_curto = eixo.split(':')[0]
        cols[i].metric(label=nome_curto, value=f"{score:+.2f}")
'''

with open("app_raiz.py", "w", encoding="utf-8") as f:
    f.write(conteudo_app)

# 3. ROTINA DE INICIALIZAÇÃO E ABERTURA DO TÚNEL CLOUDFLARE
import os
import time
import re

os.system("nohup streamlit run app_raiz.py > streamlit_log.txt 2>&1 &")
os.system("nohup ./cloudflared-linux-amd64 tunnel --url http://localhost:8501 > cloudflare_log.txt 2>&1 &")

print("Instalando dependências gráficas e roteando o servidor...")
time.sleep(10)

try:
    with open("cloudflare_log.txt", "r") as log_file:
        conteudo = log_file.read()
        urls = re.findall(r'https://[a-zA-Z0-9-]+\.trycloudflare\.com', conteudo)
        
        if urls:
            url_acesso = urls[-1]
            print("\n" + "="*80)
            print("🔗 LINK PÚBLICO E TEMPORÁRIO (TESTE DO GRÁFICO):")
            print(f">>> {url_acesso} <<<")
            print("="*80)
        else:
            print("\nTúnel pendente. Execute a célula novamente.")
except FileNotFoundError:
    print("O arquivo não foi gerado a tempo.")
