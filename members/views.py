from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Member
from .forms import MemberForm


# Create your views here.
@login_required
def index(request):
    members = Member.objects.all()
    males = Member.objects.filter(gender='M')
    females = Member.objects.filter(gender='F')
    married = Member.objects.filter(marital_status='R')
    context = {
        'members': members,
        'males': males,
        'females': females,
        'married': married
    }
    return render(request, 'members/index.html', context)


def view_member(request, id):
    member = Member.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))


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


def delete(request, id):
    if request.method == 'POST':
        member = Member.objects.get(pk=id)
        member.delete()
    return HttpResponseRedirect(reverse('index'))
