from currency.models import Source


def test_get_api_rate_list(api_client):
    response = api_client.get('/v1/api/currency/rates/')
    assert response.status_code == 200


def test_pots_api_rate_list(api_client):
    response = api_client.post('/v1/api/currency/rates/')
    assert response.status_code == 400
    assert response.json() == {
        'buy': ['This field is required.'],
        'sale': ['This field is required.'],
        'source': ['This field is required.']
    }


def test_get_api_source_list(api_client):
    response = api_client.get('/v1/api/currency/sources/')
    assert response.status_code == 200


def test_post_source_list(api_client):
    response = api_client.post('/v1/api/currency/sources/')
    assert response.status_code == 400
    assert response.json() == {
        'name': ['This field is required.'],
        'source_url': ['This field is required.'],
        'code_name': ['This field is required.']
    }


def test_post_source_create(api_client):
    data = {
        'id': 5,
        'name': 'Test',
        'source_url': 'https://www.test.com',
        'code_name': 'dsadewq'
    }
    response = api_client.post('/v1/api/currency/sources/', data=data)
    assert response.status_code == 201
    assert response.json() == data


def test_post_source_update(api_client):
    data = {
        'id': 4,
        'name': 'test1',
        'source_url': 'https://www.test1.com',
        'code_name': 'test1'
    }
    response = api_client.put('/v1/api/currency/sources/4/', data=data)
    assert response.status_code == 200
    assert response.json() == data


def test_delete_source(api_client):
    Source.objects.create(
        id=5,
        name='test5',
        source_url='https://www.test5.com',
        code_name='test5'
    )
    response = api_client.delete('/v1/api/currency/sources/5/')
    assert response.status_code == 204
    assert Source.objects.count() == 4
