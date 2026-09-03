from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

class CoordinateClick :

    def coordinate_click(driver, x, y, label):
        if label:
            print(f"Clicking button: {label}")

        finger = PointerInput("touch", "finger")
        actions = ActionBuilder(driver, mouse=finger)

        actions.pointer_action.move_to_location(x, y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.pointer_up()

        actions.perform()


