from django.contrib import admin
from jobsapp.models import Job,Applicant

class AdminJob(admin.ModelAdmin):
    list_display = ('id','user','title','description','location','type','category','last_date','company_name','company_description','website','created_at','filled','apply_url')
    
admin.site.register(Job,AdminJob)

class AdminApplicant(admin.ModelAdmin):
    list_display = ('user','job','created_at','submitted_skills','meeting_link','meeting_link_sent')
    
    
admin.site.register(Applicant,AdminApplicant)
# Register your models here.
