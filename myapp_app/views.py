from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime as dt
import datetime
from pytz import timezone
import pytz
def index(req):

    blr = datetime.datetime.now().time()
    nyc = datetime.datetime.now(pytz.timezone('US/Eastern'))
    singapore = datetime.datetime.now(pytz.timezone('Asia/Singapore'))
    sydney = datetime.datetime.now(pytz.timezone('Australia/Sydney'))
    x={
        "t_blr": "%s"%blr,
        "t_nyc": "%s"%nyc,
        "t_sing": "%s"%singapore,
        "t_sy": "%s"%sydney,
   
      } 
    tmpl=loader.get_template('index.html')
    return HttpResponse(tmpl.render(x))
  