from django.shortcuts import render
from django.views import View
from django.http import  HttpResponse
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError

# Create your views here.

class homeView(View):
    template_name = 'pages/home.html'

    def get(self, request):
        
        
        return render(request, self.template_name, {})

    def post(self, request):

        fname = request.POST.get('fname', '')
        email = request.POST.get('Email', '')
        subject = request.POST.get('sub', '')
        message = request.POST['mess']

        my_mail = settings.EMAIL_HOST_USER

        if subject and message and email:
            try:
                send_mail(
                    subject,
                    message,
                    email,
                    [my_mail],
                    fail_silently=True
                )
            except BadHeaderError or ValueError:
                return HttpResponse("Message error.")



        return render(request, self.template_name, {'firstname':fname})
