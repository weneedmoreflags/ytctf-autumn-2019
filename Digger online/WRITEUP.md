# Digger online - Web, 50 балов

В тексте условия можно заметить жирнейший намёк на то, что нам нужно найти некий `DNS DIG`.

Открываем любой из перечисленных сервисов (например, [этот](https://2whois.ru/?t=dig)) и занимаемся раскопками домена `ctf.yummytacos.me`:

```
; <<>> DiG 9.9.4-RedHat-9.9.4-73.el7_6 <<>> ctf.yummytacos.me IN ANY +retry=2 +time=5
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 16636
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;ctf.yummytacos.me.		IN	ANY

;; ANSWER SECTION:
ctf.yummytacos.me.	1798	IN	CNAME	evgfilim1.yummytacos.me.
ctf.yummytacos.me.	1798	IN	TXT	"ytctf{u_ar3_a_d1gg3r_MASTER}"

;; Query time: 68 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Sat Oct 12 20:59:39 MSK 2019
;; MSG SIZE  rcvd: 111
```

Ничего не понятно, но очень интересно!

**Флаг:** `ytctf{u_ar3_a_d1gg3r_MASTER}`
