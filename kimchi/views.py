from django.shortcuts import render

def DisplayMypage(request):
    return render(request,  'kimchi/mypage.html', {'welcome_text':'kimchi status'})