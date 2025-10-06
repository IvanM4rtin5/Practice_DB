import psycopg2

conexao = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres"
)

cursor = conexao.cursor()

# cursor.execute("""
#                CREATE TABLE IF NOT EXISTS consumer (
#                id SERIAL PRIMARY KEY,
#                nome VARCHAR(50) NOT NULL,
#                email VARCHAR(100) NOT NULL,
#                telefone VARCHAR(20) NOT NULL,
#                endereco VARCHAR(100) NOT NULL
#                );
#                """)

# cursor.execute("""
#         CREATE TABLE IF NOT EXISTS
#                products(
#                product_id SERIAL CONSTRAINT product_pk PRIMARY KEY,
#                product_name VARCHAR(50) NOT NULL,
#                product_price FLOAT NOT NULL,
#                product_type INT NOT NULL CONSTRAINT product_type_fk REFERENCES      product_type(product_type_id)
#                );
# """)
# print("tabela criada com sucesso")

# cursor.execute("""
#             CREATE TABLE IF NOT EXISTS product_type(
#             product_type_id SERIAL CONSTRAINT product_type_pk PRIMARY KEY,
#             product_type_name VARCHAR(50) NOT NULL
#             );
# """)
# print("tabela criada com sucesso")

# cursor.execute("""
# UPDATE consumer SET email = 'vitor@emial.com' WHERE id = 1;
# """)
# print("dado alterado com sucesso")


# cursor.execute("""
#             INSERT INTO consumer (nome, email, telefone, endereco, cep, cidade)
#             VALUES ('ANDREANE', 'andrea@emial.com',  '12345678910', 'rua 12', '57015080', 'SAO PAULO');""")
# print("dado inserido com sucesso")

# cursor.execute("""
#                INSERT INTO product_type (product_type_name)
#                VALUES   
#                     ('Eletronico'),
#                     ('Celular'),
#                     ('Computador');
#                """)
# print("dado inserido com sucesso")

# cursor.execute("""
#             INSERT INTO products (product_name, product_price, product_type)
#             VALUES ('Notebook', 2000.00, 1);
#             INSERT INTO products (product_name, product_price, product_type)
#             VALUES ('Celular', 1000.00, 2);
#             """)
# print("dado inserido com sucesso")


# cursor.execute("""
#             ALTER TABLE consumer ADD COLUMN cep VARCHAR(8);
#             ALTER TABLE consumer ADD COLUMN cidade VARCHAR(50);
#                 """)
# print("dado alterado com sucesso")


# cursor.execute("""
#             DELETE FROM consumer WHERE id <= 8;
#             """)
# print("dado excluido com sucesso")

# cursor.execute("""
#             DELETE FROM products WHERE products.product_id <= 3;
#             """)
# print("dado excluido com sucesso")

# conexao.commit()

# cursor.execute("SELECT * FROM consumer WHERE nome = 'ANDREANE'")

# cursor.execute("SELECT * FROM consumer WHERE nome ILIKE '%Andr%'")

# cursor.execute("SELECT * FROM consumer")
cursor.execute("SELECT * FROM products")

# cursor.execute("SELECT * FROM products WHERE product_id = 4")
# print(cursor.fetchall())

for row in cursor.fetchall():
    print(row)

conexao.commit()
conexao.close()
cursor.close()