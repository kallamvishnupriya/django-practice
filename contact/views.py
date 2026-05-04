from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('success')
    return render(request, 'contact/contact.html', {'form': form})


def success_view(request):
    return render(request, 'contact/success.html')