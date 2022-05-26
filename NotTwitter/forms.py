from django import forms
from NotTwitter.models import NotATweet

class NotATweetForm(forms.ModelForm):
    body = forms.CharField(required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "O gato comeu sua língua?...",
                "class": "textarea is-info is-medium",
            }
        ),
        label="",
    )
    


    class Meta:
        model = NotATweet
        exclude = ('user', )