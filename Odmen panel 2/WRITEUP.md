# Odmen panel 2 - Web, 150 баллов [Дорешивание]
Как и в первой части, находим файл `robots.txt`. Находим интересный файл [1](https://odmen-panel.ctf.yummytacos.me/tools/generate_password.js) и [2](https://odmen-panel.ctf.yummytacos.me/private/users.json).
В первом находим общую информацию о хэше:
```javascript
const bcrypt = require('bcrypt');
const saltRounds = 5;
const password = 'ytctf{*}'; // please make passwords 12 or less characters
bcrypt.hash(password, saltRounds, function(err, hash) {
    if (err) throw err;
    process.stdout.write(hash);
});
```
Во втором файле находим хэш пользователя `odmen` (а чуть позже - и `admin`):
```json
{
    "odmen" : { 
        "password" : "$2b$05$qcKaRj9zpRbsWfyZomwNJOQPJ4OyfbmUlxAC3VdxLUeKXvP3jkbAC"
    },
    "admin" : {
        "password" : "$2b$05$auE0zIov9BdE/AjGocljzudbnCN89A8Yp4W37vEpiD6UJ5S9DA2AW"
    }
}
```
Как видим, скрипт генерирует bcrypt-хэш, причем, судя по комментарию, длина внутри `ytctf{}` не больше пяти символов. Что ж, пробуем подобрать недостающую часть с помощью Hashcat, с каждый новым запуском увеличивая число символов в скобках. В итоге придем к выводу, что число символов внутри скобочек - 3. 
```
C:\Users\exp101t\Documents\hashcat> hashcat64.exe -a 3 -m 3200 ytctf-hash.txt ytctf{?a?a?a}
```
Ждем немного и получаем флаг. 

**Флаг:** `ytctf{J0j}`
