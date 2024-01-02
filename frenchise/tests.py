from django.conf import UserSettingsHolder
from django.contrib.auth.models import User
from django.shortcuts import render
from django.test import TestCase
from companystaff.models import Demat_Account, Insurance, Loan, Mutual_Fund
from django.utils import timezone
from datetime import datetime
from frenchise.models import frenchise_employee_register_model

# Create your tests here.


    
def get_emp_data(request):
    if request.method == 'POST':
        loginUser = request.user
        fromdate = str(request.POST.get('from'))
        todate = str(request.POST.get('to'))
        print([fromdate,todate])
        employedata = frenchise_employee_register_model.objects.filter(user=loginUser)

        
        print(employedata)
        if employedata:
            # if loginUser.username:
            #     employeedet = employedata.filter(username=loginUser.username)
            #     print("employeedata", employeedet)    

            emp_data = []
            for i in employedata:
                loanuser = User.objects.get(username=i.username)
                loandata = Loan.objects.filter(user=loanuser,creation__range=(fromdate,todate))
                loandatacompleted = Loan.objects.filter(user=loanuser,status='Completed',creation__range=(fromdate,todate))
                Insurancedata = Insurance.objects.filter(user=loanuser,creation__range=(fromdate,todate))
                Insurancedatacompleted = Insurance.objects.filter(user=loanuser,status='Completed',creation__range=(fromdate,todate))
                Mutualdata = Mutual_Fund.objects.filter(user=loanuser,creation__range=(fromdate,todate))
                Mutualdatacompleted = Mutual_Fund.objects.filter(user=loanuser,status='Completed',creation__range=(fromdate,todate))
                Dematdata = Demat_Account.objects.filter(user=loanuser,creation__range=(fromdate,todate))
                Dematdatacompleted = Demat_Account.objects.filter(user=loanuser,status='Completed',creation__range=(fromdate,todate))
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