
def donkeymanish(request):
    from .views import returningdatamofsl
    dd = returningdatamofsl(request)
    # print('fff')
    # print(dd)
    return dd