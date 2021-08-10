from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="myGroup", header="header"))
