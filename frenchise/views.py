from django.shortcuts import render,redirect, HttpResponse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.views import View
from django.contrib.auth.models import User
from .models import *
from .forms import FrenchiseRegistrationForm, frenchise_application_form, Employee_application_form
from django.views.decorators.csrf import csrf_exempt
from fastapi.responses import RedirectResponse, HTMLResponse
from django.core.mail import send_mail

from django.shortcuts import get_object_or_404
from companystaff.models import *
# from .filters import frenchise_filter
from datetime import datetime
import re
from django.db.models import Sum

from decimal import Decimal

# Create your views here.
# import matplotlib.pyplot as plt
from io import BytesIO
import base64


def Marketdas(request):
    return render(request, 'market_dashboard/template/all_indices.html' )

def empdas(request):
    return render(request, 'employe_dashboard/template/loan_form.html' )

@csrf_exempt
@login_required
def admindas(request):
    user_login  = request.user
    if user_login.is_superuser:
        total_loan_completed = Loan.objects.filter(status='Completed').count()
        print(total_loan_completed)
        total_loan_pending = Loan.objects.filter(status='In Progress').count()
        total_Insurance_completed = Insurance.objects.filter(status='Completed').count()
        total_Insurance_pending = Insurance.objects.filter(status='In Progress').count()
        total_mutual_completed = Mutual_Fund.objects.filter(status='Completed').count()
        total_mutual_pending = Mutual_Fund.objects.filter(status='In Progress').count()
        total_demate_completed = Demat_Account.objects.filter(status='Completed').count()
        total_demate_pending = Demat_Account.objects.filter(status='In Progress').count()
        total = total_loan_completed + total_Insurance_completed + total_mutual_completed + total_demate_completed
        total_pending = total_loan_pending + total_Insurance_pending + total_mutual_pending + total_demate_pending

        # 

        total_revenue = Revenue.objects.aggregate(total_amount=Sum('amount'))['total_amount'] or 0.0
        print(total_revenue)
        total_data = {
            'loan_completed':total_loan_completed,
            'loan_pending':total_loan_pending,
            'insurance_completed':total_Insurance_completed,
            'insurance_pending':total_Insurance_pending,
            'mutual_completed':total_mutual_completed,
            'mutual_pending':total_mutual_pending,
            'demate_completed':total_demate_completed,
            'demate_pending':total_demate_pending,
            'total_sale': total,
            'total_pending':total_pending,
            'total_revenue_distributed':total_revenue
        }
        print(total_data)
        return render(request, 'admin_dashboard/template/admin_home.html',{'total_data':total_data} )

    return render(request, 'admin_dashboard/template/admin_home.html' )

def index(request):
    return render(request, 'frenchise/index.html' )

#admin Search
@csrf_exempt
@login_required
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
@csrf_exempt
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
        ProfileFrenchise.objects.create(user=users,DOB=raw_dob,state=raw_state,email=raw_email,city=raw_city,number=raw_number,Occupation=raw_occupation,Education=raw_education,Role="Frenchise",partner_at=0.5)
        Revenue.objects.create(user=user,amount=0)
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





@csrf_exempt
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




@csrf_exempt
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

    else:
        # If the request method is not POST, render the employee application form
        emp_form = Employee_application_form()
        return render(request, 'frenchise_dashboard/template/emp_register.html', {'emp_form': emp_form})
    

#frenchise status True or False
@csrf_exempt
@login_required
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
            
