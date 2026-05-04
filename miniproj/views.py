from django.shortcuts import render,redirect

def login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        theme = request.POST.get('theme')
        #session
        request.session["username"] = username
        #cookie
        response = redirect('dashboard')
        response.set_cookie("theme", theme)
        return response
    return render(request,'login.html')

def dashboard(request):
    username = request.session.get("username")
    theme = request.COOKIES.get("theme")
    return render(request, 'dashboard.html', {
        "username": username,
        "theme": theme
    })

def logout(request):
    request.session.flush()  # remove all session data
    response = redirect('login')
    response.delete_cookie("theme")  # remove cookie
    return response
    




