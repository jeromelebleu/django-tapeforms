from django import forms

from tapeforms.contrib.bootstrap import (
    Bootstrap4TapeformMixin, Bootstrap5TapeformMixin, BootstrapTapeformMixin)

from . import FormFieldsSnapshotTestMixin


class Dummy4Form(Bootstrap4TapeformMixin, forms.Form):
    text = forms.CharField()
    checkbox = forms.BooleanField()
    clearable_file = forms.FileField(required=False)


class Dummy5Form(Bootstrap5TapeformMixin, forms.Form):
    CHOICES = (('foo', 'Foo'), ('bar', 'Bar'))

    text = forms.CharField()
    checkbox = forms.BooleanField()
    select = forms.ChoiceField(choices=CHOICES)
    select_multiple = forms.MultipleChoiceField(choices=CHOICES)


def test_default_version():
    assert BootstrapTapeformMixin == Bootstrap4TapeformMixin


class TestBootstrap4TapeformMixin(FormFieldsSnapshotTestMixin):
    form_class = Dummy4Form
    snapshot_dir = 'bootstrap4'

    def test_apply_widget_invalid_options(self):
        form = self.form_class({})
        assert 'text' in form.errors
        widget = form.fields['text'].widget
        assert sorted(widget.attrs['class'].split(' ')) == [
            'form-control', 'is-invalid'
        ]


class TestBootstrap5TapeformMixin(FormFieldsSnapshotTestMixin):
    form_class = Dummy5Form
    snapshot_dir = 'bootstrap5'

    def test_apply_widget_invalid_options(self):
        form = self.form_class({})
        assert 'text' in form.errors
        widget = form.fields['text'].widget
        assert sorted(widget.attrs['class'].split(' ')) == [
            'form-control', 'is-invalid'
        ]
