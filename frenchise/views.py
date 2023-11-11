from django.shortcuts import render,redirect, HttpResponse
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.views import View
from django.contrib.auth.models import User
from .models import frenchise_register_model,frenchise_employee_register_model,ProfileFrenchise
from .forms import FrenchiseRegistrationForm, frenchise_application_form, Employee_application_form
from django.contrib.auth.decorators import login_required
from fastapi.responses import RedirectResponse, HTMLResponse
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from companystaff.models import *
# from .filters import frenchise_filter
from datetime import datetime
import requests
import hashlib

# Create your views here.
# import matplotlib.pyplot as plt
from io import BytesIO
import base64
def index(request):
    return render(request, 'frenchise/index.html' )







#admin Search
def frenchise_search_view(request):
    if request.method == 'POST':
        search = request.POST.get('Search')
        print(search)
        filter_matches = ProfileFrenchise.objects.filter(email=search,number=search)

        if filter_matches:
            for match in filter_matches:
                if match.email == search:
                    # Do something when there is a match for email.
                    print("email")
                    return render(request, 'frenchise/admin_dashboard.html')
                elif match.number == search:
                    return render(request, 'frenchise/admin_dashboard.html')
                    # Do something when there is a match for number.
                    print("number")
                    pass
                # elif match.PAN == search:
                #     print("PAN")
                    # Do something when there is a match for PAN.
                    pass
            return redirect('dashboard')
        else:
            filter_matches = ProfileFrenchise.objects.filter()
            # Do something when there is no match.
            print("No matches found")
            return render(request, 'frenchise/admin_dashboard.html', {'fsearch': filter_matches})  # Render a template with a message

        # Add a default return statement in case none of the conditions are met
        return HttpResponse("Internal server error", status=500)

