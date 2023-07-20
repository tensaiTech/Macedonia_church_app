from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Member
from .forms import MemberForm
# Create your views here.
def index(request):
    return render(request, 'members/index.html', {
        'members': Member.objects.all()
    })

def view_member(request, id):
    member = Member.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
  if request.method == 'POST':
    form = MemberForm(request.POST)
    if form.is_valid():
        new_full_name = form.cleaned_data['full_name']
        new_gender = form.cleaned_data['gender']
        new_phone = form.cleaned_data['phone']
        new_email = form.cleaned_data['email']
        new_date_of_birth = form.cleaned_data['date_of_birth']
        new_place_of_birth = form.cleaned_data['place_of_birth']
        new_hometown = form.cleaned_data['hometown']
        new_occupation = form.cleaned_data['occupation']
        new_educational_background = form.cleaned_data['educational_background']
        new_house_number = form.cleaned_data['house_number']
        new_residental_area = form.cleaned_data['residental_area']
        new_residental_street = form.cleaned_data['residental_street']
        new_father_name = form.cleaned_data['father_name']
        new_father_hometown = form.cleaned_data['father_hometown']
        new_mother_name = form.cleaned_data['mother_name']
        new_mother_hometown = form.cleaned_data['mother_hometown']
        new_former_assembly = form.cleaned_data['former_assembly']
        new_former_district = form.cleaned_data['former_district']
        new_former_region_of_district_assembly = form.cleaned_data['former_region_of_district_assembly']
        new_place_of_baptism = form.cleaned_data['place_of_baptism']
        new_baptismal_officiating_minister = form.cleaned_data['baptismal_officiating_minister']
        new_zone = form.cleaned_data['zone']
        new_marital_status = form.cleaned_data['marital_status']
        new_marital_officiating_minister = form.cleaned_data['marital_officiating_minister']
        new_place_of_marriage = form.cleaned_data['place_of_marriage']
        new_year_of_marriage_registered = form.cleaned_data['year_of_marriage_registered']
        new_name_of_partner = form.cleaned_data['name_of_partner']
        new_name_of_denomination_of_partner = form.cleaned_data['name_of_denomination_of_partner']
        new_partner_hometown = form.cleaned_data['partner_hometown']


        new_member = Member(
        full_name=new_full_name,
        phone=new_phone,
        gender=new_gender,
        email=new_email,
        date_of_birth = new_date_of_birth,
        place_of_birth = new_place_of_birth,
        hometown = new_hometown,
        occupation = new_occupation,
        educational_background = new_educational_background,
        house_number = new_house_number,
        residental_area = new_residental_area,
        residental_street = new_residental_street,
        father_name = new_father_name,
        father_hometown = new_father_hometown,
        mother_name = new_mother_name,
        mother_hometown = new_mother_hometown,
        former_assembly = new_former_assembly,
        former_district = new_former_district,
        former_region_of_district_assembly = new_former_region_of_district_assembly,
        place_of_baptism = new_place_of_baptism,
        baptismal_officiating_minister = new_baptismal_officiating_minister,
        zone = new_zone,
        marital_status = new_marital_status,
        marital_officiating_minister = new_marital_officiating_minister,
        place_of_marriage = new_place_of_marriage,
        year_of_marriage_registered = new_year_of_marriage_registered,
        name_of_partner = new_name_of_partner,
        name_of_denomination_of_partner = new_name_of_denomination_of_partner,
        partner_hometown = new_partner_hometown,
      )
        new_member.save()
        return render(request, 'members/add.html', {
        'form': MemberForm(),
        'success': True
      })
  else:
    form = MemberForm()
  return render(request, 'members/add.html', {
    'form': MemberForm()
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