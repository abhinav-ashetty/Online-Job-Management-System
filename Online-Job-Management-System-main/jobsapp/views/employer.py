from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView

from accounts.views import send_email
from jobs import settings
from jobsapp.decorators import user_is_employer
from jobsapp.forms import CreateJobForm
from jobsapp.models import Job, Applicant

from django.core.mail import send_mail

from django.shortcuts import get_object_or_404, render
from jobsapp.utils import calculate_skill_match


class DashboardView(ListView):
    model = Job
    template_name = 'jobs/employer/dashboard.html'
    context_object_name = 'jobs'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_employer)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class ApplicantPerJobView(ListView):
    model = Applicant
    template_name = 'jobs/employer/applicants.html'
    context_object_name = 'applicants'
    paginate_by = 10  # Adjust the pagination to a more reasonable number

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_employer)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(job_id=self.kwargs['job_id']).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job'] = Job.objects.get(id=self.kwargs['job_id'])
        return context


# class JobCreateView(CreateView):
#     template_name = 'jobs/create.html'
#     form_class = CreateJobForm
#     success_url = reverse_lazy('jobs:employer-dashboard')

#     @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
#     @method_decorator(user_is_employer)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)

#     def form_valid(self, form):
#         form.instance.user = self.request.user  # Set the user to the current authenticated user
#         return super().form_valid(form)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Post New Job'
#         return context

# class JobCreateView(CreateView):
#     model = Job  # Specify the model to save data into the database
#     template_name = 'jobs/create.html'
#     form_class = CreateJobForm
#     success_url = reverse_lazy('jobs:employer-dashboard')

#     @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
#     @method_decorator(user_is_employer)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)

#     def form_valid(self, form):
#         job = form.save(commit=False)  # Save the form but don't commit to DB yet
#         job.user = self.request.user  # Assign the current logged-in user
#         job.save()  # Now save it to the database
#         return super().form_valid(form)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Post New Job'
#         return context

class JobCreateView(CreateView):
    template_name = 'jobs/create.html'
    form_class = CreateJobForm
    success_url = reverse_lazy('jobs:employer-dashboard')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_employer)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # Save the job details to the database first
        job = form.save(commit=False)
        job.user = self.request.user  # Assign job to the logged-in user
        job.save()

        # After saving the job, send an email notification
        self.send_email_notification(job)

        return super().form_valid(form)

    def send_email_notification(self, job):
        """Send an email when a new job is posted."""
        subject = f"New job posted: {job.title}"
        message = (
            f"A new job has been posted:\n"
            f"Company Name: {job.company_name}\n"
            f"Job Type: {job.get_type_display()}\n"
            f"Description: {job.description}\n"
            f"Location: {job.location}\n"
            f"Last Date to Apply: {job.last_date}\n"
            f"Apply using this URL: {job.apply_url}"
        )
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ["ia4693403@gmail.com", "nari133134@gmail.com", "01abhinavshetty@gmail.com"]
        
        # Send the email
        send_mail(subject, message, from_email, recipient_list)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Post New Job'
        return context



# @login_required(login_url=reverse_lazy('accounts:login'))
# @user_is_employer
# def matched_seekers(request, job_id):
#     job = get_object_or_404(Job, id=job_id, user=request.user)
#     applicants = Applicant.objects.filter(job=job)

#     matched_applicants = []
#     rejected_applicants = []

#     for applicant in applicants:
#         percentage = calculate_skill_match(applicant.submitted_skills, job.required_skills)
#         applicant_data = {
#             'applicant': applicant,
#             'match_percentage': round(percentage, 2)
#         }

#         if percentage >= job.skill_match_threshold:
#             matched_applicants.append(applicant_data)
#         else:
#             rejected_applicants.append(applicant_data)

#     return render(request, 'jobs/employer/matched_seekers.html', {
#         'job': job,
#         'matched_applicants': matched_applicants,
#         'rejected_applicants': rejected_applicants
#     })


