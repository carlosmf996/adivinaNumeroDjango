from django.shortcuts import render
import random

# Create your views here.

def home(request):
        return render(request, 'adivina/home.html')
            
def guess(request):         
    random_number = random.randint(1,100)
    user_guess = int(request.POST['guess'])

    if user_guess == random_number:
       message = 'Vaya tio weno'

    if user_guess > random_number:
        message = 'Un poquito pabajo'
    else:
        message = 'Un poquito parriba'

    return render(request, 'adivina/guess.html', {'message': message})