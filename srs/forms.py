from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from srs.models import Notefile, Notecard, Directory, Video, Audio, Document, Equation, Image

# Inheritances from UserCreationForm the user object with username, password1, and password2 fields.
# Then, it adds first_name, last_name, and email fields. Also, it grands the staff permission to the user.
class RegistrationForm(UserCreationForm):
    # Indicates that the email field is required to be filled.
    email = forms.EmailField(required = True)
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        )
    def save(self, commit = True):
        # Inheritances username, password1, and password2 fields from UserCreationForm.
        user = super(RegistrationForm, self).save(commit = False)
        # Adds first_name, last_name, and email fields to the user object.
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        # Grands staff permission.
        user.is_staff = True
        if commit:
            user.save()
        return user

class ImportForm(forms.Form):
    path = forms.CharField(label='Path', max_length=100)

class NotefileForm(forms.ModelForm):
    class Meta:
        model = Notefile
        fields = ('name',)

class NotecardForm(forms.ModelForm):

    keywords = forms.CharField(required=False, widget=forms.Textarea, strip= False)
    label = forms.CharField(required=False, widget=forms.Textarea, strip = False)
    body = forms.CharField(required=False, widget=forms.Textarea, strip = False)

    class Meta:
        model = Notecard
        fields = ('name', 'keywords', 'label', 'body',)

class DeleteNotecardForm(forms.ModelForm):

    class Meta:
        model = Notecard
        fields = ()

class DuplicateNotecardForm(forms.ModelForm):

    keywords = forms.CharField(required=False, widget=forms.Textarea, strip= False)
    label = forms.CharField(required=False, widget=forms.Textarea, strip = False)
    body = forms.CharField(required=False, widget=forms.Textarea, strip = False)
    hiddenField = forms.CharField(required=False, strip = False, widget = forms.HiddenInput())
    notefile = forms.ModelChoiceField(queryset=Notefile.objects.all(), required=True)

    class Meta:
        model = Notecard
        fields = ('name', 'notefile', 'keywords', 'label', 'body', 'hiddenField')

class DirectoryForm(forms.ModelForm):
    class Meta:
        model = Directory
        fields = ('name',)

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('url','title',)

    def __init__(self, *args, **kwargs):
        super(VideoForm, self).__init__(*args, **kwargs)
        self.fields['url'].label = 'Source'


class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ('url','title',)

    def __init__(self, *args, **kwargs):
        super(AudioForm, self).__init__(*args, **kwargs)
        self.fields['url'].label = 'Source'


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('source',)

class EquationForm(forms.ModelForm):
    class Meta:
        model = Equation
        fields = ('equation',)

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('source', 'name',)
