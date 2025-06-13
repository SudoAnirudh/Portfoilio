from django.shortcuts import render

def index(request):
    # Assuming index.html is in 'main_app/templates/main_app/index.html'
    # Django's template loader will find it if 'main_app/templates' is in TEMPLATE DIRS
    # or if using app_directories=True (default) and templates are in main_app/templates/
    return render(request, 'main_app/index.html')
