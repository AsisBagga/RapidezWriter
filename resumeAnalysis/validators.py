import os
from django.core.exceptions import ValidationError

def validate_resume_ext(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.doc', '.docx', 'docm']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Please upload your resume in a word doc or docx format')

def validate_resume_ext_job(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.doc', '.docx', 'docm', '.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Please upload your resume in a word doc or pdf format')