from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Привет, спасибо за ревью! Не получилось найти тебя в Пачке.
        # Не совсем понял, что тут имелось в виду. Насколько я понял,
        # request.user.is_authenticated выдаёт False, если пользователь
        # не аутентифицирован и наоборот. Следовательно, если пишу
        # obj.author == request.user.is_authenticated, тесты валятся.
        # Этот пермишен работает не правильно и не позволяет изменять
        # посты и комментарии, то есть не проверяет, что пользователь
        # авторизирован. Если оставляю только or request.user.is_authenticated
        # валятся тесты в тех местах, где нужно запретить пользователю
        # редактировать посты и комментарии если пользователь - не автор.
        # Единственное, до чего додумался - ниже, как бы дополнительно
        # проверил, что пользователь аутентифицирован.
        # Подскажи пожалуйста, что имелось в виду. Спасибо!
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
                and obj.author == request.user)
