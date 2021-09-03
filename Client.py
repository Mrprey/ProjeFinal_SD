# from flask import jsonify
import requests

def wellcome_API(link):
    response = requests.get(link)
    return response.text

def all_itens(link):
    response = requests.get(link)
    return response.json()

def post_iten(link, name, price):
    payload = {'nome':name, 'preco':price}
    response = requests.post(link, json = payload)
    print(response.url)
    return response.json()

def find_iten(link, id):
    try:
        response = requests.get(link+'/'+id)
        return response.json()
    except:
        return "Item não disponivel em estoque"




