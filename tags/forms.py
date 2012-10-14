import selectable.forms as selectable
from tags.lookups import TagLookup
from django import forms


class TagForm(forms.Form):
  autocomplete = forms.CharField(
    label='Tag',
    widget=selectable.AutoCompleteWidget(TagLookup),
    required=True,
  )