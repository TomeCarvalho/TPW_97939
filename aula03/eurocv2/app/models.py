from django.db import models


class Name(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)


class Address(models.Model):
    street = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


class Phone(models.Model):
    country_prefix = models.CharField(max_length=10)
    number = models.CharField(max_length=20)


class Fax(models.Model):
    country_prefix = models.CharField(max_length=10)
    number = models.CharField(max_length=20)


class Contacts(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    fax = models.ForeignKey(Fax, on_delete=models.CASCADE)
    # emails


class PersonalInfo(models.Model):
    name = models.ForeignKey(Name, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    nationality = models.CharField(max_length=50)
    birthdate = models.DateField()
    gender = models.CharField(max_length=20)


class Email(models.Model):
    type = models.CharField(max_length=50)
    value = models.EmailField(max_length=100, primary_key=True)
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)


class EmployerContact(models.Model):
    website = models.URLField()
    email = models.EmailField(max_length=100)


class Employer(models.Model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    contact = models.ForeignKey(EmployerContact, on_delete=models.CASCADE)


class CV(models.Model):
    photo = models.ImageField(upload_to='photos')
    desired_employ = models.CharField(max_length=100)
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)


class Position(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    occupation = models.CharField(max_length=50)
    # activities
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)  # workexperience is redundant


class Activity(models.Model):
    designation = models.CharField(max_length=50)
    time = models.CharField(max_length=20)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    business_sector = models.CharField(max_length=100)
