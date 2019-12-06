from django.shortcuts import render, redirect
from .models import *
from .forms import FeedbackForm

# Create your views here.

def list(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'feedbacklist.html', {'feedbacks':feedbacks})

def create(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/feedback/list')
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form}) #이런식으로 데이터 넘겨주면 되지 않을까. 데이터는 pymysql 로 logmanager 에 연결하고.

def edit(request, id):
    fb = Feedback.objects.get(pk = id)
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance = fb)
        if form.is_valid():
            form.save()
        return redirect('/feedback/list')
    else:
        form = FeedbackForm(instance=fb)

    return render(request, 'feedback.html', {'form':form})