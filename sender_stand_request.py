import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados
response = post_new_user(data.user_body)

if response.status_code != 201:
    auth_token = response.json().get('auth_token')

def post_new_client_kit (body, auth_token):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH
                         , json=body, headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    })

