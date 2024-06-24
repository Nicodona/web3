from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.contrib import messages
import random

# Create your views here.
def vote(request):
    blue_candidate = get_object_or_404(Candidates, pk="blue")
    yellow_candidate = get_object_or_404(Candidates, pk="yellow")
    white_candidate = get_object_or_404(Candidates, pk="white")

    context = {
        'blue_candidate': blue_candidate,
        'yellow_candidate': yellow_candidate,
        'white_candidate': white_candidate,

    }

    if request.method == 'POST':
        name = request.POST['name']
        figerprint = request.POST['key']
        print('see',figerprint, name)
        poll_harsh = random.randint(pow(10, 9 -1), (pow(10, 9) -1))

        while Poll.objects.filter(poll_harsh=poll_harsh).exists():
             poll_harsh = random.randint(pow(10, 9 -1), (pow(10, 9) -1))

        
        if Poll.objects.filter(voter=figerprint).exists():
            context['message'] = "vote already exist"
            return render(request, 'vote.html', context)

        else:
            if Registration.objects.filter(figerprint=figerprint).exists():
                voter= Registration.objects.get(pk=figerprint)
                choice = Candidates.objects.get(pk=name)
                new_vote = Poll(voter=voter, choice=choice, poll_harsh=poll_harsh )
                can = Candidates.objects.get(pk=name)
                can.votes += 1
                new_vote.save()
                can.save()
                context['message'] = "vote data saved"
                return render(request, 'vote.html', context)

        context['message'] = "We cant authenticate you, seek support"
        return render(request, 'vote.html', context)

    else:
      return render(request, 'vote.html', context)






def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        Nid = request.POST['Nid']
        center = request.POST['center']
        # fingerprint id 
        Rid = str(random.randint(pow(10, 7 -1), (pow(10,  7) -1)))

        while Registration.objects.filter(Rid = Rid).exists():
            Rid = str(random.randint(pow(10, 7), (pow(10, 7) -1 )))


        if Registration.objects.filter(Nid=Nid).exists() or Registration.objects.filter(name=name).exists():
            messages.info(request, "account exist user already registered")
        else:
            new_account = Registration(name=name, Nid=Nid, center=center, Rid=Rid, figerprint=Rid)
            new_account.save()
            messages.info(request, f'account created with Id {Rid},')

        return render(request, 'register.html', {messages:messages})
            
    else:
        return render(request, 'register.html')
    

