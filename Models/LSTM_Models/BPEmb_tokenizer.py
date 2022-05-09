 """"
 #!/usr/bin/env python
 """

from bpemb import BPEmb


armbpemb = BPEmb(lang="hy", vs=10000, dim=300)

text = 'Բարև ձեզ, ես այսօր ներկա եմ դասին։ Վաղը մենք համալսարանական ուրախություն'

subwords = armbpemb.encode(text)
['PAD']

armbpemb.encode(text)
print(" ".join(subwords))

armbpemb.decode(['▁բար', 'եւ', '▁ձ', 'եզ', ',', '▁ես', '▁այսօր', '▁ներկա', '▁եմ', '▁դաս', 'ին',
                 '։', '▁վաղ', 'ը', '▁մենք', '▁համալսարան', 'ական', '▁ուրախ', 'ություն'])

len(armbpemb.words)