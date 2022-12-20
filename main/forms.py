from .models import Info, Results
from django.forms import *

class InfoForm(ModelForm):
    class Meta:
        model = Info
        fields = [
            "gender",
            "date_born",
            "loan_balance",
            "profession",
            "hobby",
            "cigarets",
            "alcogol",
        ]
        widgets = {
            "gender": RadioSelect(attrs={
                'class': "form-check form-check-inline",
            }),
            "date_born": DateInput(attrs={
                'type': 'date',
            }),
            "loan_balance": NumberInput(attrs={
                'type': 'text',
            }),
            "cigarets": NumberInput(attrs={

            }),
            "alcogol": NumberInput(attrs={

            }),
        }


class ResultsForm(ModelForm):
    class Meta:
        model = Results
        fields = [
            "sum",
        ]
        widgets = {
            "sum": IntegerField(),
        }