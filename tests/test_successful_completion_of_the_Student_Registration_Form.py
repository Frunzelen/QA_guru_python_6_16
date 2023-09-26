import allure
from selene import have, command
from pages.app_for_registration_form import RegistrationPage


@allure.title('Успешное заполнение формы регистрации студента')
def test_register_demo_user_using_practice_form(setup_browser):
    browser = setup_browser

    app = RegistrationPage()

    with allure.step("Открываем страницу регистрации"):
        app.open_demoqa_practice_form()

    with allure.step("Убираем рекламный банер"):
        app.script_trick()

    with allure.step("Заполняем все поля формы регистрации"):
        browser.element(app.first_name).type("Elena")
        browser.element(app.last_name).type("Ter")
        browser.element(app.user_email).type("Elenater@email.com")
        app.select_gender('Female')
        browser.element(app.phone_number).type("1234567890")
        app.select_date_of_birth('1', 'December', '2015')
        app.select_hobby('Sports')
        browser.element(app.subject).type("Computer Science").press_enter()
        app.upload_image("Angelina_Jolie.jpg")
        app.fill_current_address("Tbilisi")
        app.select_state("NCR")
        app.select_city("Delhi")

    with allure.step("Нажимаем кнопку Submit"):
        browser.element(app.submit_button).perform(command.js.click)

    with allure.step("Проверяем заполненные данные в сформированной таблице"):
        app.should_registered_user_with.should(
            have.exact_texts(
                'Elena Ter',
                'Elenater@email.com',
                'Female',
                '1234567890',
                '01 December,2015',
                'Computer Science',
                'Sports',
                'Angelina_Jolie.jpg',
                'Tbilisi',
                'NCR Delhi'
            )

        )