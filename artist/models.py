from django.db import models


class Status(models.Model):
    """
    작가 등록 신청 상태에 대한 테이블입니다.
    id 1: 승인
    id 2: 대기
    id 3: 반려
    """
    status = models.CharField(max_length=5)


class Artist(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=16)
    gender = models.CharField(max_length=2)
    birthday = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    signup_date = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)


class Work(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    price = models.IntegerField()
    size = models.IntegerField()
    register_date = models.DateTimeField(auto_now_add=True)


class Exhibition(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField()
    work = models.ManyToManyField(Work)