from django.contrib import admin
from . import models

from import_export import resources

class MovieResource(resources.ModelResource):

    class Meta:
        model = models.movie
        
class commentResource(resources.ModelResource):

    class Meta:
        model = models.comment
        
class ReviewsResource(resources.ModelResource):

    class Meta:
        model = models.reviewss
        
class CategoryResource(resources.ModelResource):

    class Meta:
        model = models.Category
        
class RateResource(resources.ModelResource):

    class Meta:
        model = models.rate
        
class YearResource(resources.ModelResource):

    class Meta:
        model = models.year
        
class SeriesResource(resources.ModelResource):

    class Meta:
        model = models.series
        
class EpisodeCommentResource(resources.ModelResource):

    class Meta:
        model = models.episode_comment
        
class EpisodeReviewResource(resources.ModelResource):

    class Meta:
        model = models.episode_review
        
class SeasonResource(resources.ModelResource):

    class Meta:
        model = models.season
        
class EpisodeResource(resources.ModelResource):

    class Meta:
        model = models.episode
        
class PhotoResource(resources.ModelResource):

    class Meta:
        model = models.photos
        
        
class ProfileResource(resources.ModelResource):

    class Meta:
        model = models.Profile
        
admin.site.register(models.movie)
admin.site.register(models.comment)
admin.site.register(models.reviewss)
admin.site.register(models.Category)
admin.site.register(models.rate)
admin.site.register(models.year)
admin.site.register(models.series)
admin.site.register(models.episode_comment)
admin.site.register(models.episode_review)
admin.site.register(models.season)
admin.site.register(models.episode)
admin.site.register(models.photos)
admin.site.register(models.Profile)
