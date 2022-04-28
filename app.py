from flask import Flask, request
from merge_sort import merge_sort
from parallel_sort import parallel_sort


app = Flask(__name__)

@app.route('/')
def home():
    return ("<p>Opa, parece que você ainda não me passou uma array!<p>"
        + f"<p>Você pode fazer isso simplesmente adicionando os números à url separados por vírgula, como em <a href='{request.base_url}2,1,4,6,5,3'>{request.base_url}2,1,4,6,5,3</a>"
        + f"<p>Ou se preferir você pode ainda escolher o número de threads que deseja usar. Por exmplo, para usar 4 threads: <a href='{request.base_url}4/2,1,4,6,5,3'>{request.base_url}4/2,1,4,6,5,3</a>")

@app.route("/<lista>")
def hello_world(lista):
    try:
        lista = [int(i) for i in lista.split(',')]
        return "Resultado atingido com uma thread: " + str(merge_sort(lista))
    except:
        return "Entrada Inválida"

@app.route("/<threads>/<lista>")
def parallel(threads, lista):
    try:
        lista = [int(i) for i in lista.split(',')]
        return f"Resultado atingido com {threads} threads: " + str(parallel_sort(lista,int(threads)))
    except:
        return "Entrada Inválida"
