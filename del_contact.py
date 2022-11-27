import json
def del_cont(text):
    with open('sw_templates.json') as f:
        contact_book=json.load(f)
    if text in contact_book:
        del contact_book[text]
        result=True
    else:
        result=False
    with open('sw_templates.json','w') as f:
        json.dump(contact_book, f)
    return result


