import json

def check_value_numbers(text):
    symbols=['1','2','3','4','5','6','7','8','9','0','(',')','-']
    check=text.replace(' ','')
    result=True
    if ',' in check:
        check=check.split(',')
        for i in check:
            for j in i:
                if j not in symbols:
                    result=False
                    break
    else:
        for i in check:
            if i not in symbols:
                result=False
                break
    return result

def list_phones(text):
    text=text.replace(' ','')
    if ',' in text:
        result=text.split(',')
    else:
        result=[]
        result.append(text)
    return result

def check_mail(text):
    result=True
    if '@' not in text:
        result=False
    return result

def check_birthday(text):
    list_symbols=['1','2','3','4','5','6','7','8','9','0','.']
    result=True
    for i in text:
        if i not in list_symbols:
            result=False
            break
    return result

def add_contact_in_dict(contact):
    params_dict={}
    params_dict['phones']=contact[1]
    params_dict['mail']=contact[2]
    params_dict['birthday']=contact[3]
    return contact[0],params_dict


def add_in_book(name,params):
    with open('sw_templates.json') as f:
        contact_book = json.load(f)
    contact_book[name] = params
    with open('sw_templates.json', 'w') as f:
        json.dump(contact_book, f)
    return