# Frenchise Registration
def frenchise_registration_view(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        raw_password = request.POST.get('password')
        raw_education = request.POST.get('education')
        raw_occupation = request.POST.get('occupation')
        raw_number = request.POST.get('number')
        raw_state = request.POST.get('state')
        raw_city = request.POST.get('city')
        raw_dob      =  request.POST.get('dateInput')
        raw_email = request.POST.get('email')
        # passs = number+"Nakshtravani@"
        passs = str(raw_password)
        print(passs)
        user = User.objects.create(
            username=raw_number
            # role='User',
            # password=passs,
        )
        v = user.set_password(passs)
        print(v)
        # user.save()
        print([name,raw_password,raw_city,raw_dob,raw_education,raw_state,raw_number,raw_occupation])
        # user = r_form.save()
        user.is_active = False
        user.save()
        users = User.objects.get(username=raw_number)
            # user.is_active = False
        users.passwo = passs
        ProfileFrenchise.objects.create(user=users,DOB=raw_dob,state=raw_state,email=raw_email,city=raw_city,number=raw_number,Occupation=raw_occupation,Education=raw_education,Role="Frenchise")
        # Revenue.object
        send_mail(
        "Request for frenchise",
        "Your request for a franchise is under review. Our team will get back to you within 24 hours.",
        "mmaurya7475@gmail.com",
        [raw_email],
        fail_silently=False,
        )
            
        return redirect('home')
        # return render(request, 'frenchise/frenchise_registration.html',  {'r_form': r_form})
        
    else:
        r_form = FrenchiseRegistrationForm()
        return render(request, 'frenchise/frenchise_registration.html', {'r_form': r_form})





@login_required
def frenchise_application_view(request):
    if request.method == 'POST':
        a_form = frenchise_application_form(request.POST)
        current_user = request.user 
        print("fhjkl")
        print(current_user)
        if a_form.is_valid():
            # print(request.User)
            a_form.instance.user=current_user
            a_form.save()
        
            return redirect('dashboard')
        return render(request, 'frenchise/frenchise_profile.html',  {'a_form': a_form})
        
    else:
        a_form = frenchise_application_form()
        return render(request, 'frenchise/frenchise_apply_form.html', {'a_form': a_form})

#About
def about_view(request):
    return render(request, 'frenchise/about.html' )

#Services 
def Services_view(request):
    return render(request, 'frenchise/services.html' )

#Blog 
def blog_view(request):
    return render(request, 'frenchise/blog.html' )

#Blog Details
def blog_details_view(request):
    return render(request, 'frenchise/blog_details.html' )

#Contact Us
def contact_view(request):
    return render(request, 'frenchise/contact.html' )




#
def profile(request):
    return render(request, 'frenchise/frenchise_profile.html' )





@login_required
def employee_view(request):

    if request.method == 'POST':
        # emp_form = Employee_application_form(data=request.POST)

        # if emp_form.is_valid():
            # Validate the employee ID and email address
        employee_ids = request.POST.get('employee_id')
        emails = request.POST.get('email')
        name = request.POST.get('name')
        usernames = request.POST.get('username')
        usernames = usernames+"_emp"
        passwords = request.POST.get('password')
        employee_creation = frenchise_employee_register_model.objects.create(user=request.user,name=name, employee_id=employee_ids,email=emails,username=usernames, password=passwords)       
        # usernames = usernames +'_emp'
        user = User.objects.create(
            username=  usernames
        
            # role='User',
            # password=passs,
        )
        v = user.set_password(passwords)
        print(v)
        # user.save()
        # print([name,raw_password,raw_city,raw_dob,raw_education,raw_state,raw_number,raw_occupation])
        # user = r_form.save()
        # user.is_active = False
        user.save()
        users = User.objects.get(username=usernames)
            # user.is_active = False
        users.passwo = passwords
        # ProfileFrenchise.objects.create(user=users,DOB=raw_dob,state=raw_state,email=raw_email,city=raw_city,number=raw_number,Occupation=raw_occupation,Education=raw_education)

    #     user = models.ForeignKey(User, on_delete=models.CASCADE)
    # employee_id = models.IntegerField(default=123456)
    # email = models.EmailField(null=False, blank=False, default= 'employee@gmail.com')
    # username = models.CharField(max_length=15,null=False, blank=False, default='Username')
    # password = models.CharField(max_length=50)
   
        print('sjjdgjksgkjbskjbk')
        # user = emp_form.save()
        # user.save()

        print('mansjhisbbbdg')

            # if not validate_employee_id(employee_id):
            #     raise ValidationError('Invalid employee ID.')
            # if not validate_email(email):
            #     raise ValidationError('Invalid email address.')

            # Save the employee application form
            # emp_form.save()

            # Authenticate the user
        # user = authenticate(employee_id=employee_id, email=email,username=username,password=password)
            # login(request, user)

            # Redirect the user to the dashboard
        return redirect('dashboard')

        # If the form is not valid, re-render the form
        return render(request, 'frenchise/employee_dashboard.html', {'emp_form': emp_form})

    else:
        # If the request method is not POST, render the employee application form
        emp_form = Employee_application_form()
        return render(request, 'frenchise/employeregistration.html', {'emp_form': emp_form})
    

#frenchise status True or False

def check_active_frenchise(request):
    if request.method == 'POST':
        active_user = request.POST.get('activeuser')
        if active_user:
            user = User.objects.get(pk=active_user)
            user.is_active = True
            user.save()
        # if request.POST.get('activeuser'):
        #     allUser = User.objects.all()
        #     data = User()
        #  
        #     data.is_active = request.POST.get('activeuser')
        #     data.save()
            
            return render(request,'frenchise/admin_dashboard.html')
    else:
        
        return render(request,'frenchise/admin_dashboard.html')
            
@login_required
def all_frenchise_employe_view(request,frenchid):
    loginUser = request.user
    if loginUser.is_superuser:
        user = get_object_or_404(User, id=frenchid)
        
        # You can directly access the username using user.username
        usernm = user.username
        print(usernm)
        # Query the 'frenchise_employee_register_model' model using the retrieved username
        e_data = frenchise_employee_register_model.objects.filter(user=user)
        all_data = []
        for data in e_data:
            u = data.user
            usernames = data.username
            userdataemp = User.objects.filter(username=usernames)
            # print
            for i in userdataemp:
                usrnme = i.id
            loandata = Loan.objects.filter(user=usrnme)
            count_loan = loandata.count()
            print(count_loan)

            insurance_data = Insurance.objects.filter(user=usrnme)
            count_insurance = insurance_data.count()

            total_sales = count_loan + count_insurance

            data_dict = {
                'id': data.id,
                'employee_id':data.employee_id,
                'username': data.username,
                'email': data.email,
                'total':total_sales,
                'loan':count_loan,
                'insurance':count_insurance
            }
            all_data.append(data_dict)
        return render(request, 'frenchise/all_frenchise_employee_dashboard.html', {'e_data': all_data})

def employee_data_chart(request):
    # Sample employee data (replace with your actual data)
    employees = ['Employee 1', 'Employee 2', 'Employee 3']
    loan_counts = [5, 8, 3]
    insurance_counts = [2, 6, 1]

    # Create a bar chart
    plt.figure(figsize=(8, 4))
    plt.bar(employees, loan_counts, label='Loans')
    plt.bar(employees, insurance_counts, bottom=loan_counts, label='Insurance')

    plt.xlabel('Employees')
    plt.ylabel('Count')
    plt.title('Loan and Insurance Data for Employees')
    plt.legend()

    # Save the chart to a BytesIO object
    chart_buffer = BytesIO()
    plt.savefig(chart_buffer, format='png')
    chart_buffer.seek(0)
    chart_data = base64.b64encode(chart_buffer.read()).decode()
    plt.close()

    context = {
        'chart_data': chart_data,
    }

    return render(request, 'your_template.html', context)

#dashboard
@login_required
def dashboard(request):
    loginUser = request.user
    n = loginUser.username
    words = n.split()
    print(words)
    check = True
    print(len(n))
    if len(n) > 4:
        checkforemp  = n[-4:]

        if checkforemp == '_emp':
            check = False

        
    # profiledata = ProfileFrenchise.objects.get(user=loginUser)
    print(check)
    if loginUser.is_superuser:
        allUser = User.objects.all()
        users_without_emp = User.objects.exclude(username__endswith='_emp')
        return render(request,'frenchise/admin_dashboard.html',{'usersWithout':users_without_emp})
        # print(users_without_emp)
        # for i in users_without_emp:
        #     print(i)
    if check:
        f_register = frenchise_register_model.objects.filter(user=request.user)
        e_register = frenchise_employee_register_model.objects.filter(user=request.user)

        all_data = []
        for data in e_register:
            u = data.user
            usernames = data.username
            userdataemp = User.objects.filter(username=usernames)
            # print
            for i in userdataemp:
                usrnme = i.id

            current_date = datetime.now()
            current_year = current_date.year
            current_month = current_date.month
            current_day = current_date.day

            formatted_date = current_date.strftime('%Y-%m-%d')
            print(formatted_date)
            # loan data fiilter model
            loandataActive = Loan.objects.filter(user=usrnme,status='Active')
            loandata = Loan.objects.filter(user=usrnme)
            loancount = loandata.count()
            loandataInprogress = Loan.objects.filter(user=usrnme,status='In Progesss')
            loandataCompleted = Loan.objects.filter(user=usrnme,status='Completed')
            loandataRejected = Loan.objects.filter(user=usrnme,status='Rejected')
            count_loan_active = loandataActive.count()
            count_loan_InProgress = loandataInprogress.count()
            count_loan_completed = loandataCompleted.count()
            count_loan_rejected = loandataRejected.count()
            # loan data fiilter model

            InsurancedataActive = Insurance.objects.filter(user=usrnme,status='Active')
            Insurancedata = Insurance.objects.filter(user=usrnme)
            insurancecount = Insurancedata.count()
            InsurancedataInprogress = Insurance.objects.filter(user=usrnme,status='In Progesss')
            InsurancedataCompleted = Insurance.objects.filter(user=usrnme,status='Completed')
            InsurancedataRejected = Insurance.objects.filter(user=usrnme,status='Rejected')
            count_Insurance_active = InsurancedataActive.count()
            count_Insurance_InProgress = InsurancedataInprogress.count()
            count_Insurance_completed = InsurancedataCompleted.count()
            count_Insurance_rejected = InsurancedataRejected.count()

            Mutual_FunddataActive = Mutual_Fund.objects.filter(user=usrnme,status='Active')
            Mutual_Funddata = Mutual_Fund.objects.filter(user=usrnme)
            mutualfundcount = Mutual_Funddata.count()
            Mutual_FunddataInprogress = Mutual_Fund.objects.filter(user=usrnme,status='In Progesss')
            Mutual_FunddataCompleted = Mutual_Fund.objects.filter(user=usrnme,status='Completed')
            Mutual_FunddataRejected = Mutual_Fund.objects.filter(user=usrnme,status='Rejected')
            count_Mutual_Fund_active = Mutual_FunddataActive.count()
            count_Mutual_Fund_InProgress = Mutual_FunddataInprogress.count()
            count_Mutual_Fund_completed = Mutual_FunddataCompleted.count()
            count_Mutual_Fund_rejected = Mutual_FunddataRejected.count()

            Demat_AccountdataActive = Demat_Account.objects.filter(user=usrnme,status='Active')
            Demat_Accountdata = Demat_Account.objects.filter(user=usrnme)
            Demat_AccountdataInprogress = Demat_Account.objects.filter(user=usrnme,status='In Progesss')
            Demat_AccountdataCompleted = Demat_Account.objects.filter(user=usrnme,status='Completed')
            Demat_AccountdataRejected = Demat_Account.objects.filter(user=usrnme,status='Rejected')
            count_Demat_Account_active = Demat_AccountdataActive.count()
            count_Demat_Account_count = Demat_Accountdata.count()
            count_Demat_Account_InProgress = Demat_AccountdataInprogress.count()
            count_Demat_Account_completed = Demat_AccountdataCompleted.count()
            count_Demat_Account_rejected = Demat_AccountdataRejected.count()
            
            total_sales =  count_loan_completed + count_Insurance_completed + count_Mutual_Fund_completed + count_Demat_Account_completed
            print("upper loan")


            total_loan = loancount
            total_mf= mutualfundcount
            total_insurance = insurancecount
            total_da= count_Demat_Account_count

            total_submit = total_loan + total_mf + total_insurance + total_da
            # total_revenue = count_Mutual_Fund_completed+count_Insurance_completed+count_loan_completed+count_Demat_Account_completed

        

            data_dict = {
                'id': data.id,
                'total_sales':total_sales,
                'total_loan':total_loan ,
                'total_mf': total_mf,
                'total_insurance':total_insurance,
                'total_da':total_da,
                'total_da_completed':count_Demat_Account_completed,
                'total_mutual_completed':count_Mutual_Fund_completed,
                'total_loan_completed':count_loan_completed,
                'total_insurance_completed':count_Insurance_completed,
                'total_submit':total_submit
            }
            all_data.append(data_dict)
        print(all_data)
        print("ljhjhjhg")
        return render(request, 'frenchise/frenchise_overview.html', {'data_all':all_data})
    else:
        print("jhkjh")
        e_register = frenchise_employee_register_model.objects.filter(username=n)
        return render(request, 'frenchise/employesales.html', {'e_register': e_register})
@login_required
def editfrenchise(request,frenchid):
    users = request.user
    if request.method == 'POST':
        status = request.POST.get('status')
        name = request.POST.get('name')
        address = request.POST.get('address')
        Occupation = request.POST.get('Occupation')
        education = request.POST.get('education')
        number = request.POST.get('number')
        states = request.POST.get('state')
        citys = request.POST.get('city') 
        dateob = request.POST.get('dob')
        coded = request.POST.get('code')
        profileid = request.POST.get('profileid')
        userid = request.POST.get('userdataid')
        date_string = "Oct. 3, 2023"

        # Parse the date string to a datetime object
        date_obj = datetime.strptime(date_string, "%b. %d, %Y")
        print(status)
        if status == 'active':
            status = True
        else:
            status = False
        print(status)
        
        # Format the datetime object to the desired format
        formatted_date = date_obj.strftime("%Y-%m-%d")
        update = ProfileFrenchise.objects.filter(id=profileid).update(frenchise_name=name,Code=coded, DOB=formatted_date,Address_Type=address,Occupation=Occupation,Education=education,number=number,city=citys,state=states)
        updates = User.objects.filter(id=userid).update(is_active=status)
        getIduser = User.objects.get(id=userid)
        user = get_object_or_404(User, id=userid)
        # try:
        getIduser = User.objects.get(id=userid)
        getidProfile = ProfileFrenchise.objects.get(user=getIduser)
        return render(request,'frenchise/editfrenchise.html',{'userdata':getIduser,'profileDta':getidProfile})
        # print(status)
    if users.is_superuser:
        
        getIduser = User.objects.get(id=frenchid)
        user = get_object_or_404(User, id=frenchid)
        try:
            getIduser = User.objects.get(id=frenchid)
            getidProfile = ProfileFrenchise.objects.get(user=getIduser)
            # Now you can access the ProfileFrenchise data associated with the specific user
            print(getidProfile)
        except User.DoesNotExist:
            # Handle the case where the User with the given frenchid doesn't exist
            getIduser = None
            getidProfile = None
            return HttpResponse("user not exist")
        except ProfileFrenchise.DoesNotExist:
            # Handle the case where the ProfileFrenchise for the User doesn't exist
            getidProfile = None
            return HttpResponse("Profile not exist")

        if getidProfile:
            print(getidProfile)
            print(getidProfile)
            return render(request,'frenchise/editfrenchise.html',{'userdata':getIduser,'profileDta':getidProfile})

            # The ProfileFrenchise object exists and can be used here.
        else:
            return HttpResponse("else")



def apply_loan_view(request):
    return render(request, 'frenchise/apply_loan.html')

def frenchise_confirmation(request):
    return render(request, 'frenchise/wait_for_confirmation.html')

def employee_registration_view(request):
    return render(request, 'frenchise/employee.html')

def employee_dashboard_view(request):
    return render(request, 'frenchise/employee_dashboard.html')


@login_required
def edit_employee_dashboard_view(request, empid):
    loginUser = request.user.username
    # getEmployee = frenchise_employee_register_model.objects.filter(id=empid)
    if request.method == 'POST':
        print("inpost")
        emails = request.POST.get('email')
        employeeuiid = request.POST.get('employeId')
        empIds = request.POST.get('empIds')
        print(emails)

        # Update the record using a queryset with the filter condition
        frenchise_employee_register_model.objects.filter(id=empIds).update(email=emails, employee_id=employeeuiid)

        # employee_user = getEmployee.user.username
        # email = getEmployee.email
        # e_fm = Employee_application_form(request.POST, instance=getEmployee)
        # if e_fm.is_valid():
        #     e_fm.save()

        # else:
        getEmployee = frenchise_employee_register_model.objects.get(id=empid)
        e_fm = Employee_application_form(instance=getEmployee)

        return render(request,'frenchise/edit_employee_dashboard.html', {'employeData':getEmployee})



    loginUser = request.user.username
    # getEmployee = frenchise_employee_register_model.objects.filter(id=empid)
    getEmployee = frenchise_employee_register_model.objects.get(id=empid)
    employee_user = getEmployee.user.username
    email = getEmployee.email


    if loginUser == employee_user:
        
        return render(request, 'frenchise/edit_employee_dashboard.html',{'employeData':getEmployee})
    


#Admin Franchise Dashboard

def frenchise_dashboard_admin_view(request):
    return render(request, 'frenchise/frenchise_dashboard_admin.html')

def frenchise_employee_admin_view(request):
    return render(request, 'frenchise/frenchise_employee_admin.html')

@login_required
def appllyloan(request):
    if request.method == 'POST':
        users = request.user
        name = request.POST.get('name')
        emails = request.POST.get('email')
        amount = request.POST.get('amount')
        type = request.POST.get('type')
        number = request.POST.get('number')
        pan = request.POST.get('pan')
        current_date = datetime.now()
        current_year = current_date.year
        current_month = current_date.month
        current_day = current_date.day

        formatted_date = current_date.strftime('%Y-%m-%d')
        print(formatted_date)
        print([name,emails,amount,type,number])
        createloan = Loan.objects.create(user=users,clientName=name,type=type,PAN=pan,number=number,amount=amount,email=emails,creation=formatted_date)
        
        return render(request,'frenchise/apply_loan.html')

    return render(request,'frenchise/apply_loan.html')

#Employee overview 
def employee_overview_view(request):
    return render(request, 'frenchise/employee_overview.html')

# Admin Overview frenchise and employee data
@login_required
def frenchise_overview_view(request):
    loginUser = request.user
    if loginUser.is_superuser:
        return render(request, 'frenchise/frenchise_overview.html')

def loan(request):
    loginUser = request.user
    if loginUser.is_superuser:
        loandata = Loan.objects.exclude(status='Completed')
        Insurancedata = Insurance.objects.exclude(status='Completed')
        Dematdata = Demat_Account.objects.exclude(status='Completed')
        Mutualdata = Mutual_Fund.objects.exclude(status='Completed')
        print(loandata)
        appdata = []
        for i in loandata:
            dataprepare = {
                'id': i.id,
                'type':i.type,
                'name':i.clientName,
                'status':i.status,
                'creation':i.creation,
                'email':i.email,
                'amount':i.amount,
                'number':i.number,
                'PAN':i.PAN,
                'typeof':'Loan'
            }
            appdata.append(dataprepare)
        for i in Insurancedata:
            dataprepare = {
                'id': i.id,
                'type':i.type,
                'name':i.clientName,
                'status':i.status,
                'creation':i.creation,
                'email':i.email,
                'amount':i.amount,
                'number':i.number,
                'PAN':i.PAN,
                'typeof':'Insurance'
            }
            appdata.append(dataprepare)
        for i in Mutualdata:
            dataprepare = {
                'id': i.id,
                'type':i.type,
                'name':i.clientName,
                'status':i.status,
                'creation':i.creation,
                'email':i.email,
                'amount':i.amount,
                'number':i.number,
                'PAN':i.PAN,
                'typeof':'Mutual'
            }
            appdata.append(dataprepare)
        for i in Dematdata:
            dataprepare = {
                'id': i.id,
                'type':i.type,
                'name':i.clientName,
                'status':i.status,
                'creation':i.created,
                'email':i.email,
                'amount':i.amount,
                'number':i.number,
                'PAN':i.PAN,
                'typeof':'Demat'
            }
            appdata.append(dataprepare)
        print(appdata)
        return render(request,'frenchise/loandatarender.html',{'loandata':appdata})


def editsection(request,ad_id,ad_type):
    # print(ad_id,ad_type)
    loginUser = request.user
    if request.method == 'POST':
        name = request.POST.get('name')
        emails = request.POST.get('email')
        amount = request.POST.get('amount')
        type = request.POST.get('type')
        number = request.POST.get('number')
        pan = request.POST.get('pan')
        istype = request.POST.get('istype')
        ad_id = request.POST.get('ad_id')
        statuss = request.POST.get('status')
        print(statuss)
        print([name,emails,amount,type,number,pan,istype,ad_id,statuss])
        if loginUser.is_superuser:
            if istype == 'Loan':
                update = Loan.objects.filter(id=ad_id).update(clientName=name,PAN=pan,number=number,amount=amount,email=emails,status=statuss)
            if istype == 'Insurance':
                update = Insurance.objects.filter(id=ad_id).update(clientName=name,PAN=pan,number=number,amount=amount,email=emails,status=statuss)
                return redirect('loans')
                print("")

            if istype == 'Demat':
                update = Demat_Account.objects.filter(id=ad_id).update(clientName=name,PAN=pan,number=number,amount=amount,email=emails,status=statuss)
                return redirect('loans')

            if istype == 'Mutual':
                update = Mutual_Fund.objects.filter(id=ad_id).update(clientName=name,PAN=pan,number=number,amount=amount,email=emails,status=statuss)
                print(update)
                return redirect('loans')



    if loginUser.is_superuser:
        if ad_type == 'Loan':
            dataEdit = Loan.objects.get(id=ad_id)
            return render(request,'frenchise/Editloan.html',{'ad_data':dataEdit,'type':'Loan'})
            print('in loan')
        if ad_type == 'Insurance':
            dataEdit = Insurance.objects.get(id=ad_id)
            return render(request,'frenchise/Editloan.html',{'ad_data':dataEdit,'type':'Insurance'})
            print('in Insurance')
        if ad_type == 'Mutual':
            dataEdit = Mutual_Fund.objects.get(id=ad_id)
            return render(request,'frenchise/Editloan.html',{'ad_data':dataEdit,'type':'Mutual'})
            print('in Mutual')
        if ad_type == 'Demat':
            dataEdit = Demat_Account.objects.get(id=ad_id)
            return render(request,'frenchise/Editloan.html',{'ad_data':dataEdit,'type':'Demat'})
            print('in Demat')

    
# def frenchise_chart_view(request):
#     if request.method == 'POST':
#         print("date from to")

#     total = {
#         'toatal':"455",
#         'success':"105"
#     }
#     chart = {
#         'loan':'255',
#         'insurance':'200',
#         'demat':'204',
#         'mutualFund':'255',
#     }


# MOSL - authentication
def mosl_login(request):
    # Set the password, apiKey, and authtoken
    password = "abcd"
    apiKey = "abc"
    authtoken = "d3bcc86824264c689bf18052bb724fa5_M"

    # Define the URL for the production environment
    url = f"http://uattrade.motilaloswal.com:83/OpenAPI/Login.aspx?apikey={apiKey}"

    # Calculate the SHA-256 hash of the password and apiKey
    combined_string = password + apiKey
    hash_object = hashlib.sha256(combined_string.encode())
    hashed_password = hash_object.hexdigest()

    # Prepare the request data
    request_data = {
        "userid": "AA017",
        "password": hashed_password,
        "2FA": "18/10/1988",
        "totp": "Authenticator 6 digit Code"
    }
    print(request_data)
   
   # Send a GET request with the request data as parameters
    try:
        response = requests.get(url, params=request_data, headers={'authtoken': authtoken})

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "Login request sent."})