@csrf_exempt
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
            loan_completed = Loan.objects.filter(user=usrnme)
            count_loan_completed = loan_completed.count()

            insurance_data = Insurance.objects.filter(user=usrnme)
            count_insurance = insurance_data.count()
            Insurance_completed = Insurance.objects.filter(user=usrnme)
            count_Insurance_completed = Insurance_completed.count()

            mutualfunddata = Mutual_Fund.objects.filter(user=usrnme)
            count_mf = mutualfunddata.count()
            mf_completed = Mutual_Fund.objects.filter(user=usrnme)
            count_mf_completed = mf_completed.count()

            dematdata = Demat_Account.objects.filter(user=usrnme)
            count_demat = dematdata.count()
            demat_completed = Demat_Account.objects.filter(user=usrnme)
            count_demat_completed = demat_completed.count()

            total_sales = count_loan + count_insurance + count_mf + count_demat

            data_dict = {
                'id': data.id,
                'employee_id':data.employee_id,
                'username': data.username,
                'email': data.email,
                'total':total_sales,
                'loan':count_loan,
                'insurance':count_insurance,
                'mutualfund': count_mf,
                "demat": count_demat,
                "loan_completed": count_loan_completed,
                "insurance_completed": count_Insurance_completed,
                "mutualfund_completed": count_mf_completed,
                "demat_completed": count_demat_completed,
                "total_sales": total_sales
            }
            all_data.append(data_dict)
        return render(request, 'admin_dashboard/template/emp_register_by_frenchise.html', {'e_data': all_data})

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
@csrf_exempt
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
        return render(request,'admin_dashboard/template/all_frenchise.html',{'usersWithout':users_without_emp})
        # print(users_without_emp)
        # for i in users_without_emp:
        #     print(i)
    if check:
        f_register = frenchise_register_model.objects.filter(user=request.user)
        e_register = frenchise_employee_register_model.objects.filter(user=request.user)
        try:
            total_revenue = Revenue.objects.get(user=request.user)
            print("Total Revenue", total_revenue.amount)
            total_earning = total_revenue.amount
        except Revenue.DoesNotExist:
            # Handle the case where no record is found for the user
            total_revenue = None
            total_earning = 0.0

        # total_revenue = Revenue.objects.get(user=request.user)
        # for i in total_revenue:
        #     print(i.amount)

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

            count_L = count_loan_active + count_loan_InProgress
            count_Insur = count_Insurance_active + count_Insurance_InProgress
            count_mf = count_Mutual_Fund_active + count_Mutual_Fund_InProgress
            count_da = count_Demat_Account_active + count_Demat_Account_InProgress

            total_submit = total_loan + total_mf + total_insurance + total_da
            # count_total_active_and_progress = count_loan_active + count_loan_InProgress + count_Insurance_active +count_Insurance_InProgress + count_Mutual_Fund_active + count_Mutual_Fund_InProgress + count_Demat_Account_active + count_Demat_Account_InProgress
            # count_loan_insurance_mf_da_completed = count_loan_completed + count_Insurance_completed + count_Mutual_Fund_completed + count_Demat_Account_completed

            # total_revenue = count_Mutual_Fund_completed+count_Insurance_completed+count_loan_completed+count_Demat_Account_completed

        

            data_dict = {
                'id': data.id,
                'total_sales':total_sales,

                'total_loan':total_loan,
                "count_loan_active": count_loan_active,
                "count_loan_progress":count_loan_InProgress,
                "count_loan rejected": count_loan_rejected,
                'total_loan_completed':count_loan_completed,

                
                'total_insurance':total_insurance,
                "count_insurance_active": count_Insurance_active,
                "count_insurance_progress":count_Insurance_InProgress,
                "count_insurance rejected": count_Insurance_rejected,
                'total_insurance_completed':count_Insurance_completed,

                'total_mf': total_mf,
                'total_insurance':total_insurance,
                "count_mf_active": count_Mutual_Fund_active,
                "count_mf_progress":count_Mutual_Fund_InProgress,
                "count_mf rejected": count_Mutual_Fund_rejected,
                'total_mutual_completed':count_Mutual_Fund_completed,

                'total_da':total_da,
                "count_da_active": count_Demat_Account_active,
                "count_da_progress":count_Demat_Account_InProgress,
                "count_da rejected": count_Demat_Account_rejected,
                'total_da_completed':count_Demat_Account_completed,

                "count_L": count_L,
                "count_Insur":count_Insur,
                "count_mf": count_mf,
                "count_da": count_da,
                
           
                # "count_total_active_and_progress": count_total_active_and_progress,
                # "count_loan_insurance_mf_da_completed": count_loan_insurance_mf_da_completed,
                'total_submit':total_submit,
                "total_earning": total_earning,

            }
            all_data.append(data_dict)
        print(all_data)
        print("ljhjhjhg")
        return render(request, 'frenchise_dashboard/template/frenchise_dash.html', {'data_all':all_data[0]})
    else:
        print("jhkjh")
        emp_register = frenchise_employee_register_model.objects.filter(username=n)

        emp_all_data = []
        for data in emp_register:
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
                'total_submit':total_submit,
                # "total_earning": total_earning
            }
            emp_all_data.append(data_dict)
        print("employee application data", emp_all_data)
        print("empalldatahdfkj")
        return render(request, 'employe_dashboard/template/employe_dash.html', {'e_all_data': emp_all_data})
    
