from flask import Flask, request
from merge_sort import merge_sort


app = Flask(__name__)

@app.route('/')
def home():
    return ("<p>Opa, parece que você ainda não me passou uma array!<p>"
        + f"<p>Você pode fazer isso simplesmente adicionando os números à url separados por vírgula, como em <a href='{request.base_url}2,1,4,6,5,3'>{request.base_url}2,1,4,6,5,3</a>")

@app.route("/<lista>")
def hello_world(lista):
    try:
        lista = [int(i) for i in lista.split(',')]
        return str(merge_sort(lista))
    except:
        return "Entrada Inválida"