def mosl_logout(request):

    url = "https://uatopenapi.motilaloswal.com/rest/login/v1/logout"

    request_data = {
    "userid":"AA017"
    }
    
    headers = {
        "Accept": "application/json",  # Indicate that you expect a JSON response
        "Content-Type": "application/json",  # Specify the format of your request data
        # "UserAgent": "frenchise/1.0",
    }

    print(request_data)

    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=request_data, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "Logout Successfully."})

#MOSL - Order
def mosl_place_order(request):

    url = "	https://uatopenapi.motilaloswal.com/rest/trans/v1/placeorder"

    order_data_placed = {
        "clientcode": "AA017",
        "symboltoken": 1660,
        "buyorsell": "BUY",
        "ordertype": "LIMIT",
        "producttype": "Normal",
        "orderduration": "DAY",
        "price": 235.5,
        "triggerprice": 0,
        "quantityinlot": 2,
        "disclosedquantity": 0,
        "amoorder": "N",
        "algoid": "",
        "goodtilldate": "30-Jan-2022",
        "tag": "",
        "participantcode": "218450147IH"
    }
    
    headers = {
        "Accept": "application/json",  # Indicate that you expect a JSON response
        "Content-Type": "application/json",  # Specify the format of your request data
        # "UserAgent": "frenchise/1.0",
    }

    print(order_data_placed)

    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=order_data_placed, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "order placed successfully."})