@csrf_exempt
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
        return render(request,'admin_dashboard/template/edit_frenchise.html',{'userdata':getIduser,'profileDta':getidProfile})
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
            return render(request,'admin_dashboard/template/edit_frenchise.html',{'userdata':getIduser,'profileDta':getidProfile})

            # The ProfileFrenchise object exists and can be used here.
        else:
            return HttpResponse("else")



def apply_loan_view(request):
    return render(request, 'frenchise/apply_loan.html')

def frenchise_confirmation(request):
    return render(request, 'frenchise/wait_for_confirmation.html')

def employee_registration_view(request):
    return render(request, 'frenchise/employee.html')

@csrf_exempt
@login_required
def employee_dashboard_view(request):
    # loginusers = request.user
    loginUser = request.user.username
    print(loginUser)
    if request.method == 'POST':
        if '_emp' not in loginUser:
            name = request.POST.get('search')
            print(name)
            print(type(name))
            email_pattern = r'^[\w\.-]+@[\w\.-]+$'
            if re.match(email_pattern, name):
                employedata = frenchise_employee_register_model.objects.filter(user = request.user,email=name)

                print('email')

            if name.isnumeric():
                
                employedata = frenchise_employee_register_model.objects.filter(user = request.user,number=name)

                print('The name contains only numbers.')
            if name.isalpha():
                print('name')
                employedata = frenchise_employee_register_model.objects.filter(user = request.user,name=name)

            # employedata = frenchise_employee_register_model.objects.filter(user = request.user)
            print(employedata)
            if employedata:
                emp_data = []
                for i in employedata:
                    loanuser = User.objects.get(username=i.username)
                    loandata = Loan.objects.filter(user=loanuser)
                    loandatacompleted = Loan.objects.filter(user=loanuser,status='Completed')
                    Insurancedata = Insurance.objects.filter(user=loanuser)
                    Insurancedatacompleted = Insurance.objects.filter(user=loanuser,status='Completed')
                    Mutualdata = Mutual_Fund.objects.filter(user=loanuser)
                    Mutualdatacompleted = Mutual_Fund.objects.filter(user=loanuser,status='Completed')
                    Dematdata = Demat_Account.objects.filter(user=loanuser)
                    Dematdatacompleted = Demat_Account.objects.filter(user=loanuser,status='Completed')
                    total_sale = loandata.count()+Insurancedata.count()+Mutualdata.count()+Dematdata.count()
                    print("---------")
                    print(loandata)
                    data_emp = {
                        'Name':i.name,
                        'id':i.id,
                        'email':i.email,
                        'username':i.username,
                        'total_sale':total_sale,
                        'total_loan':loandata.count(),
                        'total_loan_completed':loandatacompleted.count(),
                        'total_insurance':Insurancedata.count(),
                        'total_insurance_completed':Insurancedatacompleted.count(),
                        'total_mutual':Mutualdata.count(),
                        'total_mutual_completed':Mutualdatacompleted.count(),
                        'total_demat':Dematdata.count(),
                        'total_demat_completed':Dematdatacompleted.count(),
                    }
                    emp_data.append(data_emp)

                print(emp_data)
                return render(request, 'frenchise/employee_overview.html',{'em_data':emp_data})
            else:
                return render(request,'frenchise/404.html')

    if '_emp' in loginUser:
        return render(request,'frenchise/404.html')
    else:
        print("lgjjkhjgflkhjflkh")
        employedata = frenchise_employee_register_model.objects.filter(user = request.user)
        print("employedata" ,employedata)
        emp_data = []
        for i in employedata:
            loanuser = User.objects.get(username=i.username)
            loandata = Loan.objects.filter(user=loanuser)
            loandatacompleted = Loan.objects.filter(user=loanuser,status='Completed')
            Insurancedata = Insurance.objects.filter(user=loanuser)
            Insurancedatacompleted = Insurance.objects.filter(user=loanuser,status='Completed')
            Mutualdata = Mutual_Fund.objects.filter(user=loanuser)
            Mutualdatacompleted = Mutual_Fund.objects.filter(user=loanuser,status='Completed')
            Dematdata = Demat_Account.objects.filter(user=loanuser)
            Dematdatacompleted = Demat_Account.objects.filter(user=loanuser,status='Completed')
            total_sale = loandata.count()+Insurancedata.count()+Mutualdata.count()+Dematdata.count()
            print("---------")
            print("loandata", loandata)
            data_emp = {
                'Name':i.name,
                'id':i.id,
                'email':i.email,
                'username':i.username,
                'total_sale':total_sale,
                'total_loan':loandata.count(),
                'total_loan_completed':loandatacompleted.count(),
                'total_insurance':Insurancedata.count(),
                'total_insurance_completed':Insurancedatacompleted.count(),
                'total_mutual':Mutualdata.count(),
                'total_mutual_completed':Mutualdatacompleted.count(),
                'total_demat':Dematdata.count(),
                'total_demat_completed':Dematdatacompleted.count(),
            }
            emp_data.append(data_emp)

        print("empdata", emp_data)
        return render(request, 'frenchise/employee_overview.html',{'emp_data':emp_data})
    
