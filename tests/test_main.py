from starlette.testclient import TestClient
from tibiacrud.main import app
from faker import Faker

teste = TestClient(app)
fake = Faker()
class TestMain():
    def test_post_with_a_valid_payload(self):
        nickname = fake.name()
        payload = {'nickname': nickname, 'level': 33, 'vocation': 'druid'}

        creation_player_post = teste.post('/players', json=payload)
        creation_player_json = creation_player_post.json()
        assert creation_player_json['Message'] == 'Player Created'
        assert creation_player_post.status_code == 201


    def test_post_with_a_invalid_payload(self):

        invalid_payload = {'lambe_minhas_bola': 'hahaha'}

        creation_player_post = teste.post('/players', json=invalid_payload)

        assert creation_player_post.status_code == 422


    def test_get_player_with_a_valid_id(self):
        nickname = fake.name()
        payload = {
            'nickname': nickname,
            'level': 33,
            'vocation': 'druid',
        }

        create_player_post = teste.post('/players', json=payload)
        create_player_json = create_player_post.json()
        player_id = create_player_json['_id']

        get_player = teste.get(f'/player/{player_id}')

        expected_data = {
            'nickname': nickname,
            'level': 33,
            'vocation': 'druid',
        }

        get_player_json = get_player.json()
        assert get_player_json == expected_data
        assert get_player.status_code == 200


    def test_get_player_with_a_invalid_nickname(self):

        player_id = '0123456789ab0123456789ab'
        get_player = teste.get(f'/player/{player_id}')
        get_player_json = get_player.json()

        assert get_player.status_code == 404
        assert get_player_json['Message'] == 'Player Not Found'


    def test_put_with_a_valid_nickname(self):
        nickname = fake.name()
        payload = {'nickname': nickname, 'level': 33, 'vocation': 'druid'}

        create_player_post = teste.post('/players', json=payload)
        create_player_json = create_player_post.json()

        player_id = create_player_json['_id']

        another_nickname = fake.name()
        update_player = teste.put(
            f'/player/{player_id}', json={'nickname': another_nickname}
        )
        update_player_json = update_player.json()

        assert update_player_json['Message'] == 'Player Modified'
        assert update_player.status_code == 200


    def test_put_with_a_invalid_nickname(self):

        player_id = '0123456789ab0123456789ab'
        get_player = teste.get(f'/player/{player_id}')
        get_player_json = get_player.json()
        assert get_player.status_code == 404
        assert get_player_json['Message'] == 'Player Not Found'

        update_player = teste.put(
            f'/player/{player_id}', json={'nickname': 'Its Lillia Time'}
        )
        update_player_json = update_player.json()
        assert update_player_json['Message'] == 'Error while reading database'
        assert update_player.status_code == 404


    def test_delete_with_a_valid_nickname(self):
        nickname = fake.name()
        payload = {
            'nickname': nickname,
            'level': 33,
            'vocation': 'druid',
        }

        create_player_post = teste.post('/players', json=payload)
        create_player_json = create_player_post.json()
        player_id = create_player_json['_id']

        delete_player = teste.delete(f'/player/{player_id}')
        delete_player_json = delete_player.json()

        assert delete_player.status_code == 200
        assert delete_player_json['Message'] == 'Player Deleted'


    def test_delete_with_a_invalid_nickname(self):

        player_id = '0123456789ab0123456789ab'
        get_player = teste.get(f'/player/{player_id}')
        assert not get_player

        delete_player = teste.delete(f'/player/{player_id}')
        delete_player_json = delete_player.json()

        assert delete_player.status_code == 404
        assert delete_player_json['Message'] == 'Player Not Found'
