from django import forms

from tapeforms.contrib.bootstrap import Bootstrap4TapeformMixin, BootstrapTapeformMixin

from . import FormFieldsSnapshotTestMixin


class DummyForm(Bootstrap4TapeformMixin, forms.Form):
    text = forms.CharField()
    checkbox = forms.BooleanField()
    clearable_file = forms.FileField(required=False)


def test_default_version():
    assert BootstrapTapeformMixin == Bootstrap4TapeformMixin


class TestBootstrap4TapeformMixin(FormFieldsSnapshotTestMixin):
    form_class = DummyForm
    snapshot_dir = 'bootstrap4'

    def test_apply_widget_invalid_options(self):
        form = DummyForm({})
        assert 'text' in form.errors
        widget = form.fields['text'].widget
        assert sorted(widget.attrs['class'].split(' ')) == [
            'form-control', 'is-invalid'
        ]
