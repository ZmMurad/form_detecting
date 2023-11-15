from django.shortcuts import render
from forms.models import FormTemplate
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from forms.services.form_services import find_matching_template, get_field_types


@csrf_exempt
def get_form(request):
    if request.method == 'POST':
        data = request.POST
        template = find_matching_template(data)
        if template:
            return JsonResponse({'template_name': template.name})
        else:
            return JsonResponse(get_field_types(data))



