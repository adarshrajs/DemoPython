
from django.shortcuts import render

from travelapp.models import Place, Team


def demo(request):
    obj =Place.objects.all()
    obj1=Team.objects.all()
    return render(request ,"index.html" ,{'result' :obj,'result1':obj1})

# def operations(request):
# x=int(request.GET['num1'])
# y=int(request.GET['num2'])
# add=x+y
# sub=x-y
# mul=x*y
# div=x/y
# return render(request,"result.html",{'add':add,'sub':sub,'mul':mul,'div':div})