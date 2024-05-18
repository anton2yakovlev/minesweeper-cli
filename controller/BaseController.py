from model.Model import Model
from view.BaseView import BaseView


class BaseController:
    def __init__(self, model: Model, view: BaseView):
        self.model = model
        self.view = view
        

    def handle_input(self):
        raise NotImplementedError(
            "Метод handle_input должен быть реализован в подклассе."
        )
    
    def render(self):
        raise NotImplementedError(
            "Метод render должен быть реализован в подклассе."
        )

    def main_loop(self):
        raise NotImplementedError("Метод main_loop должен быть реализован в подклассе.")

    def run(self):
        raise NotImplementedError("Метод run должен быть реализован в подклассе.")
