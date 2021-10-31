# numdeco
Number Decorator (numdeco)

```
from numdeco import deco, decoco, indeco, indecoco

deco(10000000)
decoco(10000000)

indeco(10000000)
indecoco(10000000)
```
>10M 000K 000
>
>10,000,000
>
>1C 00L 00T 000
>
>1,00,00,000
```
from numdeco import deco, decoco, indeco, indecoco

deco(1000000)
decoco(1000000)

indeco(1000000)
indecoco(1000000)
```
>1M 000K 000
>
>1,000,000
>
>10L 00T 000
>
>10,00,000
>

```
from numdeco import deco, decoco
from pytube import YouTube

ytLink = 'https://youtu.be/7wtfhZwyrcc'
video = YouTube(ytLink)

print(str(video.title)+'\n'+'Real time views : '+str(video.views))
deco(video.views)
decoco(video.views)
```

>Imagine Dragons - Believer
>
>Real time views : 2060472087
>
>2B 060M 472K 087
>
>2,060,472,087

```
from numdeco import indeco, indecoco
from pytube import YouTube

ytLink = 'https://youtu.be/7wtfhZwyrcc'
video = YouTube(ytLink)

print(str(video.title)+'\n'+'Real time views : '+str(video.views))
indeco(video.views)
indecoco(video.views)
```

>Imagine Dragons - Believer
>
>Real time views : 2060554580
>
>206C 05L 54T 580
>
>206,05,54,580
