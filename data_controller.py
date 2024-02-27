import json


class DataController:

    def __init__(self):
        self.__data_loaded = None

    def LoadData(self):
        with open("share_data.js") as file:
            data = file.read()
            if data != "":
                self.__data_loaded = json.loads(data)

    def GetData(self):
        return self.__data_loaded

    def IsDataExist(self):
        print(self.__data_loaded is not None)
        return self.__data_loaded is not None

    @staticmethod
    def SaveData(data: dict):
        with open("share_data.js", "w") as file:
            file.write(json.dumps(data, indent=1))
