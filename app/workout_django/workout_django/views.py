from django.views import View

from .handler.Handler import AnotherHandler, CompositeHandler, SimpleHandler


class CompositeView(View):
    def get(self, request):
        # Создаем композитный обработчик
        composite = CompositeHandler()
        composite.add(SimpleHandler())
        composite.add(AnotherHandler())

        # Добавляем еще один обработчик динамически
        if True:
            composite.add(AnotherHandler())

        # Вызываем цепочку обработчиков
        return composite.handle(request)