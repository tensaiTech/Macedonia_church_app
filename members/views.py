from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Member
from .forms import MemberForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from datetime import date, timedelta


# Create your views here.
@login_required
def index(request):
    members = Member.objects.all()
    males = Member.objects.filter(gender='M')
    females = Member.objects.filter(gender='F')
    married = Member.objects.filter(marital_status='R')
    current_months_birthdays = get_members_with_birthdays_in_current_month()
    context = {
        'members': members,
        'males': males,
        'females': females,
        'married': married,
        'current_months_birthdays': current_months_birthdays
    }
    return render(request, 'members/index.html', context)

@login_required
def view_member(request, id):
    member = Member.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

@login_required
def add(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = MemberForm()
    return render(request, 'members/add.html', {
        'form': form
    })

@login_required
def edit(request, id):
    if request.method == 'POST':
        member = Member.objects.get(pk=id)
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return render(request, 'members/edit.html', {
                'form': form,
                'success': True
            })
    else:
        member = Member.objects.get(pk=id)
        form = MemberForm(instance=member)
    return render(request, 'members/edit.html', {
        'form': form
    })

@login_required
def delete(request, id):
    if request.method == 'POST':
        member = Member.objects.get(pk=id)
        member.delete()
    return HttpResponseRedirect(reverse('index'))


def logout_view(request):
    logout(request)
    return redirect('/accounts/login')

def get_members_with_birthdays_in_current_month():
    today = date.today()
    # end_date = today + timedelta(days)

    # Extract month and day from today's date
    current_month = today.month
    current_day = today.day

    # Extract month and day from the end_date
    # end_month = end_date.month
    # end_day = end_date.day

    filtered_Members = Member.objects.filter(
            date_of_birth__month=current_month,
            date_of_birth__day__gte=current_day,            
        )
    return filtered_Members