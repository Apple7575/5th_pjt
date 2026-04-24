from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)  # 도서 제목
    description = models.TextField()          # 설명
    rating = models.FloatField()              # 회원 리뷰 평점 (소수점 허용을 위해 FloatField 사용)
    author = models.CharField(max_length=50)  # 저자

    def __str__(self):
        return self.title

