from django.shortcuts import render

def rubric_creator(request):
    return render(request, 'ncea/rubric_creator.html')
