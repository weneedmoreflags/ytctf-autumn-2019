# Go Back - Recon, 150 баллов
Давайте вернемся на [страницу регистрации](https://ctf.yummytacos.me/) и посмотрим, нет ли там что-то интересного. И в самом деле, находим интересный скрипт:
```javascript
var q = document.getElementById('q'),
    s = window.screen,
    hh = document.body.offsetHeight,
    w = q.width = s.width,
    h = q.height = hh,
    p = Array(256).join(1).split(''),
    c = q.getContext('2d'),
    q = 0,
    m = Math;
    ki = [5, 14, 28, 30, 47, 66, 69, 95, 101, 140];
setInterval(function() {
    c.fillStyle = 'rgba(0,0,0,0.05)';
    c.fillRect(0, 0, w, h);
    c.fillStyle = 'rgba(0,255,0,0.4)';
    let o = [121,116,99,116,102,123,103,108,97,100,50,115,101,101,95,117,95,97,103,97,105,110,95,109,121,95,115,119,101,101,116,95,58,51,125];
    p = p.map(function(v, i) {
        r = m.random();
        let k = m.floor(65 + r * 58);

        for (let si of ki){
            if (si == i){
                let zz = v / 10 % o.length;
                k = zz < 5 || o[zz] < 97 || o[zz] > 122 ? o[zz] : o[zz] - 32;
            }
        }
        c.fillText(String.fromCharCode(k), i * 10, v);
        v += 10;
        return v > 256*4 + r*1e4 ? 0 : v
    })
 }, 33)
```
Видим массив `o`, состоящий из чисел, подозрительно похожих на ASCII-коды. Посмотрим, что в нем:
```python
>>> o = [121,116,99,116,102,123,103,108,97,100,50,115,101,101,95,117,95,97,103,97,105,110,95,109,121,95,115,119,101,101,116,95,58,51,125]
>>> ''.join(map(chr, o))
'ytctf{glad2see_u_again_my_sweet_:3}'
>>> 
```
Остается только заметить, что строка `k = zz < 5 || o[zz] < 97 || o[zz] > 122 ? o[zz] : o[zz] - 32;` делает буквы внутри флага заглавными. Массив `ki` отвечает за то, в каких столбцах фона будет "падать" флаг.

**Флаг:** `ytctf{GLAD2SEE_U_AGAIN_MY_SWEET_:3}`
