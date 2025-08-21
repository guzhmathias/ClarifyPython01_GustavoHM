from flask import Flask, render_template
# Flask é uma estrutura de trabalho, um Framework 
# Foca em trabalhar com web, rotas

# Criar a aplicação em Flask
app = Flask(__name__) # Nome da aplicação é o app
# Criar a rota(caminho) para acessar a pagina inicial -> Decorator
@app.route('/')
def inicio():
    return "<h1> hello world </h1> <br> <h3> Bem vindo a minha página inicial <br> <a href='/contato'>Fale Comigo! </h3>"
# Criar a rota(caminho) para acessar a pagina de contato
@app.route('/contato')
def contato():
    return "<h3><a href='mailto:kio199@gmail.com''> Me mande um e-mail! :) </h3> <hr> <a href='/'> <<< Voltar ao início! </a>"
# Criar rota com variáveis na URL
@app.route('/especial/<nome>')
def rotaespecial(nome):
    return f'<h1> Seja bem vindo ao meu sistema, {nome}!</h1>'

# Toda a aplicação em flask necessita do seguinte comando
if __name__ == '__main__':
    app.run(debug=True)