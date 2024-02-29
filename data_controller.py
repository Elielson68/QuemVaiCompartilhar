import json
from requests import get, put


DB = "https://quemvaicompartilharbd-default-rtdb.firebaseio.com/production.json"


class DataController:

    def __init__(self):
        self.__data_loaded = None

    def LoadData(self):
        try:
            data = get(DB).json()
            self.__data_loaded = data if data != "" else None
            print("Carregou: ", self.__data_loaded)
        except:
            print("Erro ao tentar carregar dados")

    def GetData(self):
        return self.__data_loaded

    def IsDataExist(self):
        return self.__data_loaded is not None

    @staticmethod
    def SaveData(data: dict):
        try:
            put(DB, json=data)
            print("Salvou: ", data)
        except:
            print("Erro ao tentar salvar dados")
