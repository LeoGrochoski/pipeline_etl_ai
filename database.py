import psycopg2
import os
from dotenv import load_dotenv

# Carregar as variáveis do arquivo .env
load_dotenv()

# Recuperar os dados de conexão do arquivo .env
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# Função para conectar ao banco de dados PostgreSQL
def connect_db():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

# Função para buscar todos os detalhes dos produtos
def fetch_products():
    conn = connect_db()
    if conn is None:
        return []
    try:
        cur = conn.cursor()
        cur.execute("SELECT PRODUCT_NAME, DESCRIPTION, QUANTITY_BASE, UNIT_MEASUREMENT, UNIT_PRICE FROM Products")
        products = cur.fetchall()
        cur.close()
        conn.close()

        # Retorna os produtos como uma lista de dicionários
        return [{"product_name": row[0], "description": row[1], "quantity_base": row[2], "unity_measurement": row[3], "unit_price": row[4]} for row in products]

    except Exception as e:
        print(f"Error searching for products: {e}")
        return []

# Função para inserir dados na tabela vendas
def save_sale(product_name, total_quantity, total_value, seller, seller_email, date_hour):
    conn = connect_db()
    if conn is None:
        return
    try:
        cur = conn.cursor()

        # Inserir os dados na tabela vendas
        insert_query = """
            INSERT INTO Selling (product_name, total_quantity, total_value, seller, seller_email, date_hour)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cur.execute(insert_query, (product_name, total_quantity, total_value, seller, seller_email, date_hour))

        conn.commit()
        cur.close()
        conn.close()

    except Exception as e:
        print(f"Erro ao salvar a venda: {e}")
