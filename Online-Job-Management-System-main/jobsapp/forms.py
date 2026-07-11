
from django import forms
from jobsapp.models import Job, Applicant

class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('user', 'created_at',)

    def is_valid(self):
        valid = super(CreateJobForm, self).is_valid()
        return valid

    def save(self, commit=True):
        job = super(CreateJobForm, self).save(commit=False)
        if commit:
            job.save()
        return job

class ApplyJobForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ('job', 'submitted_skills')
        widgets = {
            'submitted_skills': forms.Textarea(attrs={'rows': 3, 'placeholder': 'e.g., Python, Django, SQL'}),
        }
