from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin

class movieAdmin(ImportExportModelAdmin, admin.ModelAdmin):
        ...

admin.site.register(models.movie, movieAdmin)

class CommentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
        ...

admin.site.register(models.comment, CommentAdmin)

class ReviewsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
        ...

admin.site.register(models.reviewss, ReviewsAdmin)

class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
        ...

admin.site.register(models.Category, CategoryAdmin)

class RateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
        ...

admin.site.register(models.rate, RateAdmin)

class YearAdmin(ImportExportModelAdmin, admin.ModelAdmin):
        ...

admin.site.register(models.year, YearAdmin)

class SeriesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
        ...

admin.site.register(models.series, SeriesAdmin)


class EpisodeCommentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
        ...

admin.site.register(models.episode_comment, EpisodeCommentAdmin)

class EpisodereviewAdmin(ImportExportModelAdmin, admin.ModelAdmin):
        ...

admin.site.register(models.episode_review, EpisodereviewAdmin)

class SeasonAdmin(ImportExportModelAdmin, admin.ModelAdmin):
        ...

admin.site.register(models.season, SeasonAdmin)

class EpisodeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
        ...

admin.site.register(models.episode, EpisodeAdmin)

class PhotosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
        ...

admin.site.register(models.photos, PhotosAdmin)

class ProfileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
        ...

admin.site.register(models.Profile, ProfileAdmin)