def mosl_modify_order(request):
    url = "	https://uatopenapi.motilaloswal.com/rest/trans/v2/modifyorder"
    modify_data = {
    "clientcode":"AA017", 
    "uniqueorderid ":"1101823KAL005",
    "newordertype":"LIMIT",
    "neworderduration":"DAY",
    " newquantityinlot ":100,
    "newdisclosedquantity":0,
    "newprice":235.50,
    "newtriggerprice":0,
    "newgoodtilldate":"",
    "lastmodifiedtime": "14-May-2022 11:31:25",
    "qtytradedtoday": 0
    }

    print(modify_data)

    headers = {
        "Accept": "application/json",  # Indicate that you expect a JSON response
        "Content-Type": "application/json",  # Specify the format of your request data
        # "UserAgent": "frenchise/1.0",
    }


    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=modify_data, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "Modify data successfully."})

def mosl_cancel_order(request):
    url = "https://uatopenapi.motilaloswal.com/rest/trans/v1/cancelorder"

    cancel_order_data = {
    "clientcode":"",
    "uniqueorderid":"1101823KAL005"
    }

    print(cancel_order_data)

    headers = {
        "Accept": "application/json",  # Indicate that you expect a JSON response
        "Content-Type": "application/json",  # Specify the format of your request data
        # "UserAgent": "frenchise/1.0",
    }

    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=cancel_order_data, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "Cancel Order successfully."})


