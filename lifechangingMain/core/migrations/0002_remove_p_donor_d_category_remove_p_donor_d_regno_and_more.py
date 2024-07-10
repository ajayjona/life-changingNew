# Generated by Django 5.0.3 on 2024-07-06 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='p_donor',
            name='D_category',
        ),
        migrations.RemoveField(
            model_name='p_donor',
            name='D_regno',
        ),
        migrations.RemoveField(
            model_name='t_donor',
            name='td_howtocontact',
        ),
        migrations.AddField(
            model_name='p_donor',
            name='D_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='p_donor',
            name='D_email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='p_donor',
            name='D_item',
            field=models.CharField(blank=True, choices=[('select', 'Select'), ('money', 'Money'), ('clothes', 'Clothes'), ('food items', 'Food Items'), ('others', 'Others')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='p_donor',
            name='D_item_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='p_donor',
            name='D_verify',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='t_donor',
            name='td_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='t_donor',
            name='td_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='t_donor',
            name='td_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='t_donor',
            name='td_item',
            field=models.CharField(blank=True, choices=[('select', 'Select'), ('money', 'Money'), ('clothes', 'Clothes'), ('food items', 'Food Items'), ('others', 'Others')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='t_donor',
            name='td_item_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='p_donor',
            name='D_photo_logo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='t_donor',
            name='td_photo_logo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
