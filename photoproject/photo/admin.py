from django.contrib import admin

# Register your models here.

from .models import Category, PhotoPost, Comment


class CategoryAdmin(admin.ModelAdmin):
    """
    管理ページのレコード一覧に表示するカラムを設定するクラス
    """
    # レコード一覧にidとtitleを表示
    list_display = ("id", "title")
    # 表示するカラムにリンクを設定
    list_display_links = ("id", "title")


class PhotoPostAdmin(admin.ModelAdmin):
    """
        管理ページのレコード一覧に表示するカラムを設定するクラス
    """
    # レコード一覧にidとtitleを表示
    list_display = ("id", "title")
    # 表示するカラムにリンクを設定
    list_display_links = ("id", "title")


class CommentAdmin(admin.ModelAdmin):
    """
        管理ページのレコード一覧に表示するカラムを設定するクラス
    """


# django管理サイトにはCategory,CategoryAdminを登録する
admin.site.register(Category, CategoryAdmin)

# django管理サイトにはPhotoPost,PhotoPostAdminを登録する
admin.site.register(PhotoPost, PhotoPostAdmin)

admin.site.register(Comment, CommentAdmin)
