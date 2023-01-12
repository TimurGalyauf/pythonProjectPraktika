import requests
import json

# #                                                                 Проверка GET запросов
# ПОИСК ЖИВОТНЫХ ПО СТАТУСУ
# base_url = 'https://petstore.swagger.io/v2'
#
# # #                     headers = {'accept': 'application/json'})
# res_get1 = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus",
#                    params={'status': 'available'}, headers={'accept': 'application/json'})
#
# print('Статус ответа от сервера на GET-запрос выдачи списка питомцев со статусом available: ', res_get1.status_code)
# print("Карточка запроса:")
# print(res_get1.json())
# print ('********************************************')
#
# ПОИСК ЖИВОТНЫХ ПО ID
#
# petId = 910
# res_get4 = requests.get(f"https://petstore.swagger.io/v2/pet/{petId}",
#                    headers={'accept': 'application/json'})
# print('Статус ответа от сервера на GET-запрос поиск питомцев по id: ', res_get4.status_code)
# print("Карточка запроса:")
# print(res_get4.json())

#                                                               Проверка POST запросов
# ДОБАВЛЕНИЕ НОВОГО ПИТОМЦА
# nw_pet = {
#     "id": 2515453,
#     "category": {"id": 2, "name": "Cat"},
#     "name": "VasyaKisKis",
#     "photoUrls": ["string"],
#     "tags": [{"id": 0, "name": "strings"}],
#     "status": "available"
# }
# res_post_addNewPet = requests.post(f"https://petstore.swagger.io/v2/pet",
#                                   headers={'accept': 'application/json', 'Content-Type': 'application/json'},
#                                   data = json.dumps(nw_pet, ensure_ascii=False))
# print(f"Статус ответа от сервера на POST запрос добавление питомца: {res_post_addNewPet.status_code}")
# try:
#     rez = res_post_addNewPet.json()
#     print(f"ID number добавленного питомца = {rez['id']}")
#     print(f"Имя добавленного питомца = {rez['name']}")
# except:
#     rez = res_post_addNewPet.text()
#     print("Карточка питомца:")
#     print(res_post_addNewPet.text())

#                                                         Проверка PUT запросов
# ИЗМЕНЕНИЯ ИМЕНИ ПИТОМЦА
# nw_pet = {
#     "id": 2515453,
#     "category": {"id": 2, "name": "Cat"},
#     "name": "MusyaGAVAGAV",
#     "photoUrls": ["string"],
#     "tags": [{"id": 0, "name": "strings"}],
#     "status": "available"
# }
# res_put_redactPet = requests.put(f"https://petstore.swagger.io/v2/pet",
#                                   headers={'accept': 'application/json', 'Content-Type': 'application/json'},
#                                   data = json.dumps(nw_pet, ensure_ascii=False))
# print(f"Статус ответа от сервера на PUT-запрос редактирование питомца: {res_put_redactPet.status_code}")
# try:
#     rez = res_put_redactPet.json()
#     print(f"ID номер отредактированного питомца = {rez['id']}")
#     print(f"Имя отредактированного питомца = {rez['name']}")
# except:
#     rez = res_put_redactPet.text()
#     print("Карточка питомца:")
#     print(res_put_redactPet.text())

#                                                       Проверка DELETE запросов
# УДАЛЕНИЕ ПИТОМЦА
# petId = 2515453
# res_del_Pet = requests.delete(f"https://petstore.swagger.io/v2/pet/{petId}",
#                                   headers={'accept': 'application/json', 'Content-Type': 'application/json'})
# print(f"Статус ответа от сервера на DELETE запрос удаление питомца: {res_del_Pet.status_code}")




