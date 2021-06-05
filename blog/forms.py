from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "user_name": "Your Name",
            "user_email": "Your Email",
            "text": "Your Comment"
        }
        errors = {
             "user_name": "This field is required!",
            "user_email": "Email id is not valid!",
            "text": "Please leave a comment!"
        }