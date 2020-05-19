from django.shortcuts import render


template = 'game/index.html'

def game(request):
    return render(request, template, {'range': range(9)})

# Web Sockets, Channels, AI Bot
