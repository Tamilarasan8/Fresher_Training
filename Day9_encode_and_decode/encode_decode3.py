with open('japanese_input.txt','r',encoding='utf-8') as lan:
    c=lan.read()
    with open('japanese_output.txt','w',encoding='utf-8') as de:
        de.write(c)