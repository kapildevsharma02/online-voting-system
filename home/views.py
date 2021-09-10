from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import VotingList, Results
from home.form import VForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

@login_required
def homepage(request):
    if request.method == "POST":
        form = VForm(request.POST or None)
        if form.is_valid():
            # instance = form.save(commit=False)
            # instance.manager = request.user
            # instance.save()    
            voted = form.cleaned_data['vote']
            VotingList.objects.create(manager=request.user, vote= voted, status=True)
            # v = Results.objects.filter(candidate=voted)
            # num = v.votes
            # Results.objects.filter(candidate=voted).update(votes= num + 1)
        return render(request, 'success.html')

    else:            
        v = VotingList.objects.filter(manager=request.user).count()
        if v == 1:
            return render(request, 'success.html')
        else:
            return render(request, 'home.html', {'form':VForm})

@login_required
def result(request):
    if request.user.is_superuser:
        v1 = VotingList.objects.filter(vote="Candidate 1").count()
        v2 = VotingList.objects.filter(vote="Candidate 2").count()
        v3 = VotingList.objects.filter(vote="Candidate 3").count()
        Results.objects.filter(candidate="Candidate 1").update(votes= v1)
        Results.objects.filter(candidate="Candidate 2").update(votes= v2)
        Results.objects.filter(candidate="Candidate 3").update(votes= v3)
        res = Results.objects.order_by("-votes")
        return render(request, 'result.html', {'results' : res})
    else:
        return render(request, 'denied.html')

@login_required
def clear(request):
    if request.user.is_superuser:
        votes = VotingList.objects.all()
        votes.delete()
        return redirect('result') 
    else:
        return render(request, 'denied.html')
