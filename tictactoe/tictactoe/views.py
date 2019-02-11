from django.shortcuts import render, redirect
from django.http import HttpResponse

def welcome(request):
    if request.user.is_authenticated:
        return redirect('player_home')
    else:
        return render(request, 'tictactoe/welcome.html')
