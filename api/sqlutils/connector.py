import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

hostname = os.getenv("DB_HOST", "127.0.0.1")
porta = os.getenv("DB_PORT", "3306")
usuario = os.getenv("DB_USER", "root")
senha = os.getenv("DB_PASSWORD", "")
banco = os.getenv("DB_NAME", "done_db")


def conectar():
    conexao = mysql.connector.connect(host=hostname,
    port=porta,
    user=usuario,
    password=senha,
    database=banco)
    return conexao

# use essa função quando for executar um comando
# no banco de dados que precise alterar os dados
# lá dentro.
def executarComando(comando:str):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(comando)
    conexao.commit()
    conexao.close()

# use essa função quando for executar uma consulta,
# ou seja, um comando que retorna dados do banco.
def executarConsulta(consulta:str) -> list:
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    conexao.close()
    return resultado