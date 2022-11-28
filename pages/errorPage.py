from selenium.webdriver.common.by import By


class ErrorPage:

    def __init__(self, driver):
        self.driver = driver

        self.error_button_id = "bbki-bk-error-return-homepage-link"
        self.error_message_Xpath = "//*[@id='bbki-bk-error-amadeus-err-modal']/div/h1/span[1]"

    def check_error_title(self):
        msg = self.driver.find_element(By.XPATH, self.error_message_Xpath).text
        return msg

    def click_error_button(self):
        self.driver.find_element(By.ID, self.error_button_id).click()
