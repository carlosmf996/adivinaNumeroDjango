from django.shortcuts import render
import random

# Create your views here.

def home(request):
        return render(request, 'adivina/home.html')
            
def guess(request):         
    random_number = random.randint(1,10)
    guess = int(request.POST['guess'])

    if guess == random_number:
       message = 'VAYA TIO WENO'

    if guess > random_number:
        message = 'Un poquito pabajo'
    if guess < random_number:
        message = 'Un poquito parriba'

    return render(request, 'adivina/guess.html', {'message': message})