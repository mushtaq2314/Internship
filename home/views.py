import ast
from django.shortcuts import render
from home.models import Donations
# Create your views here.
def index(request):
    data = list(Donations.objects.values_list())
    count=0
    for i in data:
        if type(ast.literal_eval(i[6])["to"])==list:
            count+=len(ast.literal_eval(i[6])["to"])
    print("No. of donations = ",count) 
    context={"donations":count}   
    return render(request,'index.html',context)
def contact(request):
    return render(request,'contact.html')
def login(request):
    if request.method == "POST":
        global lmail
        lmail = request.POST.get('lmail')
        lpass = request.POST.get('lpass')
        
        mails = list(Donations.objects.values_list('email',flat=True))
        passwords = list(Donations.objects.values_list('password',flat=True))

        if lmail in mails:
            k = mails.index(lmail)
            if passwords[k]==lpass:
                ####################################
                
                data = list(list(Donations.objects.filter(email=lmail).values_list())[0])
                print(data[6])
                context={'name':data[1],'mail':data[2],'phone':data[4],'designation':data[5],'donations':ast.literal_eval(data[6])}
                
                ####################################
                
                return render(request,'dashboard.html',context)
            else:
                context = {'message':'Invalid Credentials.Try Again'}
                return render(request,'login.html',context)
        else:
                context = {'message':'Invalid Credentials.Try Again'}
                return render(request,'login.html',context)
    return render(request,'login.html')
def signup(request):
    allmails = list(Donations.objects.values_list('email',flat=True))
    if request.method == "POST":
        name = request.POST.get('sname')
        global email
        email = request.POST.get('smail')
        password = request.POST.get('spass')
        if email in allmails:
            return render(request,'signup.html',{'message':'Email already exists!'})
        else:    
            print(name,email,password)
            signup = Donations(name= name,email = email,password=password)  
            signup.save()
            context = {'name':name}
            return render(request,'login.html',context)
    return render(request,'signup.html')
def dashboard(request):
        
        global lmail
        if request.method=='POST':
            desig = request.POST.get('pmail')
            phone = request.POST.get('pphone')
            Donations.objects.filter(email=lmail).update(designation=desig,phone=phone)
        data = list(list(Donations.objects.filter(email=lmail).values_list())[0])
        print(data)
        context={'name':data[1],'mail':data[2],'phone':data[4],'designation':data[5]}      
        return render(request,'dashboard.html',context)
def done(request):
    return render(request,'done.html')   
def previous(request):
    global lmail
    data = list(list(Donations.objects.filter(email=lmail).values_list())[0])
    context = ast.literal_eval(data[-1])
    data = zip(context['to'],context['phone'],context['email'],context['date'])
    
    return render(request,'previous.html',{'data':data})      
def adminlogin(request):
    if request.method == "POST":
        lmail = request.POST.get('amail')
        lpass = request.POST.get('apass')
        
        mails = list(Donations.objects.values_list('email',flat=True))
        passwords = list(Donations.objects.values_list('password',flat=True))

        if lmail in mails:
            k = mails.index(lmail)
            if passwords[k]==lpass:
                ####################################
                
                data = list(list(Donations.objects.filter(email=lmail).values_list())[0])
                context={'name':data[1],'mail':data[2],'phone':data[4],'designation':data[5]}
                
                ####################################
                
                return render(request,'admin.html',context)
            else:
                context = {'message':'Invalid Credentials.Try Again'}
                return render(request,'adminlogin.html',context)
        else:
                context = {'message':'Invalid Credentials.Try Again'}
                return render(request,'adminlogin.html',context)
    return render(request,'adminlogin.html')                 
def admin(request):
    if request.method == "POST":
        mail = request.POST.get('dmail')
        aname = request.POST.get('aname')
        aphone = request.POST.get('aphone')
        amail = request.POST.get('amail')
        date = request.POST.get('date')
        data = list(list(Donations.objects.filter(email=mail).values_list())[0])
        update = ast.literal_eval(data[-1])
        update['to'].append(aname)
        update['status']='Donated'
        update['email'].append(amail)
        update['phone'].append(aphone)
        update['date'].append(date)
        print("updated --> ",update,type(update['to']))
        Donations.objects.filter(email=mail).update(donations=str(update))


    return render(request,'admin.html')     