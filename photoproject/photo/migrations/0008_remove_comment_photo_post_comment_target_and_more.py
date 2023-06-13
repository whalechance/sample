# Generated by Django 4.2 on 2023-06-11 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("photo", "0007_alter_comment_content_alter_comment_created_at"),
    ]

    operations = [
        migrations.RemoveField(model_name="comment", name="photo_post",),
        migrations.AddField(
            model_name="comment",
            name="target",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="text",
                to="photo.photopost",
                verbose_name="対象投稿",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="comment",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="投稿日時"),
        ),
    ]