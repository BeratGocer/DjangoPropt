# Generated by Django 3.1.5 on 2023-07-25 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_kategorimodel_id_alter_yazimodel_id_yorummodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='IletisimModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=250)),
                ('isim_soyisim', models.CharField(max_length=150)),
                ('mesaj', models.TextField()),
                ('olusturulmaTarihi', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'iletişim',
                'verbose_name_plural': 'iletişim',
                'db_table': 'iletisim',
            },
        ),
        migrations.AlterField(
            model_name='kategorimodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='yazimodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='yorummodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]