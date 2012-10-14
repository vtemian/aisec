from django import forms
from django.utils.translation import ugettext_lazy as _

from discussion.models import Comment, Post, Discussion
from notification.models import NoticeSetting
from tags.models import Tag, TagsPost

from .utils import file_extension, DISCUSSION_UPLOAD_EXTENSIONS


def _clean_attachment(self):
    data = self.cleaned_data['attachment']
    if data is None:
        return data
    extension = file_extension(data.name)
    try:
        extension_ok = extension in DISCUSSION_UPLOAD_EXTENSIONS
    except TypeError:
        pass  # DISCUSSION_UPLOAD_EXTENSIONS has been set to None.
    else:
        if not extension_ok:
            msg = _('This is not an acceptable file type!')
            raise forms.ValidationError(msg)
    return data


class CommentForm(forms.ModelForm):

  class Meta:
      exclude = ('user', 'post')
      model = Comment
      widgets = {
          'body': forms.Textarea(attrs={'placeholder': _('Reply to this conversation')}),
      }
  clean_attachment = _clean_attachment


class PostForm(forms.ModelForm):
  tags = forms.CharField(label='', widget=forms.HiddenInput(attrs={'id': _('hidden_tags')}), required=False)
  class Meta:
      exclude = ('user', 'discussion')
      model = Post
      widgets = {
          'body': forms.Textarea(attrs={'placeholder': _('Start a conversation')}),
      }

  clean_attachment = _clean_attachment

  def save(self, force_insert=False, force_update=False, commit=True):
    post = super(PostForm, self).save(commit=False)
    post.save()

    tags = self.data['tags'].split(';')

    for tag in tags:
      try:
        new_tag = Tag.objects.get(name=tag)
        TagsPost.objects.create(post=post, tag=new_tag)
      except Exception:
        pass
    return  post


class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={'class':'search-query', 'placeholder': 'Search for messages'}))
    discussion = forms.ModelChoiceField(
            required=False,
            queryset=Discussion.objects,
            empty_label=_('All discussions'))


class SubscribeForm(forms.Form):
    send = forms.ModelMultipleChoiceField(
            NoticeSetting.objects,
            required=False,
            label=_('Notify me with updates from this discussion by'),
            widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        qs = kwargs.pop('qs')
        super(SubscribeForm, self).__init__(*args, **kwargs)
        self.fields['send'].queryset = qs
