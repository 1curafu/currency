from rest_framework import serializers
from currency.models import Rate, Source, ContactUs


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'id',
            'buy',
            'sale',
            'created',
            'source',
            'currency'
        )


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = (
            'id',
            'name',
            'source_url',
            'code_name'
        )


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = (
            'name',
            'email',
            'subject',
            'message',
        )

    def _send_mail(self, validated_data):
        subject = 'User ContactUs'
        message = f'''
                Request from: {validated_data['name']},
                Reply to: {validated_data['email']},
                Subject: {validated_data['subject']},
                Message: {validated_data['message']},
                '''
        from currency.tasks import send_mail
        send_mail.delay(subject, message)

    def create(self, validated_data):
        self._send_mail(validated_data)
        return ContactUs.objects.create(**validated_data)
