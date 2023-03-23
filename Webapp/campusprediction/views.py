from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd 
import pickle
# Create your views here.
def userlogin(request):
    res = render(request,'login.html') 
    return res


def prediction(request):
    if request.method == 'POST':
        degree_p = request.POST['degree_p']
        degree_t = request.POST['degree_t']
        etest_p = request.POST['etest_p']
        gender   = request.POST['gender']
        hsc_b    = request.POST['hsc_b']
        hsc_p    = request.POST['hsc_p']
        hsc_s    = request.POST['hsc_s']
        mba_p    = request.POST['mba_p']
        specialisation = request.POST['specialisation']
        ssc_b    = request.POST['ssc_b']
        ssc_p    = request.POST['ssc_p']
        workex   = request.POST['workex']
        # print(degree_p,degree_t,e_test_p,gender,hsc_b,hsc_p,hsc_s,mba_p,
        #       specialisation,ssc_b,
        #       ssc_p,
        #       workex)
        k = ['degree_p','degree_t','etest_p','gender','hsc_b','hsc_p','hsc_s','mba_p','specialisation','ssc_b','ssc_p','workex']

        v = [float(degree_p),degree_t,float(etest_p),int(gender),hsc_b,float(hsc_p),hsc_s,float(mba_p),specialisation,ssc_b,float(ssc_p),workex]

        dic = dict(list(zip(k,v)))
        # print(dic)
        df = pd.DataFrame(dic,index=[0])
        print(df)

         # loading ColumnTransformer
        transformer = pickle.load(open('../ColumnTransformer/test1.pickle','rb'))
        
        op = transformer.transform(df)
        print(op)

        return render(request,'prediction.html',{'degree_p':degree_p})


    res = render(request,'prediction.html')
    return res 


    