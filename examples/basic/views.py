from django.views.generic import FormView

from .forms import (
    SimpleBootstrapForm,
    SimpleBulmaForm,
    SimpleForm,
    SimpleFoundationForm,
    SimpleMultiWidgetForm,
    SimpleWithOverridesForm,
)


class SimpleView(FormView):
    form_class = SimpleForm
    template_name = 'basic/simple_view.html'


class SimpleWithOverridesView(FormView):
    form_class = SimpleWithOverridesForm
    template_name = 'basic/simple_view.html'


class SimpleBootstrapView(FormView):
    form_class = SimpleBootstrapForm
    template_name = 'basic/bootstrap_view.html'


class SimpleBulmaView(FormView):
    form_class = SimpleBulmaForm
    template_name = 'basic/bulma_view.html'


class SimpleFoundationView(FormView):
    form_class = SimpleFoundationForm
    template_name = 'basic/foundation_view.html'


class SimpleMultiWidgetView(FormView):
    form_class = SimpleMultiWidgetForm
    template_name = 'basic/simple_view.html'
