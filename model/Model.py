class BaseModel:
    """Базовый класс для моделей."""
    def save(self):
        raise NotImplementedError("Метод save должен быть реализован в подклассе.")

    def load(self):
        raise NotImplementedError("Метод load должен быть реализован в подклассе.")
