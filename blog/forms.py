from django import forms
from .models import CommentModel

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        exclude = ["post"]
        labels = {
            "user_name": "Your name",
            "user_email": "Your email",
            "comment_text": "Your comments"
        }
