from django.db import models


class Blog(models.Model):
    author = models.CharField(max_length=30, null=True)
    title = models.CharField(max_length=130)
    # image = models.ImageField(upload_to='pics', null=True, blank=True)
    post_date = models.DateTimeField('date posted')
    reply_to = models.EmailField()
    content = models.TextField()

    def rating(self):
        comments = self.comment_set.all()

        if len(comments) == 0:
            return "unrated"

        sum = 0.0
        for c in comments:
            sum = sum + c.rating

        avg = float(sum)/len(comments)
        return "%.2f"%avg

    RATING_CHOICES = (
            (1, 'Bad'),
            (2, 'OK'),
            (3, 'Good'),
            (4, 'Nice'),
            (5, 'Great'),
    )

    class Admin:
        pass

    def __str__(self):
        return "Blog(title = %s)"%(self.title)


class Comment(models.Model):
    in_reference_to = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.CharField(max_length=256)
    rating = models.IntegerField(choices = Blog.RATING_CHOICES)

    def ratingText(self):
        return Blog.RATING_CHOICES[self.rating-1][1]

    class Admin:
        pass

    def __str__(self):
        return "Comment(content = '%s', rating = %s)"%(self.content, str(self.rating))
