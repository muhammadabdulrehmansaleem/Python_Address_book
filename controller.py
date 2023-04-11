from model import dbHandler
db=dbHandler("localhost","root","1234566","addressbook")
def insert_record(l1):
    db.insert_contact(l1)
def get_record():
    l1=db.show_contacts()
    return l1
def get_byname(name):
    l1=db.get_Contact_byName(name)
    # print(l1)
    return l1
def register_user(l1):
    status=db.insert_user(l1)
    if status==True:
        return True
    else:
        return False
def verify_login(l1):
    status=db.verify_user(l1)
    if status==True:
        return True
    else:
        return False
def delete_contact_record(name):
    status=db.delete_contact(name)
    if status==True:
        return True
    else:
        return False
def update_contact_info(id,l1):
    status=db.update_contact(id,l1)
    if status==True:
        return True
    else:
        return False
def get_info(id):
    l1=db.get_contact_by_id(id)
    return l1
