from django.http import HttpResponse
from django.shortcuts import render, redirect
from .service.UserService import UserService


def test_ors(request):
    return HttpResponse("Hello Django ors program is running")


def welcome(request):
    return render(request, 'welcome.html')


def user_signup(request):
    if request.method == "POST":
        params = {}
        params['firstName'] = request.POST.get('firstName')
        params['lastName'] = request.POST.get('lastName')
        params['loginId'] = request.POST.get('loginId')
        params['password'] = request.POST.get('password')
        params['dob'] = request.POST.get('dob')
        params['address'] = request.POST.get('address')
        service = UserService()
        service.add(params)
    return render(request, 'registration.html')


def user_signin(request):
    message = ''
    if request.method == "POST":

        if request.POST.get('operation') == 'signIn':
            loginId = request.POST.get('loginId')
            password = request.POST.get('password')
            service = UserService()
            user_data = service.auth(loginId, password)
            if len(user_data) != 0:
                request.session['firstName'] = user_data[0].get('firstName')
                return redirect('/ors/welcome')
            else:
                message = 'login & password is invalid'

        if request.POST.get('operation') == 'signUp':
            return redirect("/ors/signup/")
    return render(request, 'login.html', {'message': message})


def user_logout(request):
    request.session['firstName'] = None
    return redirect('/ors/signin/')


def test_list(request):
    list = [
        {"id": 1, "firstName": "abc", "lastName": "aaa", "email": "abc@gmail.com", "password": "12345"},
        {"id": 2, "firstName": "xyz", "lastName": "aaa", "email": "abc@gmail.com", "password": "12345"},
        {"id": 3, "firstName": "pqr", "lastName": "aaa", "email": "abc@gmail.com", "password": "12345"}
    ]
    return render(request, "testlist.html", {"list": list})


def user_list(request):
    params = {}
    params['pageNo'] = 1
    params['pageSize'] = 5

    if request.method == "POST":
        if request.POST['operation'] == "next":
            params['pageNo'] = int(request.POST['pageNo'])
            params['pageNo'] += 1
        if request.POST['operation'] == "previous":
            params['pageNo'] = int(request.POST['pageNo'])
            params['pageNo'] -= 1
        if request.POST['operation'] == "search":
            params['firstName'] = request.POST['firstName']

    service = UserService()
    list = service.search(params)
    index = (params['pageNo'] - 1) * 5
    return render(request, "userlist.html", {"list": list, 'pageNo': params['pageNo'], 'index': index})


def delete_user(request, id=0):
    service = UserService()
    service.delete(id)
    return redirect("/ors/list/")


def user_save(request, id=0):
    message = ''
    data = {}
    service = UserService()

    if request.method == "GET" and id > 0:
        user_data = service.get(id)
        user_data[0]['dob'] = user_data[0]['dob'].strftime('%Y-%m-%d')
        data = user_data[0]

    if request.method == "POST":
        params = {}
        params['firstName'] = request.POST.get('firstName')
        params['lastName'] = request.POST.get('lastName')
        params['loginId'] = request.POST.get('loginId')
        params['password'] = request.POST.get('password')
        params['dob'] = request.POST.get('dob')
        params['address'] = request.POST.get('address')
        if request.POST['operation'] == "save":
            service.add(params)
            message = 'User Added Successfully'
        if request.POST['operation'] == "update":
            params['id'] = request.POST.get('id')
            service.update(params)
            message = 'User Updated Successfully'

    return render(request, 'user.html', {'message': message, 'form': data})
