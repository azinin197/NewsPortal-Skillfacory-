from django.db import models
from datetime import datetime
from django.db.models import Sum
from django.contrib.auth.models import User


class Author(models.Model):
    relation = models.OneToOneField(User, on_delete=models.CASCADE)
    rating_aut = models.FloatField(default=0.0)

    def update_rating(self):
        postRat = self.post_set.aggregate(PostRating = Sum('rating_post'))
        pRat = 0
        pRat = pRat + postRat.get("PostRating")

        commentRat = self.relation.comment_set.aggregate(CommRating = Sum('rating_comm'))
        cRat = 0
        cRat = cRat + commentRat.get('CommRating')

        self.rating_aut = pRat*3 + cRat
        self.save()


class Category(models.Model):
    namecat = models.CharField(max_length=64, unique=True)


class Post(models.Model):
    news = 'NW'
    article = 'AR'
    FieldChoise = [
        (article, 'статья'),
        (news, 'новость')
    ]
    post_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    time_wr = models.DateTimeField(auto_now_add=True)
    post_category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=64)
    post_text = models.TextField()
    field_choise = models.CharField(max_length=2,
                                    choices=FieldChoise,
                                    default=article)
    rating_post = models.FloatField(default=0.0)

    def like(self):
        self.rating_post = self.rating_post + 1
        self.save()

    def dislike(self):
        self.rating_post = self.rating_post - 1
        self.save()

    def preview(self):
        return f"{self.post_text[0:128]} ..."


class PostCategory(models.Model):
    rel_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rel_cat = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post_comm = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_comm = models.ForeignKey(User, on_delete=models.CASCADE)
    comm_text = models.CharField(max_length=124)
    time_comm = models.DateTimeField(auto_now_add=True)
    rating_comm = models.FloatField(default=0.0)

    def like(self):
        self.rating_comm = self.rating_comm + 1
        self.save()

    def dislike(self):
        self.rating_comm = self.rating_comm - 1
        self.save()
