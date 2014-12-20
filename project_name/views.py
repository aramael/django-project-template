"""
Django views for {{ project_name }} project.

"""

from django.shortcuts import render


def home(request):
    """    Display the Landing Page    """

    context = {}

    return render(request, 'home.html', context)