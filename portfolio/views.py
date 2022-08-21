from django.shortcuts import render, get_object_or_404
from .models import Project_info

def portfolio_home(request):
    projects = Project_info.objects.order_by('-project_date')
    return render(request, 'portfolio-home.html', {'projects': projects})


def portfolio_details(request, id, title):
    projects = get_object_or_404(Project_info, id=id, title=title)
    return render(request, 'portfolio-details.html', {'projects': projects})
