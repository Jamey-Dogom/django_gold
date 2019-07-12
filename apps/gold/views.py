from django.shortcuts import render, HttpResponse, redirect
import random, datetime



def index(request):
    if not request.session.get('msg'):
        request.session['msg'] = [] # needs to be a list
    if not request.session.get('gold'):
        request.session['gold'] = 0
    if not request.session.get('fontcolor'):
        request.session['fontcolor'] = "green"
    return render(request, "gold/index.html")

def process_money(request):
    user_guess = request.POST['building']
    request.session['fontcolor'] = "green"
    
    if user_guess == 'farm':
        now = datetime.datetime.now()
        rand = random.randint(10, 20) 
        msg = "<p class = 'act' style = 'color: {}'>Earned {} golds from the {}! ({})<p>".format(request.session['fontcolor'],rand, user_guess, now.strftime("%Y-%m-%d %H:%M"))
        request.session['gold'] += rand
    if user_guess == 'cave':
        now = datetime.datetime.now()
        rand = random.randint(5, 10) 
        msg = "<p class = 'act' style = 'color: {}'>Earned {} golds from the {}! ({})<p>".format(request.session['fontcolor'],rand, user_guess, now.strftime("%Y-%m-%d %H:%M"))
        request.session['gold'] += rand
    if user_guess == 'house':
        now = datetime.datetime.now()
        rand = random.randint(2, 5) 
        msg = "<p class = 'act' style = 'color: {}'>Earned {} golds from the {}! ({})<p>".format(request.session['fontcolor'],rand, user_guess, now.strftime("%Y-%m-%d %H:%M"))
        request.session['gold'] += rand 
    if user_guess == 'casino':
        now = datetime.datetime.now()
        rand = random.randint(-50, 50) 
        if rand < 0:
            request.session['fontcolor'] = "red"
        msg = "<p class = 'act' style = 'color: {}'>Earned {} golds from the {}! ({})<p>".format(request.session['fontcolor'],rand, user_guess, now.strftime("%Y-%m-%d %H:%M"))
        request.session['gold'] += rand
        
        
    request.session['msg'].append(msg)
    return redirect('/')

def reset(request):
    request.session['gold'] = 0
    request.session['msg'] = []
    return render(request, "gold/index.html")
