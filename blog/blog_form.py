from blog.models import BlogComment
from django import forms

class BlogCommentForm(forms.ModelForm):

    class Meta:
        model = BlogComment
        fields = ['comment']
    # def __init__(self, *args, **kwargs):
    #     super(BlogCommentForm, self).__init__(*args, **kwargs)
    #     self.fields['comment'].label = 'Comment'
    # Changing form objects like field label but not yet working



