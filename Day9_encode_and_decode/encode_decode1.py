with open('input.txt','r',encoding='utf-8') as en:
    c=en.read()
    with open('output.txt','w',encoding='utf-16') as de:
        de.write(c)
        