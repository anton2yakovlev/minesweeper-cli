class BaseView:

    def render(self):
        raise NotImplementedError("Метод render должен быть реализован в подклассе.")
    
    def read_event(self):
        raise NotImplementedError("Метод read_event должен быть реализован в подклассе.")

