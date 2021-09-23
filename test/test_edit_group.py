from model.group import Group
import random


def test_edit_some_group(app, orm, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = orm.get_group_list()
    group_for_edit = random.choice(old_groups)
    group = Group(name="super_group", footer="fooooooter", id=group_for_edit.id)
    app.group.edit_group_by_id(group.id, group)
    new_groups = orm.get_group_list()
    # old_groups.remove(group_for_edit)
    # old_groups.append(group)
    old_groups = (g if g.id != group_for_edit.id else group for g in old_groups)

    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    if check_ui:
        ui_list = app.group.get_group_list()
        orm_list = app.group.make_list_like_ui(new_groups)
        assert sorted(orm_list, key=Group.id_or_max) == sorted(ui_list, key=Group.id_or_max)
