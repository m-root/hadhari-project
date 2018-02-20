from django import forms
from core.models import Daycare,Owner,Organisation
from authentication.models import Account
from django.template.defaultfilters import slugify
from django.template import loader

from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMultiAlternatives
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

class DaycareForm(forms.ModelForm):

    class Meta:
        model = Daycare
        fields = [
            'serial_number',
            'name',
            'established_date',
            'max_capacity',
            'avg_children',
            'helpers',
            'standards',
            'status',
            'min_age',
            'max_age',
            'email',
            'cell_phone',
            'land_line',
            'website',
            'description',
            'owner',
            # 'location',
            'services',
            'categories'
        ]

    def save(self, commit=True):
        daycare = super(DaycareForm, self).save(commit=False)
        # activity.created_by = self.request.user

        # print(self.cleaned_data)
        daycare.slug = slugify(self.cleaned_data.get('name'))

        if commit:
            daycare.save()

        return daycare


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        exclude = ()


class OrganisationForm(forms.ModelForm):
    sub_domain = forms.CharField(max_length=100,required=True)

    class Meta:
        model = Organisation
        exclude = ('id',)

    def save(self, commit=False):
        organisation = super(OrganisationForm, self).save(commit=commit)

        organisation.id = self.cleaned_data['sub_domain']
        if commit:
            organisation.save()

        return organisation


class AdminForm(forms.Form):
    email = forms.EmailField()

    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        """
        Send a django.core.mail.EmailMultiAlternatives to `to_email`.
        """
        subject = loader.render_to_string(subject_template_name, context)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())
        body = loader.render_to_string(email_template_name, context)

        email_message = EmailMultiAlternatives(subject, body, from_email, [to_email])
        if html_email_template_name is not None:
            html_email = loader.render_to_string(html_email_template_name, context)
            email_message.attach_alternative(html_email, 'text/html')

        email_message.send()

    def save(self):
        email = self.cleaned_data.get('email')
        account = Account.objects.create_user(
            email=email,
            password='####',
            access_level=2,
            is_verified = True
        )

        use_https = True
        """
        Generate a one-use only link for resetting password and send it to the
        user.
        """
        context = {
            'email': email,
            'domain': 'domain',
            'site_name': 'site_name',
            'uid': urlsafe_base64_encode(force_bytes(account.pk)).decode(),
            'user': account,
            'token': default_token_generator.make_token(account),
            'protocol': 'https' if use_https else 'http',
        }

        self.send_mail(
            'authentication/registration/password_reset_subject.txt',
            'authentication/registration/password_reset_email.html',
            context,
            'from_email',
            email,
            None,
        )

        return account
