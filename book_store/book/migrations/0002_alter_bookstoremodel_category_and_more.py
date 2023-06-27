# Generated by Django 4.1.5 on 2023-06-12 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookstoremodel',
            name='category',
            field=models.CharField(choices=[('Mystery', 'Mystery'), ('Thriller', 'Thriller'), ('Humor', 'Humor'), ('Horror', 'Horror'), ('Sci-Fi', 'Sci-Fi')], max_length=30),
        ),
        migrations.AlterField(
            model_name='bookstoremodel',
            name='last_pub',
            field=models.DateTimeField(auto_now=True),
        ),
    ]