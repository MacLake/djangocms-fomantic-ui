# Generated by Django 4.2.9 on 2024-01-22 12:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('djangocms_fomantic_ui', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='div',
            name='background_colour_choice',
            field=models.CharField(
                blank=True,
                choices=[
                    ('#FFFFFF', 'White'),
                    ('#F0F8FF', 'AliceBlue'),
                    ('#F0FFFF', 'Azure'),
                    ('#F5F5DC', 'Beige'),
                    ('#FFF8DC', 'Cornsilk '),
                    ('#FFFAF0', 'FloralWhite'),
                    ('#D3D3D3', 'LightGrey'),
                    ('#FFFAFA', 'Snow'),
                    ('#F5F5F5', 'WhiteSmoke'),
                    ('#f5f6f8', '#f5f6f8'),
                ],
                default='',
                help_text='Here are some predefined colours.',
                max_length=9,
                verbose_name='or choose',
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='div',
            name='background_colour_text',
            field=models.CharField(
                blank=True,
                default='',
                help_text='In CSS notation like "#789abc88" or decimal',
                max_length=20,
                verbose_name='Background colour name or value',
            ),
            preserve_default=False,
        ),
    ]
