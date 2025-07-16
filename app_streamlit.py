
import streamlit as st
import json
import os

ARQUIVO = 'biblioteca_aprendizado.json'

st.title("📚 App de Aprendizado")

if not os.path.exists(ARQUIVO):
    with open(ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump([], f)

with open(ARQUIVO, 'r', encoding='utf-8') as f:
    dados = json.load(f)

tema = st.text_input("Tema")
assunto = st.text_input("Assunto")
funcao = st.text_input("Função")
explicacao = st.text_area("Explicação")
observacao = st.text_area("Observação")

if st.button("Adicionar"):
    nova_linha = [tema, assunto, funcao, explicacao, observacao]
    dados.append(nova_linha)
    with open(ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
    st.success("Adicionado com sucesso!")

filtros = st.columns(5)
filtro_tema = filtros[0].text_input("🔍 Tema")
filtro_assunto = filtros[1].text_input("🔍 Assunto")
filtro_funcao = filtros[2].text_input("🔍 Função")
filtro_explicacao = filtros[3].text_input("🔍 Explicação")
filtro_observacao = filtros[4].text_input("🔍 Observação")

st.write("## Tabela de Conhecimento")

for linha in dados:
    if all([
        filtro_tema.lower() in linha[0].lower(),
        filtro_assunto.lower() in linha[1].lower(),
        filtro_funcao.lower() in linha[2].lower(),
        filtro_explicacao.lower() in linha[3].lower(),
        filtro_observacao.lower() in linha[4].lower(),
    ]):
        st.markdown(f"**{linha[0]}** | {linha[1]} | {linha[2]}  
"
                    f"*{linha[3]}*  
"
                    f"`{linha[4]}`  
---")
