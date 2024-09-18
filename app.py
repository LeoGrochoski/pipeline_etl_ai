import streamlit as st
from datetime import datetime, time
from database import fetch_products, save_sale


def main():
    st.title("Havertify - Sales Control System")

    
    products = fetch_products() # Busca os produtos da tabela Products no banco chamando a função fetch_products

    product_names = [product['product_name'] for product in products]
        
    selected_product = st.selectbox("Product selection:", options=product_names)

    if selected_product:
        product_details = next((product for product in products if product["product_name"] == selected_product), None)
        if product_details:
            # Exibe os detalhes do produto baseado no cadastro da tabela do banco
            st.write(f"**Description**: {product_details['description']}")
            st.write(f"**Quantity in a package**: {product_details['quantity_base']} {product_details['unity_measurement']}")
            st.write(f"**Unit Price**: R$ {product_details['unit_price']:.2f}")

            # Campo para o usuário inserir a quantidade desejada
            sales_quantity = st.number_input("Quantidade desejada:", min_value=1, step=1)

            # Calculo do valor total e a quantidade total
            total_value = product_details['unit_price'] * sales_quantity
            total_quantity = product_details['quantity_base'] * sales_quantity

            # Exibindo no front o Total da compra e a Quantidade total
            st.write(f"**Total purchase value:**: R$ {total_value:.2f}")
            st.write(f"**Total Quantity**: {total_quantity} {product_details['unity_measurement']}")

    seller_name = st.text_input("Seller's Name")
    seller_email = st.text_input("Seller's Email:")
    
    date_hour = datetime.now()

    if st.button("Save"):
        try: # salva os dados no banco 
            save_sale(
                product_name=selected_product,
                total_quantity=total_quantity,
                total_value=total_value,
                seller = seller_name,
                seller_email = seller_email,
                date_hour = date_hour
        )

            st.success("Sale saved successfully!")
        except Exception as e:
            st.error(f"Error saving sale: {e}")

if __name__ == "__main__":
    main()