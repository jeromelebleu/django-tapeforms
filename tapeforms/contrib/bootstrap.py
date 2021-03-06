from django import forms

from ..mixins import TapeformMixin


class BootstrapTapeformMixin(TapeformMixin):
    """
    Tapeform Mixin to render Bootstrap4 compatible forms.
    (using the template tags provided by `tapeforms`).
    """

    #: Use a special layout template for Bootstrap compatible forms.
    layout_template = 'tapeforms/layouts/bootstrap.html'
    #: Use a special field template for Bootstrap compatible forms.
    field_template = 'tapeforms/fields/bootstrap.html'
    #: Bootstrap requires that the field has a css class "form-group" applied.
    field_container_css_class = 'form-group'
    #: All widgets need a css class "form-control" (expect checkboxes).
    widget_css_class = 'form-control'

    #: Widgets with multiple inputs require some extra care (don't use ul, etc.)
    widget_template_overrides = {
        forms.SelectDateWidget: 'tapeforms/widgets/bootstrap_multiwidget.html',
        forms.SplitDateTimeWidget: 'tapeforms/widgets/bootstrap_multiwidget.html',
        forms.RadioSelect: 'tapeforms/widgets/bootstrap_multipleinput.html',
        forms.CheckboxSelectMultiple: 'tapeforms/widgets/bootstrap_multipleinput.html'
    }

    def get_field_container_css_class(self, bound_field):
        """
        Returns 'form-check' if widget is CheckboxInput. For all other fields,
        return the default value from the form property ("form-group").
        """
        # If we render CheckboxInputs, Bootstrap requires a different
        # container class for checkboxes.
        if isinstance(bound_field.field.widget, forms.CheckboxInput):
            return 'form-check'

        return super().get_field_container_css_class(bound_field)

    def get_field_label_css_class(self, bound_field):
        """
        Returns 'form-check-label' if widget is CheckboxInput. For all other fields,
        no css class is added.
        """
        # If we render CheckboxInputs, Bootstrap requires a different
        # field label css class for checkboxes.
        if isinstance(bound_field.field.widget, forms.CheckboxInput):
            return 'form-check-label'

        return super().get_field_label_css_class(bound_field)

    def get_widget_css_class(self, field_name, field):
        """
        Returns 'form-check-input' if widget is CheckboxInput. For all other fields
        return the default value from the form property ("form-control").
        """
        # If we render CheckboxInputs, Bootstrap requires a different
        # widget css class for checkboxes.
        if isinstance(field.widget, forms.CheckboxInput):
            return 'form-check-input'

        return super().get_widget_css_class(field_name, field)

    def add_error(self, field_name, error):
        """
        The method is overwritten to append 'is-invalid' to the css class of the
        field's widget.
        """
        super().add_error(field_name, error)

        if field_name in self.fields:
            field = self.fields[field_name]
            class_names = field.widget.attrs.get('class', '').split(' ')

            if 'is-invalid' not in class_names:
                class_names.append('is-invalid')
                field.widget.attrs['class'] = ' '.join(class_names)
