import json

class utility:

    @staticmethod
    def str_to_byte(str):
        str_json = json.dumps(str)
        str_byte = bytes(str_json, 'utf-8')
        return str_byte

    @staticmethod
    def byte_to_str(a):
        x = str(a, 'utf-8')
        x = json.loads(a)
        return x


