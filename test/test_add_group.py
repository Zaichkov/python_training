from model.group import Group
import pytest
import random
import string
import re


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*3
    return prefix + "".join([random.choice(symbols) for _ in range(random.randrange(maxlen))])


test_data = [
    Group(name=random_string("name", 15), header=random_string("header", 15), footer=random_string("footer", 15)),
    Group(name=random_string("name", 20), header=random_string("header", 20), footer=random_string("footer", 20))
]


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()

    new_groups = app.group.get_group_list()
    group.name = re.sub(r'\s+', ' ', group.name).strip()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
