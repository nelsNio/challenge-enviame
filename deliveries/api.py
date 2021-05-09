import json
import requests

"""
Clase encargada de realizar conexion con api de enviame
"""
class Enviame(object):
    def __init__(self):
        self.api = {}



    '''
    Metodo post modificado para enviar  api-key
    '''
    def post(self, data):
        headers={'api-key':'ea670047974b650bbcba5dd759baf1ed'}
        return requests.post('http://stage.api.enviame.io/api/s2/v2/companies/401/deliveries/',data=data, headers=headers)

"""
env=Enviame()
resp=env.post({})
print(resp.url)
print(resp.status_code)
# print(resp.content)
print(resp.json())
"""
