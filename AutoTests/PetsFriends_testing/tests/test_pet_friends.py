from api import PetFriends
from settings import valid_email, valid_password, invalid_password, invalid_email
import os

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в тезультате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result

def test_get_api_key_for_invalid_email_valid_password(email=invalid_email, password=valid_password):
    """ __NEW TEST__
    Проверяем что запрос api ключа возвращает статус 403 при некорректном вводе email и корректном password"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' not in result

def test_get_api_key_for_valid_email_invalid_password(email=valid_email, password=invalid_password):
    """ __NEW TEST__
    Проверяем что запрос api ключа возвращает статус 403 при корректном вводе email и некорректном password --
    проверка того, что нельзя залогиниться под чужим имейлом и защита паролем работает"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' not in result

def test_get_all_pets_with_valid_key(filter=''):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
    запрашиваем список всех питомцев и проверяем что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо '' """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0

def test_get_my_pets_with_valid_key(filter='my_pets'):
    """
    __NEW TEST__
    Проверяем что запрос списка моих питомцев работает и полученный список отличен от списка всех питомцев
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
    запрашиваем список всех питомцев и проверяем что список не пустой.
    Доступное значение параметра filter - 'my_pets' """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status_1, result_1 = pf.get_list_of_pets(auth_key, '')
    status_2, result_2 = pf.get_list_of_pets(auth_key, filter)

    assert status_1 == 200
    assert status_2 == 200
    assert len(result_1['pets']) > 0
    assert len(result_2['pets']) <= len(result_1['pets'])

def test_get_all_pets_with_invalid_key(filter=''):
    """
    __NEW TEST__
    Проверяем что запрос всех питомцев c неверным кодом авторизации выдает ошибку 403
    """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    # Заменяем корректное значение ключа авторизации на некорректное "123":
    auth_key['key'] = '123'
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 403

def test_add_new_pet_with_valid_data(name='Барбоскин', animal_type='двортерьер',
                                     age='4', pet_photo='images/dog2.jpg'):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_add_new_pet_with_invalid_auth_key_valid_data(name='Барбоскин', animal_type='двортерьер',
                                     age='4', pet_photo='images/dog2.jpg'):
    """
    __NEW TEST__
    Проверяем что нельзя добавить питомца с корректными данными без авторизации на сайте
    (с некорректным кодом авторизации) -- ожидаем код 403"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Заменяем корректное значение ключа авторизации на некорректное "123":
    auth_key['key'] = '123'

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 403

def test_add_new_pet_with_invalid_data(name='Churchill', animal_type='pig',
                                     age='десять', pet_photo='images/dog2.jpg'):
    """
    __NEW TEST__
    Проверяем что добавление питомца с некорректными данными (возраст) выдает ошибку 400"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400
    assert result['name'] == name

    """Внимание! Тест failed -- запрос вернулся со статусом 200 вместо 400 -- питомец с некорректными данными в поле возраст
    (текст вместо цифрового значения) был успешно добавлен -- это BUG"""

def test_add_new_pet_with_invalid_photo(name='George', animal_type='hound',
                                     age='10', pet_photo='images/dog1.webp'):
    """
    __NEW TEST__
    Проверяем, что невозможно добавить фото питомца в некорректном формате, например webp
    Согласно API документации файл изображения должен быть только JPG, JPEG или PNG формат"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400
    assert result['name'] == name
    """ При выполнении test failed, так как сайт позволил добавить питомца с фотографией в некорректном формате - это BUG"""

def test_add_new_pet_with_valid_data_no_photo(name='Vasya', animal_type='puddle',
                                     age='2'):
    """
    __NEW TEST__
    Проверяем что можно добавить питомца с корректными данными БЕЗ ФОТО"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_no_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_add_new_pet_with_empty_data_no_photo(name='', animal_type='',
                                     age=''):
    """
    __NEW TEST__
    Проверяем, что нельзя добавить питомца с пустыми данными БЕЗ ФОТО"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_no_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400
    """ Внимание! Данный тест при выполнении failed, так как происходит добавление питомца с пустыми данными
    согласно документации параметры name, animal_type, age ОБЯЗАТЕЛЬНЫ (required), соответственно мы ожидаем статус 400,
    однаок получаем статус 200 -- это BUG """

def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='Мурзик', animal_type='Котэ', age=5):
    """Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")

def test_add_pet_photo(pet_photo='images/cat1.jpg'):
    """
    __NEW TEST__
    Проверяем возможность обновления фото питомца"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.add_pet_photo(auth_key, my_pets['pets'][0]['id'], pet_photo)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert len(result['pet_photo'])>0
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")