# Generated by Django 2.2.14 on 2021-07-17 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=130)),
                ('post_date', models.DateTimeField(verbose_name='date posted')),
                ('reply_to', models.EmailField(max_length=254)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=256)),
                ('rating', models.IntegerField(choices=[(1, 'Lame'), (2, 'Weak'), (3, 'OK'), (4, 'Nice'), (5, 'Rocks')])),
                ('in_reference_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blog')),
            ],
        ),
    ]
