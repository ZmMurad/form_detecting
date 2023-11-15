import logging
from forms.models import FormTemplate
from django.http import QueryDict
import re


def find_matching_template(data:QueryDict):
    not_match=['id','_state','name']
    for template in FormTemplate.objects.all():
        template_fields = [v for field,v in template.__dict__.items() if field not in not_match]
        data = [v for v in data.values()]
        if all(field in data for field in template_fields):
            return template
    return None


def get_field_types(data):
    field_types = {}

    for field, value in data.items():
        if re.match(r"\d{2}.\d{2}.\d{4}", value):
            field_types[field] = "date"

        elif re.match(r"\+\d{1,2} \d{3} \d{3} \d{2} \d{2}", value):
            field_types[field] = "phone"

        elif re.match(r"\S+@\S+", value):
            field_types[field] = "email"
        else:
            field_types[field] = "text"

    return field_types
