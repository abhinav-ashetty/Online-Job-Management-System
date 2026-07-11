from django.db import models
from django.utils import timezone

from accounts.models import User

JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)


class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField()
    location = models.CharField(max_length=150)
    type = models.CharField(choices=JOB_TYPE, max_length=10)
    category = models.CharField(max_length=100)
    last_date = models.DateTimeField()
    company_name = models.CharField(max_length=100)
    company_description = models.CharField(max_length=300)
    website = models.CharField(max_length=100, default="")
    created_at = models.DateTimeField(default=timezone.now)
    required_skills = models.TextField(help_text="Comma-separated skills", default="")
    skill_match_threshold = models.IntegerField(default=70)
    filled = models.BooleanField(default=False)
    apply_url = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    
class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applicants')
    submitted_skills = models.TextField(help_text="Comma-separated skills", default="")
    created_at = models.DateTimeField(default=timezone.now)
    meeting_link = models.URLField(blank=True, null=True)
    meeting_link_sent = models.BooleanField(default=False)
    skill_match_percentage = models.IntegerField(default=0)

    
    def __str__(self):
        return self.user.get_full_name()

