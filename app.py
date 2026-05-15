import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configuração da Página
st.set_page_config(page_title="Taaz Finance Dashboard", layout="wide", page_icon="📊")

# 2. Título e Estilo
st.title("📊 Taaz Finance: Dashboard de Planejamento Tributário")
st.markdown("""
Este dashboard compara a carga tributária entre o **Simples Nacional** e o **Lucro Presumido**, 
auxiliando na tomada de decisão para empresas de serviços.
""")
st.markdown("---")

# 3. Sidebar (Barra Lateral) para entrada de dados
st.sidebar.header("📥 Dados da Empresa")
faturamento_mensal = st.sidebar.number_input("Faturamento Mensal (R$)", min_value=0.0, value=15000.0, step=1000.0)
pro_labore = st.sidebar.number_input("Pró-Labore / Folha (R$)", min_value=0.0, value=3000.0, step=100.0)

# 4. Lógica de Cálculo (Regras de Negócio)
# Simples Nacional (Anexo III - Estimativa)
imposto_simples = faturamento_mensal * 0.06 
inss_simples = pro_labore * 0.11
total_simples = imposto_simples + inss_simples

# Lucro Presumido (Estimativa Federal 11.33% + ISS 5% + CPP 20%)
federais_presumido = faturamento_mensal * 0.1133
iss_presumido = faturamento_mensal * 0.05
cpp_patronal = pro_labore * 0.20
total_presumido = federais_presumido + iss_presumido + cpp_patronal + (pro_labore * 0.11)

# 5. Visualização no Dashboard
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Comparativo de Custos")
    df = pd.DataFrame({
        "Regime": ["Simples Nacional", "Lucro Presumido"],
        "Custo Total (R$)": [total_simples, total_presumido]
    })
    fig = px.bar(df, x="Regime", y="Custo Total (R$)", color="Regime", 
                 text_auto='.2f', color_discrete_sequence=['#2ecc71', '#3498db'])
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("📋 Veredito Fiscal")
    economia = abs(total_simples - total_presumido)
    melhor_opcao = "Simples Nacional" if total_simples < total_presumido else "Lucro Presumido"
    
    st.metric("Melhor Opção", melhor_opcao)
    st.metric("Economia Mensal Estimada", f"R$ {economia:.2f}")
    
    if total_simples < total_presumido:
        st.success(f"O **Simples Nacional** é a opção mais econômica para este cenário.")
    else:
        st.info(f"O **Lucro Presumido** apresenta uma vantagem tributária neste cenário.")

st.markdown("---")
st.caption("Desenvolvido por Lucas Araújo (Taaz) - Tecnologia & Contabilidade.")