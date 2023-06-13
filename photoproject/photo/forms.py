from django.forms import ModelForm
from .models import PhotoPost
from .models import Comment
from django import forms


class PhotoPostForm(ModelForm):
    """
    モデルフォームのサブクラス
    """

    class Meta:
        """
        Modelformのインナークラス
        Attributes:
            model : モデルのクラス
            fields : フォームで使用するモデルのフィールドを指定
        """
        model = PhotoPost
        fields = ['category', 'title', 'comment', 'image1', 'image2', 'video']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('photo_post', 'created_at')
