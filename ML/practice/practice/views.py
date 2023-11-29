from django.shortcuts import render
def esha(request):
    return render(request,'index.html')

def ashu(request):
    return render(request,'module.html')

def ayshii(request):
    return render(request,'form.html')

def veiwdata(request):
    Email=request.GET['email']
    Password=request.GET['pass']
    data={
        'email':Email,
        'pass' :Password
        }
    return render(request,'viewdata.html', data)
