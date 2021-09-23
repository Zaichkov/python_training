import pymysql.cursors
from fixture.orm import ORMFixture
from model.group import Group


db = ORMFixture(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    l = db.get_contact_list()
    for c in l:
        print(c)


finally:
    pass  # db.destroy()
