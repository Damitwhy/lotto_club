from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Phone Number', help_text='Enter the phone number')
    address = models.TextField(blank=True, null=True)
    postcode = models.CharField(max_length=10, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    syndicates = models.ManyToManyField('Syndicate', through='Membership')

class LotteryDraw(models.Model):
    date = models.DateField()
    draw_type = models.CharField(max_length=10, choices=[
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Both', 'Both')
    ], default='Both')
    lottery_type = models.CharField(max_length=20, choices=[
        ('UK Lottery', 'UK Lottery'),
        ('EuroMillions', 'EuroMillions')
    ], default='EuroMillions')
    line1_numbers = models.CharField(max_length=50)  # Store the first line of numbers as a comma-separated string
    line2_numbers = models.CharField(max_length=50)  # Store the second line of numbers as a comma-separated string

class Syndicate(models.Model):
    name = models.CharField(max_length=100)
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='managed_syndicates')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Membership', related_name='syndicate_memberships')

class Member(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    postcode = models.CharField(max_length=10)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Phone Number', help_text='Enter the phone number')
    date_of_birth = models.DateField()
    syndicate = models.ForeignKey(Syndicate, on_delete=models.CASCADE, related_name='members_in_syndicate')
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Membership(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    syndicate = models.ForeignKey(Syndicate, on_delete=models.CASCADE)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    participates_in_draws = models.BooleanField(default=True) # Indicate that the member participates in both draws
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.syndicate}"

class Ticket(models.Model):
    draw = models.ForeignKey(LotteryDraw, on_delete=models.CASCADE)
    syndicate = models.ForeignKey(Syndicate, on_delete=models.CASCADE)
    ticket_number = models.CharField(max_length=50)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ticket_number

class SyndicateAgreement(models.Model):
    syndicate = models.OneToOneField(Syndicate, on_delete=models.CASCADE)
    agreement_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Agreement for {self.syndicate.name}"