def mosl_order_book(request):
    url = "https://uatopenapi.motilaloswal.com/rest/book/v2/getorderbook"

    order_book = {
    "clientcode":"AA017" 
    }

    print(order_book)

    headers = {
        "Accept": "application/json",  # Indicate that you expect a JSON response
        "Content-Type": "application/json",  # Specify the format of your request data
        # "UserAgent": "frenchise/1.0",
    }

    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=order_book, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "Your order Book."})



def mosl_trade_book(request):
    url = "	https://openapi.motilaloswal.com/rest/book/v1/gettradebook"

    trade_book = {
    "clientcode":"AA017"
    }

    print(trade_book)

    headers = {
        "Accept": "application/json", 
        "Content-Type": "application/json", 
        # "UserAgent": "frenchise/1.0",
    }

    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=trade_book, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "Your trade Book."})


def mosl_orderdetails(request):
    url = "	https://openapi.motilaloswal.com/rest/book/v2/getorderdetailbyuniqueorderid"

    order_details = {
    "clientcode":"", 
    "uniqueorderid":"1000001AA020"
    }

    print(order_details)

    headers = {
        "Accept": "application/json", 
        "Content-Type": "application/json", 
        # "UserAgent": "frenchise/1.0",
    }

    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=order_details, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "Your order details Book."})



