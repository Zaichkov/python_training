from model.group import Group
import random


def test_delete_some_group(app, orm, check_ui):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = orm.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = orm.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups

    if check_ui:
        ui_list = app.group.get_group_list()
        orm_list = app.group.make_list_like_ui(new_groups)
        assert sorted(orm_list, key=Group.id_or_max) == sorted(ui_list, key=Group.id_or_max)
