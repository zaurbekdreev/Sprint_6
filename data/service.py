class Service:

    def __init__(self, base_url: str):
        self._base_url = base_url.rstrip('/')

    @property
    def base_url(self) -> str:
        return self._base_url

    def endpoint(self, path: str) -> str:
        return f"{self.base_url}/{path.lstrip('/')}"

    @property
    def order(self) -> str:
        """URL для логина."""
        return self.endpoint('order')

    @property
    def track(self) -> str:
        """URL для логина."""
        return self.endpoint('track')


qa_scooter_service = Service('https://qa-scooter.praktikum-services.ru')
