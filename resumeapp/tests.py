from django.core.mail import send_mail
from django.test import TestCase, override_settings
from django.core.mail import EmailMessage

@override_settings(
    EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend',
    EMAIL_HOST_USER='test@example.com'
)
class EmailTest(TestCase):
    def test_send_mail_with_reply_to(self):
        email = EmailMessage(
            subject='Contact Form Test',
            body='Test message content',
            from_email='test@example.com',
            to=['receiver@example.com'],
            reply_to=['replyto@example.com'],
        )
        email.send(fail_silently=False)

        from django.core import mail
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].reply_to, ['replyto@example.com'])
