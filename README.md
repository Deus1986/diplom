<h1> Проект Web/Api/Mobile тестирования "Мегафон"  </h1>

> <a target="_blank" href="https://spb.shop.megafon.ru/">Megaphone</a>

![This is an image](images/Megafone_main_page.png)
<!-- Технологии -->

### Используемые технологии

<p  align="center">
   <code><img width="5%" title="Python" src="images/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/pytest.png"></code>
  <code><img width="5%" title="Requests" src="images/requests.png"></code>
  <code><img width="5%" title="Selene" src="images/selene.png"></code>
  <code><img width="5%" title="Selenium" src="images/selenium.png"></code>
   <code><img width="5%" title="Appium" src="images/appium.png"></code>
   <code><img width="5%" title="Browserstack" src="images/browserstack.png"></code>
   <code><img width="5%" title="PyCharm" src="images/pycharm.png"></code>
  <code><img width="5%" title="Android Studio" src="images/android_studio.png"></code>
  <code><img width="5%" title="Jenkins" src="images/jenkins.png"></code>
  <code><img width="5%" title="Allure Report" src="images/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="images/allure_testops.png"></code>
  <code><img width="5%" title="Telegram" src="images/tg.png"></code>
</p>


<!-- Тесты -->
UI:

* ✅ Add product to cart
* ✅ Delete product from cart
* ✅ Filter smartphone by name iphone
* ✅ Information about contacts
* ✅ Main page header
* ✅ Private individuals services links
* ✅ Search by name iphone

Mobile:

* ✅ No access to sim card link
* ✅ Page have choices sim cards
* ✅ Authorization unregistered user by password

API:

* ✅ Delete order
* ✅ Add product to cart
* ✅ Get info about stores for product
* ✅ Storelocator
* ✅ Update quantity of product


<!-- Jenkins -->

### <img width="3%" title="Jenkins" src="images/jenkins.png"> Запуск проекта в Jenkins

### [Задача в jenkins](https://jenkins.autotests.cloud/job/hw_diplom_Vladimir/)

#### Для запуска автотестов в Jenkins

1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/hw_diplom_Vladimir/">Проект в Jenkins</a>
2. Выбрать пункт `Build with Parameters`
3. Выбрать тип запускаемых тестов в выпадающем списке Type_of_tests(ui, api, mobile)
4. Выбрать контекст запускаемых тестов в выпадающем списке context(remote_web, bstack, api)
5. Указать версию браузера, по умолчанию стоит 122
6. Нажать кнопку `Build`
7. Результат запуска сборки можно посмотреть в отчёте Allure

<img alt="This is an image" src="images/Jenkins_build_instruction.png" width="900"/>

<!-- Allure report -->

### <img width="3%" title="Allure Report" src="images/allure_report.png"> Allure report

##### Результаты выполнения тестова можно посмотреть в Allure-отчете

![This is an image](images/Allure_api_overview.png)
    Отчет позволяет получить общую информацию оп прохождении тестов

![This is an image](images/Allure_api_suites.png)
    Отчет позволяет получить информацию о прохождении каждого теста

![This is an image](images/Allure_api_suites_fail_test.png)
    Отчет позволяет получить детальную информацию по все шагам тестов, включая скриншоты, 
log - файлы и видео о прохождение теста(набор атач файлов зависит от типа тестов), а так 
же позволяет оперативно понять причину падения теста.

##### Видео прохождение  ui теста (Добавление товара в корзину)
![This is an image](images/test_video.gif)

##### Видео прохождение  mobile теста (Авторизация незарегестрированного пользователя)
![This is an image](images/mobile_test.gif)
<!-- Allure TestOps -->

### <img width="3%" title="Allure TestOps" src="images/allure_testops.png"> Интеграция с Allure TestOps

### [Dashboard](https://allure.autotests.cloud/project/4530/dashboards)

![This is an image](images/Allure_dashboard.png)
Дашборд с результатами о прохождении тестов.

<!-- Telegram -->

### <img width="3%" title="Telegram" src="images/tg.png"> Оповещения в Telegram

##### После выполнения тестов, в Telegram bot приходит сообщение с графиком и информацией о тестовом прогоне.

![This is an image](images/TG_ui.png)

Уведомление телеграмм с результатами о прохождении UI тестов.

![This is an image](images/TG_api.png)
    
Уведомление телеграмм с результатами о прохождении API тестов.

![This is an image](images/TG_mobile.png)

Уведомление телеграмм с результатами о прохождении MOBILE тестов.