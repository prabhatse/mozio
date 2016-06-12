from django import forms
from api.provider.models import Providers as Provider

class AddProviderForm(forms.Form):
    """
        Form to save/edit a Service area.
    """


    name = forms.CharField(label='Provider Name', required=False)
    email = forms.EmailField(label='Provider Email', required=False)
    phone_no = forms.CharField(label='Provider Phone', required=False)
    language = forms.CharField(label='Provider Language', required=False)
    currency= forms.CharField(label='Provider Currency', required=False)

    def save(self, force_insert=False, force_update=False, commit=True):
        try:
            obj = Provider.objects.get(name=self.data['name'], 
            	email=self.data['email'],
            	phone_no=self.data['phone_no'],
            	language=self.data['language'],
            	currency=self.data['currency'])
        except:
        	obj = Provider(name=self.data['name'], 
            	email=self.data['email'],
            	phone_no=self.data['phone_no'],
            	language=self.data['language'],
            	currency=self.data['currency'])
        obj.save()

