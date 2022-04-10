from googletrans import Translator

translator = Translator()
result = translator.translate('հարազատ մարդիկ մահանում են', src='hy', dest='en')

print(result.src)
print(result.dest)
print(result.text)
result2 = translator.translate(result.text, src='en', dest='hy')


result2.text