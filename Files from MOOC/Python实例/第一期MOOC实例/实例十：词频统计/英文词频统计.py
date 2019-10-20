#英文词频统计

def gettxt():
    txt=open("","r").read()
    txt=txt.lower()
    for ch in '!@#$%^&*()_{}:?><,./;]\"[-+=\' ':
        txt=txt.replace(ch,repalce)
    return txt

hamlet=gettxt()
words=hamlet.split()
counts={}
for word in words:
    counts[word]=counts.get(words.0)+1
items=list(counts.items())  #转换为列表
items.sort(key=lambda x:x[1],reverse=True)
    
