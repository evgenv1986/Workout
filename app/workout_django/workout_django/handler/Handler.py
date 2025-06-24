from django.http import HttpRequest, HttpResponse

class BaseHandler:
    def handle(self, request: HttpRequest) -> HttpResponse:
        raise NotImplementedError()
    
class SimpleHandler(BaseHandler):
    def handle(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse("SimpleHandler: Обработка запроса")

class AnotherHandler(BaseHandler):
    def handle(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse("AnotherHandler: Другая обработка")
    
class CompositeHandler(BaseHandler):
    def __init__(self):
        self._handlers = []

    def add(self, handler: BaseHandler):
        self._handlers.append(handler)
        return self  # Для цепочки вызовов

    def handle(self, request: HttpRequest) -> HttpResponse:
        responses = []
        for handler in self._handlers:
            response = handler.handle(request)
            responses.append(response.content.decode())
        
        return HttpResponse("<br>".join(responses))