from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.db import models

# Create your models here.
from django.conf import settings

star_Choices = (
    ("⭐", "⭐"),
    ("⭐⭐", "⭐⭐"),
    ("⭐⭐⭐", "⭐⭐⭐"),
    ("⭐⭐⭐⭐", "⭐⭐⭐⭐"),
    ("⭐⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"),
)


class Review(models.Model):
    title = models.CharField(max_length=20)
    grade = models.CharField(max_length=10, choices=star_Choices)
    content = models.TextField()
    # image = ProcessedImageField(
    #     upload_to="images/",
    #     blank=True,
    #     processors=[ResizeToFill(1200, 960)],
    #     format="JPEG",
    #     options={"quality": 80},
    # )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_revies"
    )
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="작성일")

    class Meta:
        db_table = "리뷰"
        verbose_name = "리뷰"
        verbose_name_plural = "리뷰"


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="댓글내용")
    created = models.DateTimeField(auto_now_add=True, verbose_name="작성일")
    # deleted = models.BooleanField(default=False, verbose_name='삭제여부')
    # reply = models.IntegerField(verbose_name='답글위치', default=0)
    def __str__(self):
        return self.content

    # @property
    # def created_string(self):
    #     time = datetime.now(tz=timezone.utc) - self.created

    #     if time < timedelta(minutes=1):
    #         return '방금 전'
    #     elif time < timedelta(hours=1):
    #         return str(int(time.seconds / 60)) + '분 전'
    #     elif time < timedelta(days=1):
    #         return str(int(time.seconds / 3600)) + '시간 전'
    #     elif time < timedelta(days=7):
    #         time = datetime.now(tz=timezone.utc).date() - self.created.date()
    #         return str(time.days) + '일 전'
    #     else:
    #         return False

    class Meta:
        db_table = "댓글"
        verbose_name = "댓글"
        verbose_name_plural = "댓글"


# 단일 파일은 도저히 처리 불가능.
# 모델을 새로 만듬.
class ReviewImage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
