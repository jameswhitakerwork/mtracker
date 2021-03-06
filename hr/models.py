from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from jsignature.mixins import JSignatureFieldsMixin

from django.utils import timezone
import datetime
from datetime import timedelta


# Create your models here.


class Shirt_Size(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.name


class Staff_Type(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.name


class Warden_Zone(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.name


class Action(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.name


class Grade(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.name


class Contract_Type(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.name

class Position_Status(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Position Statuses'


class Duty_Station(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=32, unique=True)
    desc = models.CharField(max_length=256, blank=True)

    def __unicode__(self):
        if self.desc:
            return self.name + ' (' + self.desc + ')'
        else:
            return self.name




class Gender(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.name


class Mission(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.name


class Office(models.Model):
    name = name = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.name


class JSignatureModel(JSignatureFieldsMixin):
    name = models.CharField(max_length=128, blank=True, null=True)


class Staff(models.Model):
    """
    Contains information about a particular person.
    Optionally matches up to a website user.
    Contains email, address, contact details.
    """

    user = models.OneToOneField(User, blank=True, null=True)
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    personnel_no = models.CharField(max_length=16)
    entry_on_duty = models.DateField(blank=True, null=True)
    shirt_size = models.ForeignKey(Shirt_Size, blank=True, null=True)
    no_of_dependants = models.IntegerField(blank=True, null=True)
    staff_type = models.ForeignKey(Staff_Type, blank=True, null=True)
    file = models.FileField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)
    gender = models.ForeignKey(Gender, blank=True, null=True)
    nationality = CountryField()
    personal_email = models.EmailField(blank=True, null=True)
    home_phone = models.IntegerField(blank=True, null=True)
    mobile_phone = models.IntegerField(blank=True, null=True)
    home_phone_at_station = models.IntegerField(blank=True, null=True)
    mobile_phone_at_station = models.IntegerField(blank=True, null=True)
    address_1 = models.CharField(max_length=64, blank=True, null=True)
    address_2 = models.CharField(max_length=64, blank=True, null=True)
    address_3 = models.CharField(max_length=64, blank=True, null=True)
    address_country = CountryField()
    zip_code = models.CharField(max_length=8, blank=True, null=True)
    un_warden_zone = models.ForeignKey(Warden_Zone, blank=True, null=True)

    class Meta:
        verbose_name_plural = '   STAFF'
        unique_together = ('first_name', 'last_name')
        permissions = (
            ('asset_access', 'Asset Access'),
            ('procurement_access', 'Procurement Access'),
            ('hr_access', 'HR Access'),
        )

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name.upper()

    def get_absolute_url(self):
        return '/hr/staff/%i/' % self.id

    def save(self, *args, **kwargs):
        # change name to Lower UPPER
        self.last_name = self.last_name.upper()
        n = self.first_name
        print 'name is ' + n
        n1 = n[0]
        n2 = n[1:]
        n1 = n1.upper()
        n2 = n2.lower()
        self.first_name = n1 + n2
        print 'name has been changed to ' + self.first_name
        super(Staff, self).save(*args, **kwargs)

    def active_contract(self):
        try:
            contracts = Contract.objects.all().filter(staff=self)
        except:
            return None
        if contracts:
            for c in contracts:
                t = timezone.now().date()
                if c.start_date <= t <= c.end_date:
                    return True
        return False

    active_contract.boolean = True

    def get_contract(self):
        try:
            contracts = Contract.objects.filter(staff=self)
        except:
            return None
        if contracts:
            t = timezone.now().date()
            for c in contracts:
                if c.start_date <= t <= c.end_date:
                    return c
        return False

    def get_position(self):
        try:
            p = Position.objects.filter(contract__staff=self)[0]
            return p
        except:
            return None


class Position(models.Model):
    """
    Position details such as grade, WBS, status
    """
    # staff = models.ForeignKey(Staff)
    position_code = models.CharField(max_length=16, blank=True, null=True)
    duty_station = models.ForeignKey(Office)
    program = models.ForeignKey(Program, blank=True, null=True)
    title = models.CharField(max_length=64)
    reports_to = models.ForeignKey('Position', blank=True, null=True)
    tor = models.FileField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    expected_need_until = models.DateField(blank=True, null=True)
    expected_monthly_rate = models.IntegerField(blank=True, null=True)
    wbs = models.CharField(max_length=32, blank=True, null=True)
    notes = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        verbose_name_plural = '  POSITIONS'

    def __unicode__(self):
        return self.title

    def active_contract(self):
        c = Contract.objects.get(position=self)
        if c:
            t = timezone.now().date()
            return c.start_date <= t <= c.end_date
        else:
            return False

    active_contract.boolean = True

    def get_expected_rate(self):
        try:
            r = getattr(self, 'expected_monthly_rate')
        except:
            r = 0
        return "{:}".format(r)


class Contract(models.Model):
    """
    Contract details with dates, rates and details.
    Also includes checklist for onboarding.
    A contract is matched to a particular staff member
    and a particular position.
    """
    position = models.ForeignKey(Position)
    staff = models.ForeignKey(Staff)
    contract_code = models.CharField(max_length=16, blank=True, null=True)
    contract_type = models.ForeignKey(Contract_Type, blank=True, null=True)
    file = models.FileField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField()
    grade = models.ForeignKey(Grade, blank=True, null=True)
    monthly_rate = models.IntegerField(blank=True, null=True)
    total_cost = models.IntegerField(blank=True, null=True)
    renew_after_expires = models.BooleanField()
    personal_history = models.FileField(blank=True, null=True)
    medical_clearance = models.FileField(blank=True, null=True)
    policy_and_conduct = models.FileField(blank=True, null=True)
    iom_email = models.BooleanField(default=False)
    basic_field_security = models.FileField(blank=True, null=True)
    advanced_field_security = models.FileField(blank=True, null=True)
    travel_profile = models.FileField(blank=True, null=True)
    proof_of_life = models.FileField(blank=True, null=True)
    ses_initiated = models.BooleanField(default=False)
    duty_station_orientation = models.BooleanField(default=False)
    photo = models.FileField(blank=True, null=True)
    iom_un_id = models.BooleanField(default=False)
    signature = models.ForeignKey(JSignatureModel, blank=True, null=True)

    class Meta:
        verbose_name_plural = ' CONTRACTS'

    def __unicode__(self):
        return "Contract " + self.contract_code

    def tasks_progress(self):
        # returns progress out of 100
        # used for progress bars
        percent = 50  # come back to calculate percentage progress
        return percent

    def tasks_completed(self):
        # returns True if all tasks completed
        return self.tasks_progress() >= 99

    def get_position(self):
        return self.position

    def is_active(self):
        t = timezone.now().date()
        return self.start_date <= t <= self.end_date

    def get_monthly_rate(self):
        r = getattr(self, 'monthly_rate')
        return "{:,}".format(r)

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError({
                'end_date': _('Contract end date must be after the start date')
            })

    def ending_soon(self):
        t = timezone.now().date()
        d = self.end_date
        renew = getattr(self, 'renew_after_expires')
        ending_soon = t > d - timedelta(days=30)
        contracts = Contract.objects.filter(staff=self.staff)
        next_contract = False
        for c in contracts:
            if t < c.start_date:
                next_contract = True
        return ending_soon and (not next_contract) and renew