@csrf_exempt
@login_required
def date_filter(request):
    loginUser = request.user.username
    print(loginUser)
    if request.method == 'POST':
        if '_emp' not in loginUser:
            name = request.POST.get('search')
            print(name)
            print(type(name))
            email_pattern = r'^[\w\.-]+@[\w\.-]+$'
            if re.match(email_pattern, name):
                employedata = frenchise_employee_register_model.objects.filter(user = request.user,email=name)

                print('email')

            if name.isnumeric():
                employedata = frenchise_employee_register_model.objects.filter(user = request.user,number=name)

                print('The name contains only numbers.')
            if name.isalpha():
                print('name')
                employedata = frenchise_employee_register_model.objects.filter(user = request.user,name=name)

            # employedata = frenchise_employee_register_model.objects.filter(user = request.user)
            print(employedata)
            if employedata:
                emp_data = []
                for i in employedata:
                    loanuser = User.objects.get(username=i.username)
                    loandata = Loan.objects.filter(user=loanuser)
                    loandatacompleted = Loan.objects.filter(user=loanuser,status='Completed')
                    Insurancedata = Insurance.objects.filter(user=loanuser)
                    Insurancedatacompleted = Insurance.objects.filter(user=loanuser,status='Completed')
                    Mutualdata = Mutual_Fund.objects.filter(user=loanuser)
                    Mutualdatacompleted = Mutual_Fund.objects.filter(user=loanuser,status='Completed')
                    Dematdata = Demat_Account.objects.filter(user=loanuser)
                    Dematdatacompleted = Demat_Account.objects.filter(user=loanuser,status='Completed')
                    total_sale = loandata.count()+Insurancedata.count()+Mutualdata.count()+Dematdata.count()
                    print("---------")
                    print(loandata)
                    data_emp = {
                        'Name':i.name,
                        'id':i.id,
                        'email':i.email,
                        'username':i.username,
                        'total_sale':total_sale,
                        'total_loan':loandata.count(),
                        'total_loan_completed':loandatacompleted.count(),
                        'total_insurance':Insurancedata.count(),
                        'total_insurance_completed':Insurancedatacompleted.count(),
                        'total_mutual':Mutualdata.count(),
                        'total_mutual_completed':Mutualdatacompleted.count(),
                        'total_demat':Dematdata.count(),
                        'total_demat_completed':Dematdatacompleted.count(),
                    }
                    emp_data.append(data_emp)

                print(emp_data)
                return render(request, 'frenchise/employee_overview.html',{'em_data':emp_data})
            else:
                return render(request,'frenchise/404.html')

    if '_emp' in loginUser:
        return render(request,'frenchise/404.html')
    else:
        print("lgjjkhjgflkhjflkh")
        employedata = frenchise_employee_register_model.objects.filter(user = request.user)
        print("employedata" ,employedata)
        emp_data = []
        for i in employedata:
            loanuser = User.objects.get(username=i.username)
            loandata = Loan.objects.filter(user=loanuser)
            loandatacompleted = Loan.objects.filter(user=loanuser,status='Completed')
            Insurancedata = Insurance.objects.filter(user=loanuser)
            Insurancedatacompleted = Insurance.objects.filter(user=loanuser,status='Completed')
            Mutualdata = Mutual_Fund.objects.filter(user=loanuser)
            Mutualdatacompleted = Mutual_Fund.objects.filter(user=loanuser,status='Completed')
            Dematdata = Demat_Account.objects.filter(user=loanuser)
            Dematdatacompleted = Demat_Account.objects.filter(user=loanuser,status='Completed')
            total_sale = loandata.count()+Insurancedata.count()+Mutualdata.count()+Dematdata.count()
            print("---------")
            print("loandata", loandata)
            data_emp = {
                'Name':i.name,
                'id':i.id,
                'email':i.email,
                'username':i.username,
                'total_sale':total_sale,
                'total_loan':loandata.count(),
                'total_loan_completed':loandatacompleted.count(),
                'total_insurance':Insurancedata.count(),
                'total_insurance_completed':Insurancedatacompleted.count(),
                'total_mutual':Mutualdata.count(),
                'total_mutual_completed':Mutualdatacompleted.count(),
                'total_demat':Dematdata.count(),
                'total_demat_completed':Dematdatacompleted.count(),
            }
            emp_data.append(data_emp)

        print("empdata", emp_data)
        return render(request, 'frenchise/employee_overview.html',{'emp_data':emp_data})




