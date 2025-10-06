import psycopg2

conexao = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres"
)

cursor = conexao.cursor()

cursor.execute("""
                CREATE TABLE IF NOT EXISTS store (
                    id SERIAL PRIMARY KEY,
                    nome VARCHAR(50) NOT NULL,
                    endereco VARCHAR(100) NOT NULL,
                    telefone VARCHAR(20) NOT NULL
                );
                """)

conexao.commit()
conexao.close()
cursor.close()