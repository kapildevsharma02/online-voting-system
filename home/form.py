from django import forms
from home.models import VotingList

CHOICES = (
    ('Candidate 1', 'Candidate 1'),
    ('Candidate 2', 'Candidate 2'),
    ('Candidate 3', 'Candidate 3'),
)

class VForm(forms.Form):

    vote = forms.ChoiceField(label ="",required=True,widget=forms.RadioSelect, choices=CHOICES)
    class Meta:
        model = VotingList
        fields = ['vote']