# Generated by Django 4.2 on 2023-06-11 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("photo", "0008_remove_comment_photo_post_comment_target_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment", old_name="target", new_name="photo_post",
        ),
    ]
