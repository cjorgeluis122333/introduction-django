from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Simple homepage view for a growing project.

    This is a minimal starting point for a Django app using class-based views
    and templates. It can be extended with context data, permissions, i18n, etc.
    """

    template_name = "mi_app/home.html"
