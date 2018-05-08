from flask import Flask, jsonify, request
import redis
import datetime

r = redis.Redis(
    host='172.16.129.18',
    port='6379')

##now = datetime.datetime.now()
##print(now)

app = Flask(__name__)

# GET /carrinho/1
@app.route('/carrinho/<int:usuarioId>')
def carrinho(usuarioId):
    dados = r.hgetall('carrinho:' + str(usuarioId))
    return jsonify(str(dados))

    ##return jsonify({'status': 404, 'mensagem': 'Postagem não encontrada'})

# POST /carrinho/
@app.route('/carrinho', methods=['POST'])
def novo_carrinho():
    objetoSessao = request.json
    
    ##return jsonify(objetoSessao['usuarioId'])
    
    r.hmset('carrinho:' + str(objetoSessao['usuarioId']), {'usuarioId': objetoSessao['usuarioId'], 'produtos': objetoSessao['produtos']})
    
    ##r.set('carrinho:usuarioId', objetoSessao['usuarioId'])
    ##r.sadd('carrinho:produtos', objetoSessao['produtos'])
    
    return jsonify({'status': 200, 'mensagem': 'Postagem salva com sucesso!'})

    ##postagem = Postagem(titulo=dados['titulo'], conteudo=dados['conteudo'])
    ##return jsonify({'status': 200, 'mensagem': 'Postagem salva com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)
