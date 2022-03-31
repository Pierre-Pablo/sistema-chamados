from flask import Flask, render_template, request, redirect, url_for
import bancodados

app = Flask(__name__)

@app.route('/')
def abre_chamado():
    dados = bancodados.exibe_todos_chamados()
    return render_template('chamados.html', dados_chamado = dados)

#Necessario definir a rota no python e no html.
@app.route('/', methods=['POST'])
def salvar_chamado():
    nome_reclamante = request.form['reclamante']
    descricao = request.form['descricao']
    bloco = request.form['bloco']
    apto = request.form['apto']
    bancodados.insere_chamado_banco(nome_reclamante, descricao, bloco, apto)
    return redirect(url_for('abre_chamado'))

@app.route('/pesquisa_chamado', methods = ['POST'])
def pesquisa_chamado():
    nome_pesquisado = request.form['pesq_nome']
    lista = bancodados.filtra_chamado(nome_pesquisado)
    return render_template('chamados.html', dados_chamado = lista)

@app.route('/excluir_chamado', methods=['POST'])
def excluir_chamado():
    id_excluido = request.form['id_chamado']
    bancodados.deleta_chamado_id(id_excluido)
    dados = bancodados.exibe_todos_chamados()
    return render_template('chamados.html', dados_chamado = dados)

@app.route('/atende_chamado', methods=['POST'])
def atende_chamado():
    id_atualiza = request.form['id_chamado']
    bancodados.atende_chamado(id_atualiza)
    return redirect(url_for('abre_chamado'))





app.run(debug = True)

