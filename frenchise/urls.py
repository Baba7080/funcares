from django.contrib import admin
from django.urls import path, include
from .views import *
from .tests import *
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .forms import LoginForm,  MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm




urlpatterns = [

    path('admin_dash', admindas, name='admin_dash'),
    path('emp_dash', empdas, name='emp_dash'),
    
    path('', index, name='home'),
    path('about/', about_view, name= 'about'),
    path('services/', Services_view, name= 'services'),
    path('blog/', blog_view, name= 'blog'),
    path('blog-details/', blog_details_view, name= 'blog_details'),
    path('contact/', contact_view, name= 'contact'),

    path('admin-frenchise-dashboard/', frenchise_dashboard_admin_view, name= 'admin_frenchise'),
    path('admin-employee-dashboard/', frenchise_employee_admin_view, name= 'admin_employee'),
    path('search-f/', frenchise_search_view, name= 'search_frenchise'),




    path('emp-details/<int:empid>/', edit_employee_dashboard_view, name= 'emp_details'),
    path('register/', frenchise_registration_view, name= 'register'),
    path('profile/', profile, name= 'profile'),

    path('dashboard/', dashboard, name= 'dashboard'),
    path('alldata/<int:frenchid>', all_frenchise_employe_view, name= 'alldata'),
    path('apply-loan/', apply_loan_view, name= 'apply_loan'),

    path('Employee-registration/', employee_view, name= 'emp_registration'),
    
    path('employee/', employee_view, name= 'employee'),
    path('confirmation/', frenchise_confirmation, name= 'confirmation'),

    path('frenchise-application/', frenchise_application_view, name= 'applyfrenchise'),
    # path('frenchise-application/', frenchise_apply_view, name= 'a_frenchise'),


    #Employee URLS
    path('emp-dashboard/', employee_dashboard_view, name= 'e_dashboard'),
    path('edit-emp-dashboard/', edit_employee_dashboard_view, name= 'edit_e_dashboard'),
    path('f-overview/', frenchise_overview_view, name= 'f_overview'),
    path('emp-overview/', employee_overview_view, name= 'e_overview'),
    path('emp-get-detail/', get_emp_data, name= 'emp_get_detail'),

    path('employee_data_chart/', employee_data_chart, name='employee_data_chart'),
    # path('employee_data_chart/', employee_data_chart, name='employee_data_chart'),

    



    #Authentication URLS
    path('accounts/login/',auth_views.LoginView.as_view(template_name='frenchise/login.html',authentication_form=LoginForm),name='login'),
    #  3-Logout
    path('logout/', auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    #Password change
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='frenchise/passwordchange.html',
        form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'),name='passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeView.as_view(template_name='frenchise/passwordchangedone.html'),name='passwordchangedone'),
    # 5-password reset
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='frenchise/password_reset.html',
        form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='frenchise/password_reset_done.html')
        ,name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='adminss/password_reset_confirm.html'
        ,form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='frenchise/password_reset_complete.html')
        ,name='password_reset_complete'),

    path('appllyloan',appllyloan,name='appllyloan'),
    path('loans',loan,name='loans'),
    path('appllyinsurance',apply_insurance,name='appllyinsurance'),
    path('applymf',apply_mf,name='applymf'),
    path('applyda',apply_da,name='applyda'),
    path('editfrenchise/<int:frenchid>',editfrenchise,name='editfrenchise'),
    path('editloan/<int:ad_id>/<str:ad_type>/', editsection, name='editloan')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
