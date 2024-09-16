import streamlit as st
from datetime import datetime, time
from contrato import Vendas
from pydantic import ValidationError


def main():
    st.title("Sistema de CRM e Vendas da ZapFlow")
    email = st.text_input("Campo de texto para inserção do email do vendedor")
    data = st.date_input("Data da compra", datetime.now())
    hora = st.time_input("Hora da Compra", value=time(9,0))
    valor = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade de produtos", min_value=1, step=1)
    produto = st.selectbox("Campo de seleção de produto", options=["ZapFlow com Gemini", "ZapFlow com chatGPT", "ZapFlow com llama3.0"])

    if st.button("Salvar"):
        try:
            data_hora = datetime.combine(data, hora)

            vendas = Vendas(
                email = email,
                data = data_hora,
                valor = valor,
                quantidade = quantidade,
                produto = produto
            )
            st.write(vendas)
        except ValidationError as e:
            st.error(f"Erro: ", {e}) 


if __name__=="__main__":
    main()