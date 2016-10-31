# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_login_add_group(app):
        app.open_home_page()
        app.login(username="admin", password="secret")
        app.create_group(Group(name="new_group", header="description", footer="description_2"))
        app.logout()

def test_login_add_group_empty(app):
        app.open_home_page()
        app.login(username="admin", password="secret")
        app.create_group(Group(name="", header="", footer=""))
        app.logout()
