from django.shortcuts import render
from .models import Person
from .forms import PhoneNumberForm

def search_phone_number(request):
    if request.method == "POST":
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            # Search for the phone number in the database
            persons = Person.objects.filter(phone_number=phone_number)
            if persons.exists():
                return render(request, 'search_results.html', {'persons': persons})
            else:
                return render(request, 'search_results.html', {'message': 'No match found.'})
    else:
        form = PhoneNumberForm()

    return render(request, 'search_form.html', {'form': form})
