# 📊 Financial Dashboard: Planejamento Tributário

Este projeto é uma aplicação interativa desenvolvida para facilitar a análise de regimes tributários no Brasil. Ele utiliza dados financeiros para projetar e comparar gastos entre o **Simples Nacional** e o **Lucro Presumido**.



## 🧠 Explicação do Código

O Dashboard funciona através de três pilares principais:

1.  **Entrada Dinâmica:** Através da barra lateral (`st.sidebar`), o usuário insere o faturamento e o custo de folha, permitindo simulações em tempo real.
2.  **Motor de Cálculo:** O código aplica as fórmulas de alíquotas efetivas do Simples Nacional (Anexo III) e as presunções de impostos federais e municipais do Lucro Presumido.
3.  **Visualização de Dados:** Transforma números complexos em gráficos de barras e métricas de destaque, facilitando a interpretação para quem toma decisões.

## 📚 Bibliotecas Utilizadas

Para rodar este projeto, as seguintes bibliotecas Python são necessárias:

* **Streamlit:** Framework principal usado para criar a interface web do dashboard.
* **Pandas:** Utilizada para a manipulação e estruturação dos dados financeiros em tabelas.
* **Plotly Express:** Biblioteca de gráficos interativos que permite visualizar o comparativo de custos de forma profissional.

## 🛠️ Como Executar

1. Instale as dependências:
   ```bash
   pip install streamlit pandas plotly