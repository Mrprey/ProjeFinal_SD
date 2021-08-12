from flask import jsonify
import requests

def wellcome_API(link):
    response = requests.get(link)
    return response.text

def all_movies(link):
    response = requests.get(link)
    return response.json()

def post_movie(link, name, duration):
    payload = {'title':name, 'duration':duration}
    response = requests.post(link, json = payload)
    print(response.url)
    return response.json()

def find_movie(link, id):
    try:
        response = requests.get(link+'/'+id)
        return response.json()
    except:
        return "Filme não encontrado"



#if __name__ == "__main__":
    #print(wellcome_API('http://127.0.0.1:5000/datas/'))
    #print(find_movie('http://127.0.0.1:5000/datas', "4"))
    #print(post_movie('http://127.0.0.1:5000/datas'))
    #print(all_movies('http://127.0.0.1:5000/datas'))
