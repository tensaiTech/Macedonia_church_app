from django.db import models

# Create your models here.
class Member(models.Model):
    full_name = models.CharField(max_length=200)
    gender = models.IntegerField(choices=((0, 'Male'), (1, 'Female')))
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=200, null=True)
    hometown = models.CharField(max_length=200, null=True)
    occupation = models.CharField(max_length=200, null=True)
    educational_background = models.CharField(max_length=200, null=True)
    house_number = models.CharField(max_length=20, null=True)
    residental_area = models.CharField(max_length=200, null=True)
    residental_street = models.CharField(max_length=200, null=True)
    father_name = models.CharField(max_length=200, null=True)
    father_hometown = models.CharField(max_length=200, null=True)
    mother_name = models.CharField(max_length=200, null=True)
    mother_hometown = models.CharField(max_length=200, null=True)
    former_assembly = models.CharField(max_length=200, null=True)
    former_district = models.CharField(max_length=200, null=True)
    former_region_of_district_assembly = models.CharField(
        max_length=200, null=True)
    place_of_baptism = models.CharField(max_length=200, null=True)
    baptismal_officiating_minister = models.CharField(
        max_length=200, null=True)
    zone = models.IntegerField()
    marital_status = models.IntegerField(
        choices=((0, "Single"), (1, "Married")))
    marital_officiating_minister = models.CharField(max_length=200, null=True)
    place_of_marriage = models.CharField(max_length=200, null=True)
    year_of_marriage_registered = models.DateField()
    name_of_partner = models.CharField(max_length=200, null=True)
    name_of_denomination_of_partner = models.CharField(
        max_length=200, null=True)
    partner_hometown = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name