# numdeco
Number Decorator (numdeco)

```
#importing libraries 
from numdeco import deco, decoco
from pytube import YouTube

#YouTube Link
ytLink = 'https://youtu.be/7wtfhZwyrcc'
video = YouTube(ytLink)

#video name and real time views
print(str(video.title)+'\n'+'Real time views : '+str(video.views))

#video views using deco
deco(video.views)

#video views using decoco
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
from numdeco import deco, decoco

deco(1000000000000)

decoco(1000000000000)
```
>1T 000B 000M 000K 000
>
>1,000,000,000,000

```
from numdeco import deco, decoco

deco(100000000000)

decoco(100000000000)
```
>100B 000M 000K 000
>
>100,000,000,000

```
from numdeco import deco, decoco

deco(10000000000)

decoco(10000000000)
```
>10B 000M 000K 000
>
>10,000,000,000

```
from numdeco import deco, decoco

deco(1000000000)

decoco(1000000000)
```
>1B 000M 000K 000
>
>1,000,000,000

```
from numdeco import deco, decoco

deco(100000000)

decoco(100000000)
```
>100M 000K 000
>
>100,000,000

```
from numdeco import deco, decoco

deco(10000000)

decoco(10000000)
```
>10M 000K 000
>
>10,000,000 

```
from numdeco import deco, decoco

deco(1000000)

decoco(1000000)
```
>1M 000K 000
>
>1,000,000

```
from numdeco import deco, decoco

deco(100000)

decoco(100000)
```
>100K 000
>
>100,000 

```
from numdeco import deco, decoco

deco(10000)

decoco(10000)
```
>10K 000
>
>10,000 

```
from numdeco import deco, decoco

deco(1000)

decoco(1000)
```
>1K 000
>
>1,000  

```
from numdeco import deco, decoco

deco(100)

decoco(100)
```
>0.1K
>
>0.100  

```
from numdeco import deco, decoco

deco(10)

decoco(10)
```
>0.01K
>
>0.010  

```
from numdeco import deco, decoco

deco(1)

decoco(1)
```
>1
>
>1
