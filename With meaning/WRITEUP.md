# With meaning - Stegano, 100 баллов

Распакуем суперсекретный архив `to_agent_228.zip`, в нём лежит два файла:

`cipher`:

```
0.341  14.267  4.316  0.124  14.86  6.33  12.173  2.234  4.302  14.4  7.15  16.290  12.70  14.305  4.34  10.56  12.64  2.41  7.15  14.31  16.86  10.252  16.193  7.15  0.244  12.22  16.42  0.22  7.15  10.238  4.40  16.64  2.140  7.15  14.201  0.166  0.2  16.195  10.124  14.44  16.211  14.271  14.145  14.191  4.183  7.15  14.66  0.367  16.145  16.216  7.15  12.52  10.119  12.60  7.15  0.306  6.25  8.3
```

`Message.txt`:

```
Dissimilar admiration so terminated no in contrasted it. So by colonel hearted ferrars. Bed uncommonly his discovered for estimating far. Ecstatic elegance gay but disposed. Advantages entreaties mr he apartments do. Fortune day out married parties. Decisively advantages nor expression unpleasing she led met. Draw fond rank form nor the day eat. At none neat am do over will. How o

Detract yet delight written farther his general. If as increasing contrasted entreaties be. Their saved linen downs tears son add music. Sentiments two occasional affronting solicitude travelling and one contrasted. How one dull get busy dare far. Small for ask shade water manor think men begin. Sitting hearted on it without me. Steepest speaking up attended

Now summer who day looked our behind moment coming. Girl quit if case mr sing as no have. Indulgence contrasted sufficient to unpleasant in in insensible favourable. Took sold add play may none him few. We me rent been part what. Small for ask shade water manor think men begin. Fat new smallness few supposing suspici

// for (int i = 0; i < 228; i++) {
// 	 printf("EZ_TASK!\n");
// }

Made neat an on be gave show snug tore. Do play they miss give so up. Advantages entreaties mr he apartments do. Pain son rose more park way that. To sure calm much most long me mean. Hard do me sigh with west same lady. Dissimilar admiration so terminated no in contrasted it. Sentiments two occasional affronti

We me rent been part what. As mr started arrival subject by believe. Ecstatic elegance gay but disposed. Celebrated delightful an especially increasing instrument am. Is inquiry no he several excited am. Strictly numerous outlived kindness whatever on we no on addition. Up hung mr we give rest half. At none

To things so denied admire. Fortune day out married parties. Indulgence contrasted sufficient to unpleasant in in insensible favourable. So by colonel hearted ferrars. Decisively advantages nor expression unpleasing she led met. Draw from upon here gone add one. An stairs as be lovers uneasy. Dissimilar admiration so termina

Draw fond rank form nor the day eat. Decisively advantages nor expression unpleasing she led met. We leaf to snug on no need. Able rent long in do we. Fat new smallness few supposing suspicion two. Their saved linen downs tears son add music. Estate was tended ten boy nearer seemed. Dissimilar admiration so
```

Многабукаф, согласны. Смысла они особого не несут до тех пор, пока мы не заметим, что в каждой паре чисел первое варируется от 0 до 16, в то время, как строк в сообщении ровно 17. А что если второе число - это номер символа в строке?

Напишем восхитительный `solver.py`, который пытается получить исходное сообщение по описанной выше стратегии.

С таким скриптом мы были обречены на успех.

**Флаг:** `ytctf{uuuh_icansee_that_this_text_issosmisloy_good_job_m8}`
