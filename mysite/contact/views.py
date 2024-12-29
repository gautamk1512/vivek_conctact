from django.shortcuts import render
from django.contrib import messages
from .models import Contact

# Create your views here.
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        
        if name and phone:
            contact = Contact(name=name, phone=phone)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
        else:
            messages.error(request, "Please fill in all fields.")

    return render(request, 'contact.html')
