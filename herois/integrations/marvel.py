import os
import hashlib
import requests
import json

from decouple import config


class MarvelApi:
    def __init__(self):
        self.MARVEL_APIKEY = config("MARVEL_APIKEY")
        self.MARVEL_PRIVATE_KEY = config("MARVEL_PRIVATE_KEY")
        self.TIMESTAMP = config("TIMESTAMP")

    def __get_hash(self):
        string_to_hash = self.TIMESTAMP + self.MARVEL_PRIVATE_KEY + self.MARVEL_APIKEY
        hasher = hashlib.md5(string_to_hash.encode())
        return hasher.hexdigest()

    def get_heroe(self, nome: str):
        """Busca as informações do herói que foi informado como parâmetro
        :nome: nome do herói cadastrado na api da marvel
        """
        ts = self.TIMESTAMP
        public_key = self.MARVEL_APIKEY
        hash_md5 = self.__get_hash()

        response = requests.get(
            f'https://gateway.marvel.com:443/v1/public/characters?name={nome}&ts={ts}&apikey={public_key}&hash={hash_md5}')

        dict_response = response.json()

        return dict_response['data']['results'][0]
