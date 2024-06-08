import requests
import json


url = "https://server.trixlog.com/driver/43936"

payload = {
    "name":"LEONARDO WENDEL DUARTE REGO","registration":"28003127","type":"SELLER","driverTeam":{"id":583,"name":"RN - MSR - LEILA LIANE MARTINS SILVA","description":"RN - MSR - AURIDEMBERG FRANCISCO DE FREITAS DO NASCIMENTO","organization":{"id":10535,"parentOrganization":{"id":10072,"parentOrganization":{"id":10309,"parentOrganization":{"id":10720,"parentOrganization":{"id":10616,"parentOrganization":{"id":10474,"parentOrganization":{"id":10020,"name":"SOLARBR","state":"","country":"","gmt":-180,"dst":False,"trixOrganization":False,"hierarchicalLevel":{"id":1,"name":"Solar","description":"Solar","level":1,"isLevelDetailed":True},"logo":{"id":21,"url":"https://s3.amazonaws.com/prod-roadnet-integration/photos/organization/logo/1624658099784"}},"name":"OPERAÇÃO DIRETA","state":"","country":"","gmt":-180,"dst":False,"hierarchicalLevel":{"id":2,"name":"Operação","description":"Operação","level":2,"isLevelDetailed":True}},"name":"OPERAÇÃO SOLAR","description":" ","gmt":-180,"hierarchicalLevel":{"id":754,"name":"Nível 3","description":"Nível 3","level":3,"isLevelDetailed":True}},"name":"REG. LESTE - OPERAÇÃO DIRETA","state":"","country":"","gmt":-180,"dst":False,"hierarchicalLevel":{"id":3,"name":"Regionais","description":"Regionais","level":4,"isLevelDetailed":True}},"name":"RN - RIO GRANDE DO NORTE","description":"OPERAÇÃO DIRETA RIO GRANDE DO NORTE.","state":"","country":"","tags":"","gmt":-180,"dst":False,"trixOrganization":False,"hierarchicalLevel":{"id":4,"name":"Estados","description":"Estado","level":5,"isLevelDetailed":True}},"name":"RN - MSR - MOSSORO","description":"SOLAR MOSSORO ","state":"","country":"","tags":"","gmt":-180,"dst":False,"trixOrganization":False,"hierarchicalLevel":{"id":6,"name":"Unidades","description":"Unidades","level":7,"isLevelDetailed":True}},"name":"RN - MSR - VENDAS GERENCIA 1","state":"","country":"","gmt":-180,"dst":False,"hierarchicalLevel":{"id":7,"name":"Areas Operacionais","description":".","level":8,"isLevelDetailed":True}},"secundaryOrganizations":[10427,10535,10426,10392,10309,10073,10072,10350,10425,10543,10544,10717,10750,10763,10764],"filiationType":"INHERENT","ignoreDriverBehaviorScore":False,"representatives":[12173]},"hiringType":"FIXED","status":"ACTIVE","cpf":"08759734426","license":"2672523453","licenses":[{"license":"A"},{"license":"B"}],"licenseRegister":"7170872633","licenseExpedition":"2023-09-14T03:00:00.000Z","licenseExpiration":"2033-09-11T03:00:00.000Z","firstLicense":"2018-11-28T03:00:00.000Z","birthDate":"1995-08-08T03:00:00.000Z","identifications":[{"identificationType":"SAFETY","login":"87597344","password":"585e25cc29cb3fb9e887eb3a1c6f3088","uuid":"8753f540-ff6c-33f6-a7f6-77a56b737ff9","createdDate":"2022-01-12T14:54:21.319Z","updatedDate":"2022-01-13T10:10:56.223Z","status":"ACTIVE","hidePassword":True},{"identificationType":"DRIVER_APP","login":"87597344","password":"585e25cc29cb3fb9e887eb3a1c6f3088","uuid":"e24c2c5f-e4b0-396b-9bbe-0e7d9a61a93d","createdDate":"2022-01-12T14:54:21.319Z","updatedDate":"2022-01-13T10:10:56.223Z","lastLogon":"2024-05-29T11:10:40.947Z","status":"ACTIVE","hidePassword":True}],"riskDriver":False,"admissionDate":"2021-06-02T03:00:00.000Z","id":43936,"hasRFIDIdentification":False,"isBlockedToLinkVehicle":True
}

headers = {'Customer': str(44) ,}


response = requests.put(url, auth=('','!'),  headers=headers, json=payload)
data = response.json()
# print(data)
# print(data['registration'])

if response.status_code == 200:
    print("Login efetuado com sucesso!")
else:
    print(f"Erro ao fazer login. Código de status: {response.status_code}")