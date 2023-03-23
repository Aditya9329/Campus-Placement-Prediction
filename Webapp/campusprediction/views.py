from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def userlogin(request):
    res = render(request,'login.html') 
    return res


def prediction(request):
    if request.method == 'POST':
        degree_p = request.POST['degree_p']
        degree_t = request.POST['degree_t']
        e_test_p = request.POST['e_test_p']
        gender   = request.POST['gender']
        hsc_b    = request.POST['hsc_b']
        hsc_p    = request.POST['hsc_p']
        hsc_s    = request.POST['hsc_s']
        mba_p    = request.POST['mba_p']
        specialisation = request.POST['specialisation']
        ssc_b    = request.POST['ssc_b']
        ssc_p    = request.POST['ssc_p']
        workex   = request.POST['workex']
        print(degree_p,degree_t,e_test_p,gender,hsc_b,hsc_p,hsc_s,mba_p,
              specialisation,ssc_b,
              ssc_p,
              workex)
        return render(request,'prediction.html',{'degree_p':degree_p})


    res = render(request,'prediction.html')
    return res 


    