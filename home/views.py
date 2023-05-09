from django.shortcuts import render
from django.views import View

# Render index page
class renderIndex(View):
    template_name = "home/index.html"

    def get(self, request):
        return render(request, self.template_name)