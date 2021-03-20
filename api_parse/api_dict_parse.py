import json
from requests import get



def get_certs():
    list_inn_supplierinn = [7735116621, 7729394758, 7731625191, 7702735506, 7722523002, 5024096727, 7709654648, 7710499161, 7722523002, 9723041340, 7717629606, 7811625045, 7717629606, 7810797732, 7840501541, 3664115445, 7704767623, 7715631511, 7722585721, 7714842686, 5904159516, 7805109081, 5904159516, 7734649680, 7734649680, 7734649680, 7734649680, 7805109081, 7734649680, 7734649680, 7424022032, 7704767623, 7805109081, 7704767623, 3664115445, 7704767623, 3664115445, 7704767623, 7715631511, 7703608910, 7842464310, 7724833987, 9705138050, 7704030780, 7729498813, 5260146265]
    list_inn_customerinn = [7710878000, 7701903677, 7706074737, 7704055136, 7702005066, 7701014621]
    
    json_contracts_zaka = []
    json_contracts_post = []

    for inn in list_inn_supplierinn:
        req = get(f"http://openapi.clearspending.ru/restapi/v3/contracts/search//?supplierinn={inn}")
        data = json.loads(req.text)
        json_contracts_zaka.append(data)

    for inn in list_inn_customerinn:
        req = get(f"http://openapi.clearspending.ru/restapi/v3/contracts/search//?customerinn={inn}")
        data = json.loads(req.text)
        json_contracts_post.append(data)

    return json_contracts_zaka, json_contracts_post

