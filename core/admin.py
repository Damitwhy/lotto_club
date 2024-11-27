from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Syndicate, SyndicateAgreement, Member, Membership, Ticket, LotteryDraw

User = get_user_model()

# Unregister the User model if it is already registered
if admin.site.is_registered(User):
    admin.site.unregister(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'address', 'postcode', 'date_of_birth')
    search_fields = ('username', 'email', 'phone_number')

@admin.register(Syndicate)
class SyndicateAdmin(admin.ModelAdmin):
    list_display = ('name', 'manager')
    search_fields = ('name', 'manager__username')

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'address', 'postcode', 'date_of_birth', 'syndicate')
    search_fields = ('name', 'email', 'phone_number')

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'syndicate', 'percentage', 'participates_in_draws')
    search_fields = ('user__username', 'syndicate__name')

@admin.register(SyndicateAgreement)
class SyndicateAgreementAdmin(admin.ModelAdmin):
    list_display = ('syndicate', 'created_at')
    search_fields = ('syndicate__name',)

@admin.register(LotteryDraw)
class LotteryDrawAdmin(admin.ModelAdmin):
    list_display = ('date', 'draw_type', 'lottery_type', 'line1_numbers', 'line2_numbers')
    search_fields = ('date', 'draw_type', 'lottery_type')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('draw', 'syndicate', 'ticket_number', 'purchase_date')
    search_fields = ('draw__date', 'syndicate__name', 'ticket_number')

