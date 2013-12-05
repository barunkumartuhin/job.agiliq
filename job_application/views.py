from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
import json
import urllib2
import requests

client_id = '121'
redirect_uri = 'http://127.0.0.1:8000/job/register'

def job_register(request):
    url = '''http://10.42.0.4:8001/oauth/access_token?client_id=%s&redirect_uri=%s&client_secret=121&code=%s''' % (client_id, redirect_uri,request.GET['code'])
    response = requests.get(url)
    json_data =  response.json()
    resume = open('/home/waris/Desktop/examform.pdf', 'rb')
    data = {    'first_name': 'Waris Amin',
                'last_name': 'Mir',
                'projects_url': 'https://github.com/warisamin',
                'code_url': 'https://github.com/warisamin/job.agiliq',

                }
    files = { 'resume' : ('resume.pdf', resume)}
    url = 'http://10.42.0.4:8001/api/resume/upload/?access_token=%s' % json_data['access_token']
    requests.post(url, data=data, files = files)
    return HttpResponseRedirect('http://10.42.0.4:8001/accounts/profile')
    
def authorize(request):
    url = 'http://10.42.0.4:8001/oauth/authorize?client_id=%s&redirect_uri=%s' % (client_id, redirect_uri)
    return redirect(url)
