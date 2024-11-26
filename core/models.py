from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.conf import settings


class User(AbstractUser): 
    pass


class Ticket(models.Model):
    draw = models.ForeignKey(LotteryDraw, on_delete=models.CASCADE)
    syndicate = models.ForeignKey(Syndicate, on_delete=models.CASCADE)
    ticket_number = models.CharField(max_length=50)


class LotteryDraw(models.Model):
    date = models.DateField()
    draw_type = models.CharField(max_length=10, choices=[('Tuesday', 'Tuesday'), ('Friday', 'Friday')])
    lottery_type = models.CharField(max_length=20, choices=[('UK Lottery', 'UK Lottery'), ('EuroMillions', 'EuroMillions')])
    line1_numbers = models.CharField(max_length=50)  # Store the first line of numbers as a comma-separated string
    line2_numbers = models.CharField(max_length=50)  # Store the second line of numbers as a comma-separated string


class SyndicateAgreement(models.Model):
    syndicate = models.OneToOneField(Syndicate, on_delete=models.CASCADE)
    agreement_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Membership(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    syndicate = models.ForeignKey(Syndicate, on_delete=models.CASCADE)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)


class Syndicate(models.Model):
    name = models.CharField(max_length=100)
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='managed_syndicates')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Membership')
