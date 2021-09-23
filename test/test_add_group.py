from model.group import Group
import pytest
import re


# @pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, orm, json_groups, check_ui):
    group = json_groups
    old_groups = orm.get_group_list()
    app.group.create(group)
    new_groups = orm.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    if check_ui:
        ui_list = app.group.get_group_list()
        orm_list = app.group.make_list_like_ui(new_groups)
        assert sorted(orm_list, key=Group.id_or_max) == sorted(ui_list, key=Group.id_or_max)



