import mysql.connector as mc 
import datetime as dt

#função que cria a conexão com o banco de dados
def conecta_banco():
    conexao = mc.connect(
        host = 'localhost', #local onde esta o banco
        database = 'bd_condominios', #nome da base de dados
        user = 'root', #tipo de usuario que realiza o login
        password = 'Fabi0809*') #senha de acesso ao banco
    return conexao

def insere_chamado_banco(solicitante, descricao, bloco, apto):
    COMANDO_INSERT = 'insert into chamados(solicitante, dt_abertura, descricao, bloco, apt) values (%s, %s, %s, %s, %s)'
    #sempre que precisar manipular banco de dados pelo python, usar essa função:
    conexaobd = conecta_banco()
    manipulador_sql = conexaobd.cursor()
    #passando valores para o coringa (%s)
    valores = (solicitante, dt.datetime.now(), descricao, bloco, apto)
    #função que executa o comando no banco de dados:
    manipulador_sql.execute(COMANDO_INSERT, valores)
    #confirma alteração no banco:
    conexaobd.commit()


def exibe_todos_chamados():
    COMANDO_SELECT = "select * from chamados order by dt_abertura desc"
    conexao_bd = conecta_banco()
    manipulador_sql = conexao_bd.cursor()
    manipulador_sql.execute(COMANDO_SELECT)

    lista_chamados = manipulador_sql.fetchall()
    return lista_chamados

def filtra_chamado(nome):
    COMANDO_SELECT = "select * from chamados where solicitante like %s"
    valor = (nome,)
    conexao_bd = conecta_banco()
    manipulador_sql = conexao_bd.cursor()
    manipulador_sql.execute(COMANDO_SELECT, valor)
    return manipulador_sql.fetchall()

def deleta_chamado_id(id_chamado):
    COMANDO_DELETE = 'delete from chamados where id = %s'
    conexao_bd = conecta_banco()
    manipulador_sql = conexao_bd.cursor()
    valor = (id_chamado,)
    manipulador_sql.execute(COMANDO_DELETE, valor)
    conexao_bd.commit()

def atende_chamado(id_chamado):
    COMANDO_UPDATE = 'update chamados set status = false, dt_conclusao = %s where id = %s'
    conexao_bd = conecta_banco()
    manipulador_sql = conexao_bd.cursor()
    valor = (dt.datetime.now(), id_chamado)
    manipulador_sql.execute(COMANDO_UPDATE, valor)
    conexao_bd.commit()

