# Generated by Django 3.2.14 on 2022-07-12 21:19

from django.db import migrations


def update_removed_targeting_config_slugs(apps, schema_editor):
    NimbusExperiment = apps.get_model("experiments", "NimbusExperiment")
    NimbusExperiment.objects.filter(
        targeting_config_slug="urlbar_firefox_suggest_us_en"
    ).update(targeting_config_slug="urlbar_firefox_suggest")


class Migration(migrations.Migration):

    dependencies = [
        ("experiments", "0214_migrate_sticky"),
    ]

    operations = [
        migrations.RunPython(update_removed_targeting_config_slugs),
    ]