# class ApplicantsListView(ListView):
#     model = Applicant
#     template_name = 'jobs/employer/all-applicants.html'
#     context_object_name = 'applicants'

#     @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
#     @method_decorator(user_is_employer)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)

#     def get_queryset(self):
#         return self.model.objects.filter(job__user=self.request.user)


@login_required(login_url=reverse_lazy('accounts:login'))
def filled(request, job_id=None):
    try:
        job = Job.objects.get(user=request.user, id=job_id)
        job.filled = True
        job.save()
    except Job.DoesNotExist:
        # Handle the case where the job does not exist
        return HttpResponseRedirect(reverse_lazy('jobs:employer-dashboard'))  # You can redirect or show an error message here

    return HttpResponseRedirect(reverse_lazy('jobs:employer-dashboard'))



# class ApplicantsListView(ListView):
#     model = Applicant
#     template_name = 'jobs/employer/all-applicants.html'
#     context_object_name = 'applicants'

#     @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
#     @method_decorator(user_is_employer)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)

#     def get_queryset(self):
#         return Applicant.objects.filter(job__user=self.request.user)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         job_id = self.kwargs.get('job_id')  # Expecting job_id in URL
#         job = get_object_or_404(Job, id=job_id, user=self.request.user)
#         applicants = Applicant.objects.filter(job=job)

#         required_skills = [s.strip().lower() for s in job.required_skills.split(',')]
#         threshold = job.skill_match_threshold

#         matched_applicants = []
#         rejected_applicants = []

#         for applicant in applicants:
#             submitted_skills = [s.strip().lower() for s in applicant.submitted_skills.split(',')]
#             match_count = sum(1 for skill in required_skills if skill in submitted_skills)
#             match_percentage = (match_count / len(required_skills)) * 100 if required_skills else 0

#             if match_percentage >= threshold:
#                 matched_applicants.append({'applicant': applicant, 'match_percentage': round(match_percentage, 2)})
#             else:
#                 rejected_applicants.append({'applicant': applicant, 'match_percentage': round(match_percentage, 2)})

#         context['job'] = job
#         context['matched_applicants'] = matched_applicants
#         context['rejected_applicants'] = rejected_applicants
#         return context

class ApplicantsListView(ListView):
    model = Applicant
    template_name = 'jobs/employer/all-applicants.html'
    context_object_name = 'applicants'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_employer)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        # Get all applicants for jobs posted by current employer
        return Applicant.objects.filter(job__user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        applicants = context['applicants']
        meeting_link =""
        matched_applicants = []
        rejected_applicants = []

        for applicant in applicants:
            job = applicant.job
            required_skills = [s.strip().lower() for s in job.required_skills.split(',')]
            threshold = job.skill_match_threshold
            submitted_skills = [s.strip().lower() for s in applicant.submitted_skills.split(',')]

            match_count = sum(1 for skill in required_skills if skill in submitted_skills)
            match_percentage = (match_count / len(required_skills)) * 100 if required_skills else 0

            applicant_data = {
                'applicant': applicant,
                'job': job,
                'match_percentage': round(match_percentage, 2)
            }

            if match_percentage >= threshold:
                matched_applicants.append(applicant_data)
                
                if not applicant.meeting_link_sent:
                    meeting_link = "https://meet.google.com/xyz-abc-def"  # Replace with real logic
                    applicant.meeting_link = meeting_link
                    applicant.meeting_link_sent = True
                    applicant.save()

                send_mail(
                    subject="Interview Meeting Link",
                    message=f"Hi {applicant.user.get_full_name()},\n\nCongratulations! You have been shortlisted.\nJoin the interview using this meeting link: {meeting_link}. Date to attend Interview will be updated futher to this email.",
                    from_email="abhinavarunkumarshetty@gmail.com",
                    # recipient_list=[applicant.user.email],
                    recipient_list=['01abhinavshetty@gmail.com'],
                    fail_silently=False,
                )
                
            else:
                rejected_applicants.append(applicant_data)

        context['matched_applicants'] = matched_applicants
        context['rejected_applicants'] = rejected_applicants
        return context

