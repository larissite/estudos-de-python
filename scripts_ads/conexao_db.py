import sqlite3 as conector

conexao = None
cursor = None
try:
    conexao = conector.connect('./meu_banco.db')
    conexao.execute('PRAGMA foreign_keys = on')
    cursor = conexao.cursor()
    #
    # comando = ''' DROP TABLE Pessoa '''
    #
    # comando_2 = ''' DROP TABLE Marca '''
    #
    # comando_3 = ''' DROP TABLE Veiculo '''

    tabela = '''CREATE TABLE Pessoa (
                        cpf INTEGER NOT NULL,
                        nome TEXT NOT NULL,
                        nascimento DATE NOT NULL,
                        oculos BOOLEAN NOT NULL,
                        PRIMARY KEY (cpf)
                        );'''

    tabela_2 = '''CREATE TABLE Marca (
                        id INTEGER NOT NULL,
                        nome TEXT NOT NULL,
                        sigla CHARACTER(2) NOT NULL,
                        PRIMARY KEY (id)
                );'''

    tabela_3 = '''CREATE TABLE Veiculo (
                        placa CHARACTER(7) NOT NULL,
                        ano INTEGER NOT NULL,
                        cor TEXT NOT NULL,
                        proprietario INTEGER NOT NULL,
                        marca INTEGER NOT NULL,
                        PRIMARY KEY (placa),
                        FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
                        FOREIGN KEY(marca) REFERENCES Marca(id)
                );'''

    # cursor.execute(comando)
    # cursor.execute(comando_2)
    # cursor.execute(comando_3)

    cursor.execute(tabela)
    cursor.execute(tabela_2)
    cursor.execute(tabela_3)
    conexao.commit()
    
except conector.DatabaseError as error:
    print('Erro de banco de dados', error)

finally:
    if conexao:
        cursor.close()
        conexao.close()
