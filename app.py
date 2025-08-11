import streamlit as st
import json
import time
from typing import Dict, Any
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="Jornada Interativa - Fundamentos Financeiros",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado para melhorar a aparência
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Poppins:wght@300;400;500;600;700;800&display=swap');
    
    .main-header {
        font-family: 'Poppins', sans-serif;
        font-size: 3rem;
        font-weight: 700;
        color: #F59E0B;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .module-card {
        background: linear-gradient(135deg, #065F46 0%, #047857 100%);
        border: 2px solid #F59E0B;
        border-radius: 1rem;
        padding: 1.5rem;
        margin: 1rem 0;
        color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .module-title {
        font-family: 'Poppins', sans-serif;
        font-size: 1.5rem;
        font-weight: 600;
        color: #F59E0B;
        margin-bottom: 0.5rem;
    }
    
    .module-description {
        font-family: 'Inter', sans-serif;
        font-size: 1rem;
        line-height: 1.6;
        color: #D1D5DB;
        margin-bottom: 1rem;
    }
    
    .level-badge {
        background-color: rgba(245, 158, 11, 0.2);
        color: #FCD34D;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .stats-container {
        background: rgba(0, 0, 0, 0.3);
        border: 2px solid rgba(245, 158, 11, 0.3);
        border-radius: 1rem;
        padding: 2rem;
        margin: 2rem 0;
        text-align: center;
    }
    
    .stat-item {
        display: inline-block;
        margin: 0 2rem;
        text-align: center;
    }
    
    .stat-value {
        font-family: 'Poppins', sans-serif;
        font-size: 2rem;
        font-weight: 700;
        color: #F59E0B;
    }
    
    .stat-label {
        font-family: 'Inter', sans-serif;
        font-size: 0.875rem;
        color: #D1D5DB;
        margin-top: 0.5rem;
    }
    
    .welcome-section {
        background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.7)), 
                    url('https://images.unsplash.com/photo-1553729459-efe14ef6055d?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
        background-size: cover;
        background-position: center;
        border-radius: 1rem;
        padding: 3rem;
        margin: 2rem 0;
        text-align: center;
        color: white;
    }
    
    .welcome-title {
        font-family: 'Poppins', sans-serif;
        font-size: 2.5rem;
        font-weight: 700;
        color: #F59E0B;
        margin-bottom: 1.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
    }
    
    .welcome-text {
        font-family: 'Inter', sans-serif;
        font-size: 1.125rem;
        line-height: 1.6;
        margin-bottom: 2rem;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }
    
    .neuro-insight {
        background: rgba(245, 158, 11, 0.1);
        border-left: 4px solid #F59E0B;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin: 1.5rem 0;
    }
    
    .neuro-title {
        font-family: 'Poppins', sans-serif;
        font-size: 1.25rem;
        font-weight: 600;
        color: #F59E0B;
        margin-bottom: 0.75rem;
    }
    
    .exercise-container {
        background: rgba(17, 24, 39, 0.5);
        border: 1px solid rgba(245, 158, 11, 0.2);
        border-radius: 0.5rem;
        padding: 1.5rem;
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Dados dos módulos
MODULES_DATA = [
    {
        "id": 1,
        "title": "Linguagem Financeira",
        "icon": "📚",
        "level": "FUNDAMENTAL",
        "description": "Domine o vocabulário essencial dos negócios e desenvolva fluência na interpretação de demonstrações financeiras.",
        "content": {
            "title": "Módulo 1: Linguagem Financeira Fundamental",
            "neuro_insight": "Este módulo ativa simultaneamente as áreas de Broca (processamento linguístico), córtex pré-frontal (análise lógica) e hipocampo (formação de memórias), criando uma rede neural robusta para compreensão financeira.",
            "introduction": "Assim como um fazendeiro possui terras, equipamentos e colheitas, uma empresa possui recursos que geram valor futuro. Este módulo ensina o idioma básico das finanças.",
            "details": [
                "Ativos: Recursos de Valor. São todos os bens e direitos controlados pela empresa.",
                "Passivos: Obrigações Assumidas. Representam as dívidas e compromissos da empresa.",
                "Patrimônio Líquido: O capital próprio da empresa, a diferença entre Ativos e Passivos."
            ],
            "exercise": {
                "type": "classification",
                "title": "Exercício de Fixação Neural",
                "introduction": "Classifique os itens abaixo como Ativo ou Passivo para fortalecer suas conexões neurais.",
                "items": [
                    {"text": "💻 Computadores da empresa", "answer": "ativo"},
                    {"text": "🏦 Empréstimo bancário", "answer": "passivo"},
                    {"text": "💰 Dinheiro em conta corrente", "answer": "ativo"},
                    {"text": "🧾 Contas a pagar para fornecedores", "answer": "passivo"}
                ]
            }
        }
    },
    {
        "id": 2,
        "title": "Análise Patrimonial",
        "icon": "⚖️",
        "level": "INTERMEDIÁRIO",
        "description": "Desvende a estrutura patrimonial das empresas e aprenda técnicas de análise vertical e horizontal.",
        "content": {
            "title": "Módulo 2: Análise Patrimonial Estratégica",
            "neuro_insight": "Este módulo estimula o córtex parietal (processamento espacial) e o córtex pré-frontal dorsolateral (análise comparativa), desenvolvendo a capacidade de 'visualizar' estruturas patrimoniais complexas.",
            "introduction": "Vamos aprofundar nossa análise, aprendendo a interpretar a 'fotografia' financeira de uma empresa e a simular cenários para entender seu impacto.",
            "details": [
                "Análise Vertical e Horizontal: Ferramentas para entender a composição e a evolução do patrimônio.",
                "Indicadores de Liquidez: Medem a capacidade da empresa de pagar suas contas de curto prazo.",
                "Capital de Giro: O 'fôlego' financeiro para as operações do dia a dia."
            ]
        }
    },
    {
        "id": 3,
        "title": "Performance & Rentabilidade",
        "icon": "📈",
        "level": "AVANÇADO",
        "description": "Analise a capacidade de geração de valor e desenvolva competências em modelagem de cenários.",
        "content": {
            "title": "Módulo 3: Performance e Rentabilidade",
            "neuro_insight": "Este módulo estimula o núcleo accumbens (centro de recompensa) e o córtex orbitofrontal (tomada de decisão), criando associações positivas com análise de performance financeira.",
            "introduction": "Agora vamos medir o sucesso. Os indicadores de rentabilidade mostram o quão eficientemente uma empresa transforma seus recursos em lucro.",
            "details": [
                "Margem de Lucro: O percentual de cada venda que se transforma em lucro.",
                "ROE (Retorno sobre Patrimônio): Mede o retorno que os sócios obtêm sobre seu capital investido."
            ]
        }
    },
    {
        "id": 4,
        "title": "Síntese e Aplicação",
        "icon": "🎯",
        "level": "ESTRATÉGICO",
        "description": "Aplique todo o conhecimento em um desafio final, consolidando sua expertise financeira.",
        "content": {
            "title": "Módulo 4: Síntese e Aplicação Estratégica",
            "neuro_insight": "Este módulo integra todas as áreas cerebrais trabalhadas anteriormente, criando uma rede neural consolidada para tomada de decisões financeiras estratégicas.",
            "introduction": "Chegou o momento de aplicar todo o conhecimento adquirido. Este módulo final consolida sua jornada de aprendizado.",
            "details": [
                "Integração de Conceitos: Conecte todos os conhecimentos adquiridos.",
                "Análise Estratégica: Desenvolva visão sistêmica dos negócios.",
                "Tomada de Decisão: Aplique os conceitos em situações reais."
            ]
        }
    }
]

# Inicialização do estado da sessão
if 'journey_started' not in st.session_state:
    st.session_state.journey_started = False
if 'completed_modules' not in st.session_state:
    st.session_state.completed_modules = set()
if 'stats' not in st.session_state:
    st.session_state.stats = {
        'sinapses': 0,
        'insights': 0,
        'aplicacoes': 0
    }
if 'current_module' not in st.session_state:
    st.session_state.current_module = None

def show_welcome_section():
    """Exibe a seção de boas-vindas"""
    st.markdown("""
    <div class="welcome-section">
        <h2 class="welcome-title">🌾 O Despertar da Inteligência Financeira</h2>
        <div class="welcome-text">
            <p>Assim como o Espantalho descobriu que sempre possuiu a inteligência que buscava, você está prestes a despertar competências financeiras que transformarão sua visão sobre o mundo dos negócios.</p>
        </div>
        <div class="neuro-insight">
            <h4 class="neuro-title">🧠 Neurociência Aplicada</h4>
            <p>Cada elemento desta jornada ativa múltiplas áreas cerebrais, criando conexões neurais robustas para facilitar a compreensão e aplicação prática dos conceitos.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 INICIAR JORNADA", type="primary", use_container_width=True):
            st.session_state.journey_started = True
            st.rerun()

def show_module_card(module):
    """Exibe um card de módulo"""
    completed = module["id"] in st.session_state.completed_modules
    completion_icon = "✅" if completed else ""
    
    st.markdown(f"""
    <div class="module-card">
        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div style="flex: 1;">
                <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                    <span style="font-size: 2rem; margin-right: 1rem;">{module["icon"]}</span>
                    <h3 class="module-title">{module["title"]}</h3>
                    {f'<span style="font-size: 1.5rem; margin-left: 1rem;">{completion_icon}</span>' if completed else ''}
                </div>
                <p class="module-description">{module["description"]}</p>
                <span class="level-badge">{module["level"]}</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button(f"Abrir {module['title']}", key=f"open_{module['id']}", use_container_width=True):
        st.session_state.current_module = module["id"]
        st.rerun()

def show_stats():
    """Exibe as estatísticas de gamificação"""
    st.markdown("""
    <div class="stats-container">
        <h3 style="color: #F59E0B; font-family: 'Poppins', sans-serif; margin-bottom: 2rem;">🏆 Conquistas Neurocientíficas</h3>
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap;">
            <div class="stat-item">
                <div style="font-size: 3rem;">🧠</div>
                <div class="stat-value">{}</div>
                <div class="stat-label">Sinapses Ativas</div>
            </div>
            <div class="stat-item">
                <div style="font-size: 3rem;">⚡</div>
                <div class="stat-value">{}</div>
                <div class="stat-label">Insights Gerados</div>
            </div>
            <div class="stat-item">
                <div style="font-size: 3rem;">🎯</div>
                <div class="stat-value">{}</div>
                <div class="stat-label">Aplicações Práticas</div>
            </div>
        </div>
    </div>
    """.format(
        st.session_state.stats['sinapses'],
        st.session_state.stats['insights'],
        st.session_state.stats['aplicacoes']
    ), unsafe_allow_html=True)

def show_module_content(module_id):
    """Exibe o conteúdo detalhado de um módulo"""
    module = next((m for m in MODULES_DATA if m["id"] == module_id), None)
    if not module:
        return
    
    content = module["content"]
    
    # Cabeçalho do módulo
    col1, col2 = st.columns([1, 10])
    with col1:
        if st.button("← Voltar"):
            st.session_state.current_module = None
            st.rerun()
    
    with col2:
        st.markdown(f"""
        <h1 style="color: #F59E0B; font-family: 'Poppins', sans-serif;">
            {module["icon"]} {content["title"]}
        </h1>
        """, unsafe_allow_html=True)
    
    # Insight neurocientífico
    st.markdown(f"""
    <div class="neuro-insight">
        <h4 class="neuro-title">🧠 Insight Neurocientífico</h4>
        <p>{content["neuro_insight"]}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Introdução
    st.markdown(f"**Introdução:** {content['introduction']}")
    
    # Detalhes
    st.markdown("**Conceitos Fundamentais:**")
    for detail in content["details"]:
        st.markdown(f"• {detail}")
    
    # Exercício (se disponível)
    if "exercise" in content and content["exercise"]["type"] == "classification":
        show_classification_exercise(content["exercise"], module_id)
    
    # Simulador de liquidez para módulo 2
    if module_id == 2:
        show_liquidity_simulator()
    
    # Simulador de rentabilidade para módulo 3
    if module_id == 3:
        show_profitability_simulator()
    
    # Botão de conclusão
    completed = module_id in st.session_state.completed_modules
    if not completed:
        if st.button(f"✅ Marcar {module['title']} como Concluído", type="primary"):
            st.session_state.completed_modules.add(module_id)
            st.session_state.stats['sinapses'] += 1
            st.success(f"Parabéns! Você concluiu o {module['title']}!")
            time.sleep(1)
            st.rerun()
    else:
        st.success(f"✅ {module['title']} concluído!")

def show_classification_exercise(exercise, module_id):
    """Exibe exercício de classificação"""
    st.markdown(f"""
    <div class="exercise-container">
        <h4 style="color: #F59E0B; font-family: 'Poppins', sans-serif;">{exercise["title"]}</h4>
        <p>{exercise["introduction"]}</p>
    </div>
    """, unsafe_allow_html=True)
    
    for i, item in enumerate(exercise["items"]):
        st.markdown(f"**{item['text']}**")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Ativo", key=f"ativo_{module_id}_{i}"):
                if item["answer"] == "ativo":
                    st.success("✅ Correto!")
                    st.session_state.stats['insights'] += 1
                else:
                    st.error("❌ Incorreto. Tente novamente!")
        
        with col2:
            if st.button("Passivo", key=f"passivo_{module_id}_{i}"):
                if item["answer"] == "passivo":
                    st.success("✅ Correto!")
                    st.session_state.stats['insights'] += 1
                else:
                    st.error("❌ Incorreto. Tente novamente!")

def show_liquidity_simulator():
    """Exibe simulador de liquidez para o módulo 2"""
    st.markdown("""
    <div class="exercise-container">
        <h4 style="color: #F59E0B; font-family: 'Poppins', sans-serif;">🧪 Laboratório de Análise de Liquidez</h4>
        <p>Experimente diferentes cenários e observe como mudanças patrimoniais afetam os indicadores.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        ativo_circulante = st.slider("Ativo Circulante (R$ mil)", 100, 1000, 500)
        passivo_circulante = st.slider("Passivo Circulante (R$ mil)", 50, 800, 300)
    
    with col2:
        # Cálculos
        liquidez_corrente = ativo_circulante / passivo_circulante if passivo_circulante > 0 else 0
        capital_giro = ativo_circulante - passivo_circulante
        
        # Interpretação da liquidez
        if liquidez_corrente >= 1.5:
            status = "✅ Situação financeira saudável"
            color = "green"
        elif liquidez_corrente >= 1.0:
            status = "⚠️ Situação financeira de atenção"
            color = "orange"
        else:
            status = "❌ Situação financeira preocupante"
            color = "red"
        
        st.metric("Liquidez Corrente", f"{liquidez_corrente:.2f}")
        st.metric("Capital de Giro", f"R$ {capital_giro:,.0f} mil")
        st.markdown(f"<p style='color: {color}; font-weight: bold;'>{status}</p>", unsafe_allow_html=True)
        
        # Gráfico
        fig = go.Figure(data=[
            go.Bar(name='Ativo Circulante', x=['Recursos'], y=[ativo_circulante], marker_color='green'),
            go.Bar(name='Passivo Circulante', x=['Obrigações'], y=[passivo_circulante], marker_color='red')
        ])
        fig.update_layout(title="Comparação Ativo vs Passivo Circulante", yaxis_title="Valor (R$ mil)")
        st.plotly_chart(fig, use_container_width=True)

def show_profitability_simulator():
    """Exibe simulador de rentabilidade para o módulo 3"""
    st.markdown("""
    <div class="exercise-container">
        <h4 style="color: #F59E0B; font-family: 'Poppins', sans-serif;">🎮 Simulador de Estratégias de Rentabilidade</h4>
        <p>Ajuste os parâmetros e observe como diferentes estratégias afetam a rentabilidade.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        estrategia = st.selectbox("Estratégia de Preços", [
            "Competitivo (padrão)",
            "Premium (+20% preço, -10% volume)",
            "Penetração (-15% preço, +25% volume)"
        ])
        
        eficiencia = st.slider("Eficiência Operacional (%)", 80, 120, 100)
    
    with col2:
        # Cálculos baseados na estratégia
        receita_base = 1000000
        custo_base = 700000
        
        if "Premium" in estrategia:
            mult_receita = 1.2 * 0.9  # +20% preço, -10% volume
        elif "Penetração" in estrategia:
            mult_receita = 0.85 * 1.25  # -15% preço, +25% volume
        else:
            mult_receita = 1.0
        
        receita = receita_base * mult_receita
        custo = custo_base * (eficiencia / 100)
        lucro = receita - custo
        margem = (lucro / receita) * 100 if receita > 0 else 0
        
        st.metric("Receita", f"R$ {receita:,.0f}")
        st.metric("Lucro", f"R$ {lucro:,.0f}")
        st.metric("Margem de Lucro", f"{margem:.1f}%")
        
        # Gráfico de pizza
        fig = go.Figure(data=[go.Pie(
            labels=['Lucro', 'Custos'],
            values=[lucro, custo],
            hole=.3,
            marker_colors=['green', 'red']
        )])
        fig.update_layout(title="Composição da Receita")
        st.plotly_chart(fig, use_container_width=True)

def main():
    """Função principal do aplicativo"""
    # Cabeçalho
    st.markdown('<h1 class="main-header">🧠 Fundamentos Financeiros</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #D1D5DB; font-family: Inter, sans-serif; font-size: 1.125rem;">Jornada do Espantalho</p>', unsafe_allow_html=True)
    
    # Barra de progresso
    progress = len(st.session_state.completed_modules) / len(MODULES_DATA) * 100
    st.progress(progress / 100)
    st.markdown(f'<p style="text-align: center; color: #F59E0B; font-weight: bold;">{progress:.0f}% Concluído</p>', unsafe_allow_html=True)
    
    # Conteúdo principal
    if not st.session_state.journey_started:
        show_welcome_section()
    elif st.session_state.current_module:
        show_module_content(st.session_state.current_module)
    else:
        # Mapa de competências
        st.markdown('<h2 style="text-align: center; color: #F59E0B; font-family: Poppins, sans-serif; margin: 2rem 0;">🗺️ Mapa de Competências Financeiras</h2>', unsafe_allow_html=True)
        
        # Módulos em grid
        for i in range(0, len(MODULES_DATA), 2):
            col1, col2 = st.columns(2)
            with col1:
                show_module_card(MODULES_DATA[i])
            if i + 1 < len(MODULES_DATA):
                with col2:
                    show_module_card(MODULES_DATA[i + 1])
        
        # Estatísticas
        show_stats()
        
        # Verificar se todos os módulos foram concluídos
        if len(st.session_state.completed_modules) == len(MODULES_DATA):
            st.balloons()
            st.markdown("""
            <div style="background: linear-gradient(135deg, #F59E0B, #D97706); padding: 2rem; border-radius: 1rem; text-align: center; margin: 2rem 0;">
                <h2 style="color: white; font-family: 'Poppins', sans-serif;">🎉 Parabéns!</h2>
                <p style="color: white; font-size: 1.25rem;">Você concluiu sua jornada de fundamentos financeiros!</p>
                <p style="color: white;">Sua mente agora possui as conexões neurais necessárias para compreender e aplicar conceitos financeiros fundamentais.</p>
            </div>
            """, unsafe_allow_html=True)

    # Sidebar com informações
    with st.sidebar:
        st.markdown("### 📊 Progresso da Jornada")
        st.metric("Módulos Concluídos", f"{len(st.session_state.completed_modules)}/{len(MODULES_DATA)}")
        st.metric("Sinapses Ativas", st.session_state.stats['sinapses'])
        st.metric("Insights Gerados", st.session_state.stats['insights'])
        st.metric("Aplicações Práticas", st.session_state.stats['aplicacoes'])
        
        st.markdown("---")
        st.markdown("### 🧠 Sobre a Jornada")
        st.markdown("""
        Esta jornada utiliza princípios de neurociência para otimizar o aprendizado de conceitos financeiros fundamentais.
        
        Cada módulo foi projetado para ativar diferentes áreas cerebrais, criando uma rede neural robusta para compreensão financeira.
        """)
        
        if st.button("🔄 Reiniciar Jornada"):
            st.session_state.journey_started = False
            st.session_state.completed_modules = set()
            st.session_state.stats = {'sinapses': 0, 'insights': 0, 'aplicacoes': 0}
            st.session_state.current_module = None
            st.rerun()

if __name__ == "__main__":
    main()

