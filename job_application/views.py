from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
import json
import urllib2
import requests
from django.conf import settings



def job_register(request):
    url = '''http://join.agiliq.com/oauth/access_token/?client_id=%s&redirect_uri=%s&client_secret=121&code=%s''' \
    % (settings.CLIENT_ID,settings.REDIRECT_URI,request.GET['code'])
    
    response = requests.get(url)
    json_data =  response.json()
    
    resume = open('<path to my resume>', 'rb')
    data = {    'first_name': 'Waris Amin',
                'last_name': 'Mir',
                'projects_url': 'https://github.com/warisamin',
                'code_url': 'https://github.com/warisamin/job.agiliq',

                }
    files = { 'resume' : ('resume.pdf', resume)}
    url = 'http://join.agiliq.com/api/resume/upload/?access_token=%s' % json_data['access_token']
    requests.post(url, data=data, files = files)
    
    return HttpResponseRedirect('http://join.agiliq.com/accounts/profile')
    
def authorize(request):
    print settings.CLIENT_ID
    url = '''http://join.agiliq.com/oauth/authorize/?client_id=%s&redirect_uri=%s'''\
     % (settings.CLIENT_ID, settings.REDIRECT_URI)
    return redirect(url)
