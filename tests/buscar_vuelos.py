from selenium import webdriver
import time
import unittest
from pages.buscarVuelosPage import BuscarVuelosPage
from pages.errorPage import ErrorPage
from ddt import ddt, file_data
import HtmlTestRunner


@ddt
class BuscarVuelosTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path="driver/chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://www.iberia.com/")

    @file_data("../BD/datos.json")
    def test_buscar_vuelo(self, vueloida, vueloreg, fechaida, fechareg, adult, child, baby):
        driver = self.driver
        formbusqueda = BuscarVuelosPage(driver)
        err_page = ErrorPage(driver)
        formbusqueda.click_cookie_button()
        formbusqueda.click_help_button()
        formbusqueda.enter_vuelo_ida(vueloida)
        formbusqueda.enter_vuelo_destino(vueloreg)
        formbusqueda.enter_fecha_ida(fechaida)
        formbusqueda.enter_fecha_vuelta(fechareg)
        formbusqueda.click_pasajeros_button()
        formbusqueda.click_adult_button(adult)
        formbusqueda.click_children_button(child)
        formbusqueda.click_baby_button(baby)
        sumpass = formbusqueda.get_button_fligh_text()
        sumint = int(adult) + int(child) + int(baby)
        self.assertEqual(sumpass, str(sumint) + ' Pasajeros')
        formbusqueda.click_submit_button()
        time.sleep(3)
        message = err_page.check_error_title()
        self.assertEqual(message, "Lo sentimos,")

    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()
        print("Test completado")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="reports"))
