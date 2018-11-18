import json
from Api import create_app
import pytest
from Api.models.database import DBConnect
from tests import test_base


# creating our test client
@pytest.fixture(scope='module')
def client():
    app = create_app(config_name='testing')
    test_client = app.test_client()

    # creating the database object
    db = DBConnect()
    db.create_tables()
    # establishing the application context
    cxt = app.app_context()
    cxt.push()
    yield test_client
    db.drop_tables('users', 'parcel_orders')
    cxt.pop()


def test_user_signup_has_empty_field(client):
    """test that checks for empty field in user input"""
    response = client.post('api/v1/auth/signup', data=json.dumps(test_base.empty_users))
    assert response.status_code == 400
    assert json.loads(response.data)['message'] == 'some fields are empty'


def test_to_check_for_invalid_users_and_password(client):
    """test that checks for invalid and username length"""
    response = client.post('api/v1/auth/signup', data=json.dumps(test_base.invalide_user))
    assert response.status_code == 400
    assert json.loads(response.data)['message'] == 'username and password should be atleast six chars'


def test_to_check_for_invalid_email(client):
    response = client.post('api/v1/auth/signup', data=json.dumps(test_base.invalide_email))
    assert response.status_code == 400
    assert json.loads(response.data)['message'] == 'invalid email'
