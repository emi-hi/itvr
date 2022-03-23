# Generated by Django 4.0.1 on 2022-03-23 00:01

from django.db import migrations, models
import encrypted_fields.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IncomeVerification',
            fields=[
                ('create_timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('create_user', models.CharField(default='SYSTEM', max_length=130)),
                ('update_timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('update_user', models.CharField(max_length=130, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sin', encrypted_fields.fields.EncryptedCharField(max_length=9)),
                ('last_name', models.CharField(max_length=250)),
                ('first_name', models.CharField(max_length=250)),
                ('middle_names', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('postal_code', models.CharField(max_length=6)),
                ('drivers_licence', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField()),
                ('tax_year', models.IntegerField()),
                ('doc1', models.ImageField(upload_to='docs')),
                ('doc2', models.ImageField(upload_to='docs')),
                ('verified', models.BooleanField()),
            ],
            options={
                'db_table': 'income_verification',
            },
        ),
    ]
