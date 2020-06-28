from django import forms

from ..mixins import TapeformMixin


class Bootstrap4TapeformMixin(TapeformMixin):
    """
    Tapeform mixin to render Bootstrap 4 compatible forms.
    """

    #: Use a special layout template for Bootstrap compatible forms.
    layout_template = 'tapeforms/layouts/bootstrap.html'
    #: Use a special field template for Bootstrap compatible forms.
    field_template = 'tapeforms/fields/bootstrap.html'
    #: Bootstrap requires ".form-group" on the field container.
    field_container_css_class = 'form-group'
    #: Bootstrap requires ".form-control" on the field widget.
    widget_css_class = 'form-control'
    #: Use a special class to invalid field's widget.
    widget_invalid_css_class = 'is-invalid'

    #: Widgets with multiple inputs require some extra care (don't use ul, etc.)
    widget_template_overrides = {
        forms.SelectDateWidget: 'tapeforms/widgets/bootstrap_multiwidget.html',
        forms.SplitDateTimeWidget: 'tapeforms/widgets/bootstrap_multiwidget.html',
        forms.RadioSelect: 'tapeforms/widgets/bootstrap_multipleinput.html',
        forms.CheckboxSelectMultiple: 'tapeforms/widgets/bootstrap_multipleinput.html'
    }

    def get_field_container_css_class(self, bound_field):
        """
        Returns "form-check" if widget is CheckboxInput. For all other fields,
        the default value from the form property is returned (e.g. "form-group").
        """
        if isinstance(bound_field.field.widget, forms.CheckboxInput):
            return 'form-check'

        return super().get_field_container_css_class(bound_field)

    def get_field_label_css_class(self, bound_field):
        """
        Returns "form-check-label" if widget is CheckboxInput. For all other fields,
        no CSS class is added.
        """
        if isinstance(bound_field.field.widget, forms.CheckboxInput):
            return 'form-check-label'

        return super().get_field_label_css_class(bound_field)

    def get_widget_css_class(self, field_name, field):
        """
        Returns "form-check-input" if widget is CheckboxInput or "form-control-file"
        if widget is FileInput. For all other fields, the default value from the form
        property is returned (e.g. "form-control").
        """
        if isinstance(field.widget, forms.CheckboxInput):
            return 'form-check-input'

        if isinstance(field.widget, forms.FileInput):
            return 'form-control-file'

        return super().get_widget_css_class(field_name, field)


class Bootstrap5TapeformMixin(TapeformMixin):
    """
    Tapeform mixin to render Bootstrap 5 compatible forms.
    """

    #: Use a special layout template for Bootstrap compatible forms.
    layout_template = 'tapeforms/layouts/bootstrap.html'
    #: Use a special field template for Bootstrap compatible forms.
    field_template = 'tapeforms/fields/bootstrap.html'
    #: Add a bottom margin on the field container.
    field_container_css_class = 'mb-3'
    #: Bootstrap requires ".form-label" on the field label.
    field_label_css_class = 'form-label'
    #: Bootstrap requires ".form-control" on the field widget.
    widget_css_class = 'form-control'
    #: Use a special class to invalid field's widget.
    widget_invalid_css_class = 'is-invalid'

    #: Widgets with multiple inputs require some extra care (don't use ul, etc.)
    widget_template_overrides = {
        forms.SelectDateWidget: 'tapeforms/widgets/bootstrap_multiwidget.html',
        forms.SplitDateTimeWidget: 'tapeforms/widgets/bootstrap_multiwidget.html',
        forms.RadioSelect: 'tapeforms/widgets/bootstrap_multipleinput.html',
        forms.CheckboxSelectMultiple: 'tapeforms/widgets/bootstrap_multipleinput.html'
    }

    def get_field_container_css_class(self, bound_field):
        """
        Returns the default value from the form property (e.g. "mb-3"), and add
        "form-check" if widget is CheckboxInput.
        """
        class_name = super().get_field_container_css_class(bound_field)

        if isinstance(bound_field.field.widget, forms.CheckboxInput):
            return '{} form-check'.format(class_name)

        return class_name

    def get_field_label_css_class(self, bound_field):
        """
        Returns "form-check-label" if widget is CheckboxInput. For all other fields,
        no CSS class is added.
        """
        if isinstance(bound_field.field.widget, forms.CheckboxInput):
            return 'form-check-label'

        return super().get_field_label_css_class(bound_field)

    def get_widget_css_class(self, field_name, field):
        """
        Returns "form-check-input" if widget is CheckboxInput or "form-select" if widget is
        Select - or any subclass. For all other fields, the default value from the form
        property is returned (e.g. "form-control").
        """
        if isinstance(field.widget, forms.CheckboxInput):
            return 'form-check-input'

        if isinstance(field.widget, forms.Select):
            return 'form-select'

        return super().get_widget_css_class(field_name, field)


#: Use Bootstrap 4 mixin by default for backward compatibility.
BootstrapTapeformMixin = Bootstrap4TapeformMixin
