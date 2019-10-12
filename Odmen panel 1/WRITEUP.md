# Odmen panel 1 - Web, 50 баллов

Итак, мы попали на на замечательный сайт `https://odmen-panel.ctf.yummytacos.me/`. Не знаю, как вам, а нам интересно, что же одмен хотел скрыть от поисковых систем.

Взглянём на файл `https://odmen-panel.ctf.yummytacos.me/robots.txt`:

```
User-agent: *
Allow: /public/
Disallow: /app.js
Disallow: /views/all.ejs
Disallow: /views/error.ejs
Disallow: /views/index.ejs
Disallow: /views/odmen.ejs
Disallow: /routes/all.js
Disallow: /routes/index.js
Disallow: /private/users.json
Disallow: /server.js
Disallow: /node_modules
Disallow: /public/tacos.txt
Disallow: /images/loading.svg
Disallow: /tools/generate_password.js
```

Казалось бы, причём тут вообще флаг. Попробуем посмотреть, что можно нарыть в этих файлах.

Наше внимание привлёк `https://odmen-panel.ctf.yummytacos.me/routes/all.js`:

```
var express = require('express');
var router = express.Router();
var path = require('path'); 
var fs = require('fs');

router.all('/odmen', function(req, res, next){
    if (req.session.user != undefined && req.session.user.login != undefined){
        res.render('odmen');
    } else {
        res.status(418);
        res.render('error', { statusCode: 418 });
    }
})

router.all('/get_a_super_secret_flag_that_is_hidden_in_the_source_code', function(req, res, next){
    let flag = "ytctf{we_hid3_flags_in_source_c0des_yay}";
    res.send(flag);
})

router.all('/*', function(req, res, next) {
    fs.readFile('.' + req.originalUrl, function(err, contents) {
        if (err){
            res.status(404);
            res.render('error', { statusCode: 404 });
        } else {
            res.render('all', {data: contents.toString()});
        }
    });
});


module.exports = router;
```

А вот и очень надёжно спрятанный флаг.

**Флаг:** `ytctf{we_hid3_flags_in_source_c0des_yay}`
