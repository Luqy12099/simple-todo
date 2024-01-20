from django import forms
from .models import ToDoList


class form_create(forms.ModelForm):
    name = forms.CharField(label='ToDo List')

    class Meta:
        model = ToDoList
        fields = ['name']

'''
class form_edit(forms.ModelForm):
    deskripsi_distributor = forms.CharField(required=False)
    ACTIVE_CHOICES = [
        (0, "Not Active"),
        (1, 'Active'),
    ]

    is_active = forms.ChoiceField(choices=ACTIVE_CHOICES, label='Select Activate', required=False,
                                  initial=10, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = distributor
        fields = ['nama_distributor', 'kota_distributor', 'alamat_distributor', 'deskripsi_distributor', 'is_active']

class searchAndRowcount(forms.Form):
    search_query = forms.CharField(max_length=255, required=False)
    #row_count = forms.IntegerField(min_value=1, required=False)

    ROW_COUNT_CHOICES = [
        (10, '10'),
        (25, '25'),
        (50, '50'),
        (100, '100'),
    ]

    row_count = forms.ChoiceField(choices=ROW_COUNT_CHOICES, label='Select Row Count', required=False,
                                  initial=10, widget=forms.Select(attrs={'class': 'form-control'}))
    

class form_create_mobil(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(form_create_mobil, self).__init__(*args, **kwargs)
        self.fields['distributor'].queryset = distributor.objects.filter(is_delete=0)

    class Meta:
        model = mobil
        fields = ['plat_mobil', 'distributor', 'model_mobil']
        widgets = {
            'distributor': forms.Select(attrs={'class': 'custom-select'})  # Optional styling
        }

class form_edit_mobil(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(form_edit_mobil, self).__init__(*args, **kwargs)
        self.fields['distributor'].queryset = distributor.objects.filter(is_delete=0)

    ACTIVE_CHOICES = [
        (0, "Not Active"),
        (1, 'Active'),
    ]

    is_active = forms.ChoiceField(choices=ACTIVE_CHOICES, label='Select Activate',
                                   widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = mobil
        fields = ['plat_mobil', 'distributor', 'model_mobil', 'is_active']
        widgets = {
            'distributor': forms.Select(attrs={'class': 'custom-select'}),
            'is_active': forms.Select(attrs={'class': 'form-control'})  # Optional styling
        }
'''
