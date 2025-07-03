import sender_stand_request
import data


def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body

def positive_assert(name):
    response_user = sender_stand_request.post_new_user(data.user_body)
    assert response_user.status_code == 201
    auth_token = response_user.json().get('authToken')

    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 201

def negative_assert(name):
    response_user = sender_stand_request.post_new_user(data.user_body)
    assert response_user.status_code == 201
    auth_token = response_user.json().get('authToken')
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 400
    assert kit_response.json().get('code') == 400
    assert kit_response.json().get('message') == 'No se han aprobado todos los parámetros requeridos'

def negative_assert_no_name():
    response_user = sender_stand_request.post_new_user(data.user_body)
    assert response_user.status_code == 201
    auth_token = response_user.json().get("authToken")
    kit_body = {}
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 400
    assert kit_response.json().get('code') == 400
    assert kit_response.json().get('message') == 'No se han aprobado todos los parámetros requeridos'

def negative_assert_non_string_name():
    response_user = sender_stand_request.post_new_user(data.user_body)
    assert response_user.status_code == 201
    auth_token = response_user.json().get("authToken")

    kit_body = {
        "name": 123
    }

    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert kit_response.status_code == 400
    assert kit_response.json().get('code') == 400
    assert kit_response.json().get('message') == 'El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres'

# Test 1. User created successfully the kit with 1 character as a name
def test_create_kit_1_character_in_name_get_success_response():
    positive_assert("a")
# Test 2. User created successfully the kit with 511 characters as a name
def test_create_kit_511_character_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
#Test 3. User created unsuccessfully the kit with 0 characters as a name
def test_create_kit_0_character_name_get_no_success_response():
    negative_assert("")
#Test 4. User created unsuccessfully the kit with 512 characters as a name
def test_create_kit_1_character_name_get_no_success_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
#Test 5. User created successfully the kit with special characters as a name
def test_create_kit_special_character_name_get_success_response():
    positive_assert("№%@,")
#Test 6. User created successfully the kit with space between characters as a name
def test_create_kit_space_between_characters_name_get_no_success_response():
    positive_assert(" A Aaa ")
#Test 7. User created unsuccessfully the kit with numbers as a name
def test_create_kit_numbers_as_name_get_success_response():
    positive_assert("123")
#Test 8. User created unsuccessfully the kit with no parameter sent as a name
def test_create_kit_no_parameter_get_no_success_response():
    negative_assert_no_name()
#Test 9. User created unsuccessfully the kit with different parameter sent as a name
def test_create_kit_name_different_parameter_get_no_success_response():
    negative_assert_non_string_name()