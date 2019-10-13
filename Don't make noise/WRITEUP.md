# Don't make noise - Stegano, 150 баллов [Дорешивание]
Если открыть картинку в Paint и присмотреться, то можно заметить, что в картинке используется не так много различных цветов. Давайте посмотрим, сколько именно. 
```python
>>> from PIL import Image
>>> 
>>> img = Image.open('subst.png')
>>> pixels = []
>>> 
>>> for i in range(64):
...     for j in range(64):
...         pixel = img.getpixel((j, i))
...         if pixel not in img:
...             pixels.append(pixel)
...
>>> len(pixels)
26
>>> 
```
Как видим, число различных пикселей совпадает с количеством букв в английском алфавите. Сделаем смелое предположение, что каждый пиксель кодирует какую-то букву.
Пусть, для определенности, буква будет определяться позицией очередного пикселя в `pixels`
```python
>>> result = ''
>>> 
>>> for i in range(64):
...     for j in range(64):
...         index = pixels.index(img.getpixel((j, i)))
...         result += chr(ord('a') + index)
...
>>> print(result)
abcdefghidjfkejlmnlgagmgahbcafkodaljpogkhqhrobcdefgabineskackmbaglhrftjabgougjdodoftjcoqsagkcafkodgougjcc
hdqabighjrauoqlelgopgkombaglpjenolabitotoggodlgkophlgchpphbfjadlhrtoggodlgdaftoglhrtoggodlpaugmdolhrgkojn
hvojbqlhrhdgkgkodocoavodqocafkodlgkogougnefodrhdpabigkoabvodlolmnlgagmgahblmnlgagmgahbcafkodlcjbnochpfjdo
qsagkgdjblfhlagahbcafkodlegcgrbacolmnlgagmgahbcafkodabfbiabjgdjblfhlagahbcafkodgkombaglhrgkoftjabgougjdod
ojddjbioqabjqarrodobgjbqmlmjttewmagochpftouhdqodnmggkombaglgkoplotvoljdotorgmbckjbioqnechbgdjlgabjlmnlgag
mgahbcafkodgkombaglhrgkoftjabgougjdodogjaboqabgkoljpolowmobcoabgkocafkodgougnmggkombaglgkoplotvoljdojtgod
oqgkodojdojbmpnodhrqarrodobggefolhrlmnlgagmgahbcafkodargkocafkodhfodjgolhblabitotoggodlagalgodpoqjlapftol
mnlgagmgahbcafkodjcafkodgkjghfodjgolhbtjdiodidhmflhrtoggodlalgodpoqfhteidjfkacjphbhjtfkjnogaccafkodmlolra
uoqlmnlgagmgahbhvodgkoobgadopolljioskodojljfhtejtfkjnogaccafkodmloljbmpnodhrlmnlgagmgahbljgqarrodobgfhlag
ahblabgkopolljioskodojmbagrdhpgkoftjabgougalpjffoqghhbohrlovodjtfhllanatagaolabgkocafkodgougjbqvacovodljl
mnlgagmgahbhrlabitotoggodllofjdjgotelapftolmnlgagmgahbcjbnoqophblgdjgoqnesdagabihmggkojtfkjnogablhpohdqod
ghdofdolobggkolmnlgagmgahbgkalalgodpoqjlmnlgagmgahbjtfkjnoggkocafkodjtfkjnogpjenolkargoqhddovodloqcdojgab
igkocjoljdjbqjgnjlkcafkodldolfocgavotehdlcdjpntoqabjphdochpftourjlkahbabskackcjloagalcjttoqjpauoqjtfkjnog
hdqodjbioqjtfkjnoggdjqagahbjttepauoqjtfkjnoglpjenocdojgoqneradlgsdagabihmgjxoeshdqdophvabidofojgoqtoggodl
abaggkobsdagabijttgkodopjababitoggodlabgkojtfkjnogabgkomlmjthdqodmlabigkallelgopgkoxoeshdqyondjliavolmlgk
orhtthsabijtfkjnogljtgkhmikgkogdjqagahbjtxoeshdqpogkhqrhdcdojgabijpauoqlmnlgagmgahbjtfkjnogallapftojlodah
.........................................................................................................
>>> 
```
