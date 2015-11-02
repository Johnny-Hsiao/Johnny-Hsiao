from django.views.generic import TemplateView

class AboutTemplate(TemplateView):
	template_name = "about.html"

about = AboutTemplate.as_view()