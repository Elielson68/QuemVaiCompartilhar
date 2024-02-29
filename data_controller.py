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
        except Exception as e:
            print("------------\nErro ao tentar carregar dados:\n", e, "\n------------")

    def GetData(self):
        return self.__data_loaded

    def IsDataExist(self):
        return self.__data_loaded is not None

    @staticmethod
    def SaveData(data: dict):
        try:
            put(DB, json=data)
            print("Salvou: ", data)
        except Exception as e:
            print("------------\nErro ao tentar salvar dados:\n", e, "\n------------")
