from django.views.generic import TemplateView

class PortfolioView(TemplateView):
	template_name = "portfolio.html"

portfolio = PortfolioView.as_view()