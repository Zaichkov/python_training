import pymysql.cursors
from fixture.orm import ORMFixture
from model.group import Group


db = ORMFixture(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    l = db.get_contacts_not_in_group(Group(id='220'))
    print(len(l))
    for item in l:
        print(item)


finally:
    pass  # db.destroy()
