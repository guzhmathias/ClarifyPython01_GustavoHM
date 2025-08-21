# Tipos de Bancos de Dados
# MongoDB -> Facebook
# SQL -> O que usaremos
# MySQL
# NoSQL
# Supabase
# Paradox

import sqlite3

# Conectar ao banco de dados (ou criar um novo, caso não exista)
def conectarBanco():
    conexao = sqlite3.connect('bancodedados.db')
    return conexao 

# Criar uma tabela
def criarTabela():
    conexao = conectarBanco() # Abre a conexão
    cursor = conexao.cursor() # cria um cursor para executar o comando sql

    #criar a tabela se ela não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nome TEXT,
            idade INTEGER
        )
        ''')
    conexao.commit()
    conexao.close()

def inserirUsuario(nome, idade):
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO usuarios (nome, idade)
        VALUES(?, ?)
    ''', (nome, idade))
    conexao.commit()
    conexao.close()

def listarUsuarios():
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('''
        SELECT * FROM usuarios
    ''')
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)
    conexao.close()

#Atualizar Banco de dados
def atualizarUser(id, novoNome, novaIdade):
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('''
        UPDATE usuarios
        SET nome = ?, idade = ?
        WHERE id = ?
    ''',(novoNome, novaIdade, id))
    conexao.commit()
    conexao.close()


#Excluir usuario - TOMAR CUIDADO USANDO ISSO AQUI
def excluirUser(id):
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('''
        DELETE FROM usuarios
        WHERE id = ?
    ''',(id,))
    conexao.commit()
    conexao.close()

#Exemplos de uso das funções crud

#Criar a tabela
criarTabela()

#Inserir dados no banco de dados


inserirUsuario("Gustavo", "22")
inserirUsuario("Marcelo", "23")
inserirUsuario("Catarina", "21")
inserirUsuario("Raissa", "19")
inserirUsuario("Seu Antenor","89")

# Listar todos os usuarios cadastrados no banco

print("Usuarios antes de atualizar")
listarUsuarios()


linha = '-' * 20
print(linha)

#Atualizar a idade e nome de um usuario
atualizarUser(1, 'Pedro', 23)
atualizarUser(3, 'Gabriela', 20)
print("Usuarios após atualizar")
listarUsuarios()
print(linha)

#Excluir usuario
print("Usuarios limpos com Sucesso")

excluirUser(1)
excluirUser(2)
excluirUser(3)
excluirUser(4)
excluirUser(5)

listarUsuarios()
print(linha)

