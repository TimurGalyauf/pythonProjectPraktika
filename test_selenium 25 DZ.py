import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def autorize():
   pytest.driver = webdriver.Chrome\
       ('/Projects/PycharmProjects/ChromeDriver/chromedriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.maximize_window()
   pytest.driver.get('http://petfriends.skillfactory.ru/login')
   yield
   pytest.driver.quit()

@pytest.fixture()
def page_my_pets():
    # Заходим в учетную запись пользователя
    pytest.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('llltimalll@gmail.com')
    pytest.driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys('az1sx2dc3fv4')
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Убеждаемся что страница верна (название страницы h1 == 'PetFriends')
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == 'PetFriends'

    # Переход в раздел "Мои питомцы"
    pytest.driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
    assert pytest.driver.find_element(By.TAG_NAME, 'h2').text != ''


def test_amount(page_my_pets):
    """Тест определяет все ли питомцы, отображенные в статистике, присутствуют
    на странице, в виде карточек питомцев"""

    # Выясняем количество питомцев из статистики и выводим число
    wait = WebDriverWait(pytest.driver, 10).until \
        (EC.presence_of_element_located((By.CSS_SELECTOR, '.\\.col-sm-4.left')))
    amount_of_pets_stat = int(pytest.driver.find_element(By.XPATH,
            '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(":")[1])
    print(f'\nПитомцев по статистике:', amount_of_pets_stat, ' шт.')

    # Выводим массив с именами и породой питомцев
    all_pets = pytest.driver.find_elements\
        (By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
    pets_data = [pet.text for pet in all_pets]
    not_uniq_pets = set([pet.text for pet in all_pets
                         if pets_data.count(pet.text) > 1])
    pet_names = []
    pet_types = []
    for pet in all_pets:
        pet_names.append(pet.text.split(' ')[0])
        pet_types.append(pet.text.split(' ')[1])
    print('Имена питомцев:', pet_names)
    print('Породы питомцев:', pet_types)
    print('Повторяющиеся питомцы:', not_uniq_pets)

    # Находим количество карточек питомцев
    amount_of_pets_card = len(pets_data)
    print('Количество карточек питомцев:', amount_of_pets_card)

    # Проверяем что все питомцы из статистики отображены в карточках
    assert amount_of_pets_stat == amount_of_pets_card


def test_photo(page_my_pets):
    """Тест определяет есть ли фото, хотя бы у половины карточек питомцев,
    если меньше половины - тест не пройдет"""

    # Выясняем количество питомцев из статистики и выводим число
    wait = WebDriverWait(pytest.driver, 10).until \
            (EC.presence_of_element_located((By.CSS_SELECTOR, '.\\.col-sm-4.left')))
    amount_of_pets_stat = int(pytest.driver.find_element(By.XPATH,
            '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(":")[1])
    print(f'\nПитомцев:', amount_of_pets_stat, ' шт.')

    # Находим половину от количества питомцев
    half_pets = (amount_of_pets_stat / 2)
    print('Половина питомцев:', half_pets, 'шт.')

    # Вычисляем карточки питомцев свозможным фото (по атрибуту img)
    photo = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')

    # Находим количество фото
    pets_with_photo = 0
    for i in range(len(photo)):
        if photo[i].get_attribute('src') != '':
            pets_with_photo += 1
    print('Питомцев с фото:', pets_with_photo)

    # Вычисляем, что количество питомцев с фото, не меньше половины питомцев
    assert pets_with_photo >= half_pets, 'Количество питомцев с фото меньше ' \
                                         'половины количества питомцев'


def test_name_age_breed(page_my_pets):
    """Определяем у всех ли питомцев есть имя, возраст и порода, если нет -
    тест не пройдет"""

    pytest.driver.implicitly_wait(10)
    pytest.driver.find_elements(By.CSS_SELECTOR,
                            'div#all_my_pets table tbody tr th img')
    pytest.driver.find_elements(By.CSS_SELECTOR,
                            'div#all_my_pets table tbody tr td')
    pytest.driver.find_elements(By.CSS_SELECTOR,
                            'div#all_my_pets table tbody tr td:nth-of-type(3)')

    # Сохраняем данные питомцев
    pet_data = pytest.driver.find_elements(By.CSS_SELECTOR,
                                           '.table.table-hover tbody tr')
    print('\n',pet_data)

    # Проверяем начилие необходимых атрибутов в данных питомцев
    for i in range(len(pet_data)):
        ex_pet_data = pet_data[i].text.replace('\n', '').replace('*', '')
        fin_pet_data = ex_pet_data.split(' ')
        result = len(fin_pet_data)
        assert result == 3, 'не у всех питомцев есть имя, возраст или порода'

    if result == 3:
        print('\n','У всех питомцев указано имя, возраст и порода')


def test_different_name(page_my_pets):
    """Проверяем имена питомцев, они должны быть разными, если нет -
    тест не пройдет"""

    wait = WebDriverWait(pytest.driver, 10).until\
            (EC.presence_of_element_located((By.CSS_SELECTOR,
                                             '.table.table-hover tbody tr')))

    # Получаем данные питомцев
    pet_data = pytest.driver.find_elements(By.CSS_SELECTOR,
                                           '.table.table-hover tbody tr')

    # Выбираем имена
    pets_name = []
    for i in range(len(pet_data)):
        ex_pet_data = pet_data[i].text.replace('\n', '').replace('×', '')
        fin_pet_data = ex_pet_data.split(' ')
        pets_name.append(fin_pet_data[0])

    # Ищем одинаковые имена (счетчик считает число повторений)
    identic = 0
    for i in range(len(pets_name)):
        if pets_name.count(pets_name[i]) > 1:
            identic += 1
    assert identic == 0, 'В списке представлены питомцы имеющие одинаковые имена'

    if identic == 0:
        print('\n','У всех питомцев разные имена')


def test_different_pets(page_my_pets):
    """Проверяем, что у нас нет полностью идентичных питомцев, сразу по трем
     аргументам (имя, возраст, порода)"""

    wait = WebDriverWait(pytest.driver, 10).until\
            (EC.presence_of_element_located((By.CSS_SELECTOR,
                                             ".table.table-hover tbody tr")))

    # Получаем данные питомцев
    pet_data = pytest.driver.find_elements(By.CSS_SELECTOR,
                                           '.table.table-hover tbody tr')

    # Выбираем данные
    data_arg = []
    for i in range(len(pet_data)):
        pet_data_start = pet_data[i].text.replace('\n', '').replace('×', '')
        pet_data_end = pet_data_start.split(' ')
        data_arg.append(pet_data_end)

    # Полученные данные преобразуем в сплошную строку, ее в список, его в множество
    line = ''
    for i in data_arg:
        line += ''.join(i)
        line += ' '
    list_line = line.split(' ')
    set_list_line = set(list_line)

    # Находим количество элементов списка и множества, сравниваем
    a = len(list_line)
    b = len(set_list_line)
    result = a - b

    # Если результат == 0, значит идентичных питомцев нет
    assert result == 0, 'В списке содержатся повторяющиеся питомцы'

    if result == 0:
        print('\n','Идентичных питомцев нет')