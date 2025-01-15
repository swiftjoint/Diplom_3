from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 50).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_element_invisibility(self, wait_locator):
        element = self.driver.find_element(*wait_locator)
        WebDriverWait(self.driver, 100).until(expected_conditions.invisibility_of_element_located(element))

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 50).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def move_the_element_chrome(self, locator_element, locator_target):
        element = self.get_element(locator_element)
        target = self.get_element(locator_target)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(element, target).perform()

    def get_element(self, locator):
        return self.find_element_with_wait(locator)

    def drag_and_drop_element_firefox(self, locator_from, locator_to):
        source_element = self.find_element_with_wait(locator_from)
        target_element = self.find_element_with_wait(locator_to)
        script = """
                function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
                    var dataTransfer = new DataTransfer();
                    var dragStartEvent = new DragEvent('dragstart', {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dataTransfer
                    });
                    sourceNode.dispatchEvent(dragStartEvent);

                    var dropEvent = new DragEvent('drop', {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dataTransfer
                    });
                    destinationNode.dispatchEvent(dropEvent);

                    var dragEndEvent = new DragEvent('dragend', {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dataTransfer
                    });
                    sourceNode.dispatchEvent(dragEndEvent);
                }
                simulateHTML5DragAndDrop(arguments[0], arguments[1]);
                """
        self.driver.execute_script(script, source_element, target_element)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_counter_value(self, locator):
        counter_element = WebDriverWait(self.driver, 50).until(
            expected_conditions.visibility_of_element_located(locator)
        )
        return int(counter_element.text)

    def go_to_url(self, url):
        self.driver.get(url)

    def is_element_visible(self, locator):
        element = self.find_element_with_wait(locator)
        return element.is_displayed()

    def wait_element_invisibility_base(self, wait_locator):
        WebDriverWait(self.driver, 50).until(
            expected_conditions.invisibility_of_element_located(wait_locator)
        )