def mosl_tradedetails(request):
    url = "	https://openapi.motilaloswal.com/rest/book/v1/gettradedetailbyuniqueorderid"

    trade_details = {
    "clientcode":"AA017",
    "uniqueorderid":"2700002AA020"
    }
    print(trade_details)

    headers = {
        "Accept": "application/json", 
        "Content-Type": "application/json", 
        # "UserAgent": "frenchise/1.0",
    }

    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=trade_details, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "Your trade details Book."})

#Portfolio
def mosl_holdings(request):
    url = "	https://openapi.motilaloswal.com/rest/report/v1/getdpholding"

    holdings = {
    "clientcode":"AA017"
    }
    print(holdings)

    headers = {
        "Accept": "application/json", 
        "Content-Type": "application/json", 
        # "UserAgent": "frenchise/1.0",
    }

    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=holdings, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "Your Holdings"})


def mosl_position(request):
    url = "	https://openapi.motilaloswal.com/rest/book/v1/getposition"

    position = {
    "clientcode":"AA017"
    }
    print(position)

    headers = {
        "Accept": "application/json", 
        "Content-Type": "application/json", 
        # "UserAgent": "frenchise/1.0",
    }

    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=position, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "Your Position"})


def mosl_position_conversion(request):
    url = "https://openapi.motilaloswal.com/rest/trans/v1/positionconversion"

    position_conversion = {
    "clientcode":"KAL005", 
    "exchange":"NSE",
    "scripcode":1660,
    "quantity":100,
    "oldproduct":"Normal",
    "newproduct":"ValuePlus"
    }
    print(position_conversion)

    headers = {
        "Accept": "application/json", 
        "Content-Type": "application/json", 
        # "UserAgent": "frenchise/1.0",
    }

    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=position_conversion, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "Your Position Conversion"})


