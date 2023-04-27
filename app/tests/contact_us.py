from currency.models import ContactUs


def test_get_contact_us(client):
    response = client.get('/currency/contact/create/')
    assert response.status_code == 200


def test_post_empty_form_200(client):
    response = client.post('/currency/contact/create/')
    assert response.status_code == 200


def test_post_empty_form_errors(client):
    response = client.post('/currency/contact/create/')
    assert response.context_data['form']._errors == {
        'name': ['This field is required.'],
        'email': ['This field is required.'],
        'subject': ['This field is required.'],
        'message': ['This field is required.']
    }


def test_post_invalid_email_200(client):
    payload = {
        'name': 'Misha',
        'email': 'INVALID_EMAIL',
        'subject': 'This field is required.',
        'message': 'This field is required.'
    }
    response = client.post('/currency/contact/create/', data=payload)
    assert response.status_code == 200


def test_post_invalid_email_error(client):
    payload = {
        'name': 'Misha',
        'email': 'INVALID_EMAIL',
        'subject': 'This field is required.',
        'message': 'This field is required.'
    }
    response = client.post('/currency/contact/create/', data=payload)
    assert response.context_data['form']._errors == {'email': ['Enter a valid email address.']}


def test_post_valid_data(client, mailoutbox, settings):
    initial_count = ContactUs.objects.count()
    payload = {
        'name': 'Misha',
        'email': 'example@example.com',
        'subject': 'This field is required.',
        'message': 'This field is required.'
    }
    response = client.post('/currency/contact/create/', data=payload)
    assert response.status_code == 302
    assert response['location'] == '/currency/contact/list/'
    assert ContactUs.objects.count() == initial_count + 1
    assert len(mailoutbox) == 1
    assert mailoutbox[0].from_email == settings.DEFAULT_FROM_EMAIL
