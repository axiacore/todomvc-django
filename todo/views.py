from django.views.generic import TemplateView


# All todos view
class Home( TemplateView ):

	# Set the view template
	template_name = 'index.html'