def mosl_position_details(request):

    url = "	https://openapi.motilaloswal.com/rest/book/v1/getpositiondetail"

    position_details = {
    "clientcode":"AA020" 
    }

    print(position_details)

    headers = {
        "Accept": "application/json", 
        "Content-Type": "application/json", 
        # "UserAgent": "frenchise/1.0",
    }

    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=position_details, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "Your Position Details"})

# MOSL - Limit/Margin - Price/LTP
def mosl_margin_summary(request):

    url = "	https://openapi.motilaloswal.com/rest/report/v1/getreportmarginsummary"

    margin_summary = {
    "clientcode":"AA020" 
    }

    print(margin_summary)

    headers = {
        "Accept": "application/json", 
        "Content-Type": "application/json", 
        # "UserAgent": "frenchise/1.0",
    }

    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=margin_summary, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "Your Margin Summary"})

def mosl_margin_details(request):

    url = "	https://openapi.motilaloswal.com/rest/report/v1/getreportmargindetail"

    margin_details = {
    "clientcode":"AA020" 
    }

    print(margin_details)

    headers = {
        "Accept": "application/json", 
        "Content-Type": "application/json", 
        # "UserAgent": "frenchise/1.0",
    }

    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=margin_details, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "Your Margin Details"})

def mosl_Price(request):


    url = "https://openapi.motilaloswal.com/rest/report/v1/getltpdata"

    price = {
    "clientcode":"AA020",
    "scripcode":500317
    }
    print(price)

    headers = {
        "Accept": "application/json", 
        "Content-Type": "application/json", 
        # "UserAgent": "frenchise/1.0",
    }

    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=price, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "Price"})


# MOSL - Master data & DPR Data
def mosl_scrips(request):

    url = "	https://openapi.motilaloswal.com/rest/report/v1/getscripsbyexchangename"

    scrips_FO = {
    "clientcode":"AA020", 
    "exchangename":"NSEFO"
    }
    print(scrips_FO)

    headers = {
        "Accept": "application/json", 
        "Content-Type": "application/json", 
        # "UserAgent": "frenchise/1.0",
    }

    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=scrips_FO, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "Scrips"})

def mosl_DPR(request):

    url = "	https://openapi.motilaloswal.com/rest/report/v1/getdprvalues"

    DPR = {
    "clientcode":"",
    "symbol":"BANKNIFTY"
    }
    print(DPR)

    headers = {
        "Accept": "application/json", 
        "Content-Type": "application/json", 
        # "UserAgent": "frenchise/1.0",
    }

    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=DPR, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "DPR"})


# MOSL - index
def mosl_index(request):
    return render(request, 'market/mosl_index.html')




















































































































































