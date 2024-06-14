from django.shortcuts import render

def index(request):
    # Add any data or logic you need to pass to the template here
    context = {'message': 'Welcome to your car dealership website!'}
    return render(request, 'front/car_dealer_front/index.html', context)
