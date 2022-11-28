from selenium.webdriver.common.by import By


class BuscarVuelosPage:

    def __init__(self, driver):
        self.driver = driver
        self.tira_ofertas_close_xpath = "//*[@id='t296---bf22-tira-con-ofertas-en-home-btn-close']"
        self.cookie_aceptar_button_id = "onetrust-accept-btn-handler"
        self.help_button_xpath = "//*[@id='root_ibot']/div/div/div/button"
        self.vuelo_ida_input_name = "flight_origin"
        self.vuelo_destino_input_name = "flight_destiny"
        self.fecha_ida_input_name = "flight_hotel_round_date"
        self.fecha_vuelta_input_name = "flight_return_date"
        self.pasajeros_button_name = "flight_passengers"
        self.adulto_button_xpath = "//*[@id='people-counter-1']/ul/li[2]/div[2]/button[2]"
        self.children_button_xpath = "//*[@id='people-counter-1']/ul/li[5]/div[2]/button[2]"
        self.baby_button_xpath = "//*[@id='people-counter-1']/ul/li[6]/div[2]/button[2]"
        self.submit_button_id = "buttonSubmit1"

    def click_tira_oferta_close(self):
        # if self.driver.find_element(By.XPATH, self.tira_ofertas_close_xpath):
        self.driver.find_element(By.XPATH, self.tira_ofertas_close_xpath).click()

    def click_cookie_button(self):
        self.driver.find_element(By.ID, self.cookie_aceptar_button_id).click()

    def click_help_button(self):
        self.driver.find_element(By.XPATH, "//*[@id='root_ibot']/div/div/div/button").click()

    def enter_vuelo_ida(self, vuelo_ida):
        self.driver.find_element(By.NAME, self.vuelo_ida_input_name).clear()
        self.driver.find_element(By.NAME, self.vuelo_ida_input_name).send_keys(vuelo_ida)

    def enter_vuelo_destino(self, vuelo_destino):
        self.driver.find_element(By.NAME, self.vuelo_destino_input_name).clear()
        self.driver.find_element(By.NAME, self.vuelo_destino_input_name).send_keys(vuelo_destino)

    def enter_fecha_ida(self, fecha_ida):
        self.driver.find_element(By.NAME, self.fecha_ida_input_name).clear()
        self.driver.find_element(By.NAME, self.fecha_ida_input_name).send_keys(fecha_ida)

    def enter_fecha_vuelta(self, fecha_vuelta):
        self.driver.find_element(By.NAME, self.fecha_vuelta_input_name).clear()
        self.driver.find_element(By.NAME, self.fecha_vuelta_input_name).send_keys(fecha_vuelta)

    def click_pasajeros_button(self):
        self.driver.find_element(By.NAME, self.pasajeros_button_name).click()

    def click_adult_button(self, adult):
        i = 1
        while i < adult:
            self.driver.find_element(By.XPATH, self.adulto_button_xpath).click()
            i += 1

    def click_children_button(self, child):
        i = 0
        while i < child:
            self.driver.find_element(By.XPATH, self.children_button_xpath).click()
            i += 1

    def click_baby_button(self, baby):
        i = 0
        while i < baby:
            self.driver.find_element(By.XPATH, self.baby_button_xpath).click()
            i += 1

    def click_submit_button(self):
        self.driver.find_element(By.ID, self.submit_button_id).click()

    def get_button_fligh_text(self):
        valorpass = self.driver.find_element(By.NAME, self.pasajeros_button_name).text
        return valorpass
