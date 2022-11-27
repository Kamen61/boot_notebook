import json
def show():
    with open('sw_templates.json') as f:
        contact_book=json.load(f)
    result=''
    for i,j in contact_book.items():
        result+=i+'\n'
        for k,n in j.items():
            if isinstance(n,list):
                result+=k+' : '+' , '.join(n)+'\n'
            else:
                result+=k+' : '+n+' \n'
        result+='\n'+'\n'
    result=result[:-4]
    return result

def serch_in_book(name):
    with open('sw_templates.json') as f:
        contact_book=json.load(f)
    result=False
    if name in contact_book:
        result=name+'\n'
        for i,j in contact_book[name].items():
            if isinstance(j,list):
                result+=i+' : '+' , '.join(j)+'\n'
            else:
                result+=i+' : '+j+' \n'
    return result


