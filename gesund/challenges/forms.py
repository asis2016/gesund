from django import forms
from .models import Challenge


class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ('start_date', 'challenge',)

    def __init__(self, *args, **kwargs):
        super(ChallengeForm, self).__init__(*args, **kwargs)
        self.fields['start_date'].required = True


class ChallengeUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ChallengeUpdateForm, self).__init__(*args, **kwargs)
        self.fields['start_date'].required = True

    class Meta:
        model = Challenge
        fields = ('start_date', 'challenge', 'status')