@csrf_exempt
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

@csrf_exempt
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
        
        return render(request,'frenchise_dashboard/template/loan_form.html')

    return render(request,'frenchise_dashboard/template/loan_form.html')

@csrf_exempt
@login_required
def apply_insurance(request):
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
        createloan = Insurance.objects.create(user=users,clientName=name,type=type,PAN=pan,number=number,amount=amount,email=emails,creation=formatted_date)
        
        return render(request,'frenchise_dashboard/template/insurance_form.html')

    return render(request,'frenchise_dashboard/template/insurance_form.html')


@csrf_exempt
@login_required
def apply_mf(request):
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
        createloan = Mutual_Fund.objects.create(user=users,clientName=name,type=type,PAN=pan,number=number,amount=amount,email=emails,creation=formatted_date)
        
        return render(request,'frenchise_dashboard/template/mf_form.html')

    return render(request,'frenchise_dashboard/template/mf_form.html')


@csrf_exempt
@login_required
def apply_da(request):
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
        createloan = Demat_Account.objects.create(user=users,clientName=name,type=type,PAN=pan,number=number,amount=amount,email=emails,creation=formatted_date)
        
        return render(request,'frenchise_dashboard/template/da_form.html')

    return render(request,'frenchise_dashboard/template/da_form.html')

#Employee overview 
@csrf_exempt
@login_required
def employee_overview_view(request):
    if request.method == 'GET':
        loginUser = request.user
        # fromdate = str(request.POST.get('from'))
        # todate = str(request.POST.get('to'))
        # print([fromdate,todate])
        employedata = frenchise_employee_register_model.objects.filter(user=loginUser)

        
        print(employedata)
        if employedata:
            # if loginUser.username:
            #     employeedet = employedata.filter(username=loginUser.username)
            #     print("employeedata", employeedet)    

            emp_data = []
            for i in employedata:
                loanuser = User.objects.get(username=i.username)
                loandata = Loan.objects.filter(user=loanuser)
                loandatacompleted = Loan.objects.filter(user=loanuser,status='Completed')
                Insurancedata = Insurance.objects.filter(user=loanuser)
                Insurancedatacompleted = Insurance.objects.filter(user=loanuser,status='Completed')
                Mutualdata = Mutual_Fund.objects.filter(user=loanuser)
                Mutualdatacompleted = Mutual_Fund.objects.filter(user=loanuser,status='Completed')
                Dematdata = Demat_Account.objects.filter(user=loanuser)
                Dematdatacompleted = Demat_Account.objects.filter(user=loanuser,status='Completed')
                total_sale = loandata.count()+Insurancedata.count()+Mutualdata.count()+Dematdata.count()
                print("---------")
                print(loandata)
                data_emp = {
                    'Name':i.name,
                    'id':i.id,
                    'email':i.email,
                    'username':i.username,
                    'total_sale':total_sale,
                    'total_loan':loandata.count(),
                    'total_loan_completed':loandatacompleted.count(),
                    'total_insurance':Insurancedata.count(),
                    'total_insurance_completed':Insurancedatacompleted.count(),
                    'total_mutual':Mutualdata.count(),
                    'total_mutual_completed':Mutualdatacompleted.count(),
                    'total_demat':Dematdata.count(),
                    'total_demat_completed':Dematdatacompleted.count(),
                }
                emp_data.append(data_emp)

            print(emp_data)
            return render(request, 'frenchise_dashboard/template/emp_list.html',{'em_data':emp_data})
        else:
            return render(request,'frenchise/404.html')


    else:
        print("lgjjkhjgflkhjflkh")
        employedata = frenchise_employee_register_model.objects.filter(user = request.user)
        print("employedata" ,employedata)
        emp_data = []
        for i in employedata:
            loanuser = User.objects.get(username=i.username)
            loandata = Loan.objects.filter(user=loanuser)
            loandatacompleted = Loan.objects.filter(user=loanuser,status='Completed')
            Insurancedata = Insurance.objects.filter(user=loanuser)
            Insurancedatacompleted = Insurance.objects.filter(user=loanuser,status='Completed')
            Mutualdata = Mutual_Fund.objects.filter(user=loanuser)
            Mutualdatacompleted = Mutual_Fund.objects.filter(user=loanuser,status='Completed')
            Dematdata = Demat_Account.objects.filter(user=loanuser)
            Dematdatacompleted = Demat_Account.objects.filter(user=loanuser,status='Completed')
            total_sale = loandata.count()+Insurancedata.count()+Mutualdata.count()+Dematdata.count()
            print("---------")
            print("loandata", loandata)
            data_emp = {
                'Name':i.name,
                'id':i.id,
                'email':i.email,
                'username':i.username,
                'total_sale':total_sale,
                'total_loan':loandata.count(),
                'total_loan_completed':loandatacompleted.count(),
                'total_insurance':Insurancedata.count(),
                'total_insurance_completed':Insurancedatacompleted.count(),
                'total_mutual':Mutualdata.count(),
                'total_mutual_completed':Mutualdatacompleted.count(),
                'total_demat':Dematdata.count(),
                'total_demat_completed':Dematdatacompleted.count(),
            }
            emp_data.append(data_emp)

        print("empdata", emp_data)
        return render(request, 'frenchise_dashboard/template/emp_list.html',{'emp_data':emp_data})
    # return render(request, 'frenchise/employee_overview.html')

