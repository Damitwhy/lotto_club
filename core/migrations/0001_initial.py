# Generated by Django 5.1.3 on 2024-11-27 01:44

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='LotteryDraw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('draw_type', models.CharField(choices=[('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Both', 'Both')], default='Both', max_length=10)),
                ('lottery_type', models.CharField(choices=[('UK Lottery', 'UK Lottery'), ('EuroMillions', 'EuroMillions')], default='EuroMillions', max_length=20)),
                ('line1_numbers', models.CharField(max_length=50)),
                ('line2_numbers', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone_number', models.CharField(blank=True, help_text='Enter the phone number', max_length=15, null=True, verbose_name='Phone Number')),
                ('address', models.TextField(blank=True, null=True)),
                ('postcode', models.CharField(blank=True, max_length=10, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('participates_in_draws', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Syndicate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='managed_syndicates', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(related_name='syndicate_memberships', through='core.Membership', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='membership',
            name='syndicate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.syndicate'),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('postcode', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, help_text='Enter the phone number', max_length=15, null=True, verbose_name='Phone Number')),
                ('date_of_birth', models.DateField()),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('syndicate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members_in_syndicate', to='core.syndicate')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='syndicates',
            field=models.ManyToManyField(through='core.Membership', to='core.syndicate'),
        ),
        migrations.CreateModel(
            name='SyndicateAgreement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agreement_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('syndicate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.syndicate')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_number', models.CharField(max_length=50)),
                ('purchase_date', models.DateTimeField(auto_now_add=True)),
                ('draw', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.lotterydraw')),
                ('syndicate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.syndicate')),
            ],
        ),
    ]