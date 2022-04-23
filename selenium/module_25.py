import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#driver = webdriver.Chrome()
#driver.get('http://petfriends1.herokuapp.com/login')

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('./chromedriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends1.herokuapp.com/login')

   yield

   pytest.driver.quit()

def test_all_my_pets_present():
   # Тест на проверку того, что количество питомцев в таблице "Мои питомцы"
   # совпадает с тем, что указано в информации о пользователе
   # c явным ожиданием загрузки списка "Мои питомцы"
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('yuriy.ragel@icloud.com')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys("Ragel1985?")
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Переходим на страницу "Мои питомцы"
   pytest.driver.find_element_by_css_selector('a[href="/my_pets"]').click()
   # Добавляем явное ожидание загрузки списка моих питомцев
   element = WebDriverWait(pytest.driver, 10).until(EC.visibility_of_element_located((By.ID, "all_my_pets")))
   # Посчитаем количество питомцев
   my_pets_qty = pytest.driver.find_elements_by_xpath("//*[contains(@scope, 'row')]")
   print("\n Количество питомцев в таблице My pets", len(my_pets_qty))

   # Собираем информацию о пользователе на сайте:
   user_info = pytest.driver.find_element_by_css_selector("div.\.col-sm-4.left")
   print ("\n Информация о пользователе на сайте: \n", user_info.text)

   # Проверяем, что количество питомцев в таблице "Мои питомцы" совпадает с тем, что указано в информации о пользователе
   assert str(len(my_pets_qty)) in user_info.text


def test_pets_no_photo():
   # Тест на проверку количества питомцев без фото на странице "Все питомцы"
   # c добавлением неявного ожидания на загрузку карточек питомцев
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('yuriy.ragel@icloud.com')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys("Ragel1985?")
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Делаем неявную задержку пока не загрузится контейнер с карточками питомцев
   pytest.driver.implicitly_wait(10)
   pytest.driver.get("http://petfriends1.herokuapp.com/all_pets")
   # Неявные ожидания:
   WaitContainerLoad = pytest.driver.find_elements_by_class_name("card-deck")
   WaitCardBodiesLoad = pytest.driver.find_elements_by_class_name("card-body")
   WaitCardsPhotosLoad = pytest.driver.find_elements_by_class_name("card-img-top")
   WaitCardsNamesLoad = pytest.driver.find_elements_by_class_name("card-title")
   WaitCardsTextLoad = pytest.driver.find_elements_by_class_name("card-text")
   images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
   print("\n Всего питомцев", len(images))
   no_images = 0
   for i in range(len(images)):
      if images[i].get_attribute('src') == '':
         no_images +=1
   print("\n Питомцев без фотографий = ", no_images)


def test_show_my_pets():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('yuriy.ragel@icloud.com')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys("Ragel1985?")
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"

def test_my_pets():
   images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
   names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
   descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')


   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      assert ', ' in descriptions[i]
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0
