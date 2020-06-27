from django import forms
from backend.api.models import Post


class AddPostForm(forms.Form):
    post_title = forms.CharField(max_length=50)
    body = forms.CharField(max_length=280)
    boast_or_roast = forms.BooleanField(
        help_text="Boast if checked", required=False)
