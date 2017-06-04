from django.forms import ModelForm, Form
from django.contrib.admin.widgets import AdminFileWidget
from .models import Asset, Check, AssetSignature
from django import forms
from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget

years = [x for x in range(2000, 2025)]


class AssetForm(ModelForm):
    class Meta:
        model = Asset
        exclude = ['', ]
        widgets = {'capitalized': forms.SelectDateWidget(years=years)}
        labels = {
            'descr': 'Description',
            'add_descr': 'Additional Description',
        }


class Checkin_Form(ModelForm):
    class Meta:
        model = Check
        exclude = ['',]
        labels = {
            'document': 'Asset Return Form (signed)',
        }
        widgets = {
            'asset': forms.HiddenInput(),
            'staff': forms.HiddenInput(),
            'check_type': forms.HiddenInput(),
            'document': AdminFileWidget,
        }


class Checkout_Form(ModelForm):
    class Meta:
        model = Check
        exclude = ['',]
        labels = {
            'document': 'Asset Assignment Form (signed)',
        }
        widgets = {
            'asset': forms.HiddenInput(),
            'check_type': forms.HiddenInput(),
            'document': AdminFileWidget,
        }

class Signout_Form(ModelForm):
    class Meta:
        model = Check
        exclude = ['signature', 'approval_signature', 'document', 'check_type']
        labels = {'date': 'Date: (YYYY-MM-DD)',}

class Signout_Signature_Form(ModelForm):
    class Meta:
        model = AssetSignature
        widgets = {'signature': JSignatureWidget, }
        fields = ['signature', ]

class Signout_Signature_Approved_Form(ModelForm):
    class Meta:
        model = AssetSignature
        widgets = {'signature': JSignatureWidget, }
        fields = ['signature', ]


