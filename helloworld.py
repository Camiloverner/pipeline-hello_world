from flask import Flask

# Cria uma instância do Flask
app = Flask(__name__)

# Define uma rota para a página inicial
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Executa o aplicativo
if __name__ == '__main__':
    app.run(debug=True)