# Admin Overview frenchise and employee data
@csrf_exempt
@login_required
def frenchise_overview_view(request):
    loginUser = request.user
    if loginUser.is_superuser:
        return render(request, 'frenchise/frenchise_overview.html')

@csrf_exempt
@login_required
def loan_data(request):
    loginUser = request.user
    if loginUser.is_superuser:
        loandata = Loan.objects.exclude(status='Completed')
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

        return render(request,'admin_dashboard/template/loan_data.html',{'loandata':appdata})

@login_required
def insurance_data(request):
    loginUser = request.user
    if loginUser.is_superuser:
        Insurancedata = Insurance.objects.exclude(status='Completed')
        appdata = []
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

        return render(request,'admin_dashboard/template/insurance_data.html',{'loandata':appdata})

def demat_data(request):
    loginUser = request.user
    if loginUser.is_superuser:

        Dematdata = Demat_Account.objects.exclude(status='Completed')
        appdata = []
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
        return render(request,'admin_dashboard/template/demat_data.html',{'loandata':appdata})

def mutualfund_data(request):
    loginUser = request.user
    if loginUser.is_superuser:

        Mutualdata = Mutual_Fund.objects.exclude(status='Completed')

        appdata = []
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

        return render(request,'admin_dashboard/template/mutualfund_data.html',{'loandata':appdata})


@csrf_exempt
@login_required
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
            if statuss == 'Completed':
                getUserbyLoan = Loan.objects.get(id=ad_id)
                empUser = User.objects.get(username=getUserbyLoan.user)
                empProfile = frenchise_employee_register_model.objects.get(username=empUser)
                print(empProfile.user)                    
                franchiseUser = ProfileFrenchise.objects.get(user=empProfile.user)
                percentage = Decimal(franchiseUser.partner_at)

                # Perform operations with percentage
                amount = int(amount)
                amount1 = (percentage / 100) * amount

                # Print the results
                print(percentage)
                print(amount1)
                try:
                    revenue_record = Revenue.objects.get(user=franchiseUser.user)
                except Revenue.DoesNotExist:
                    revenue_record = None
                if revenue_record is not None:
                    # If the record exists, update the amount
                    revenue_record.amount += amount1
                    revenue_record.save()
                else:
                    # If the record doesn't exist, create a new one
                    revenue_record = Revenue(user=franchiseUser.user, amount=amount1)
                    revenue_record.save()

                print(franchiseUser)
                print(empUser)
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
            return render(request,'admin_dashboard/template/edit_loan.html',{'ad_data':dataEdit,'type':'Loan'})
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