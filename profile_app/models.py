from django.db import models


# Create your models here.


class Profile(models.Model):
    guid = models.UUIDField(primary_key=True)
    isActive = models.BooleanField()
    balance = models.CharField(max_length=16, )
    picture = models.URLField()
    age = models.IntegerField()
    eyeColor = models.CharField(max_length=16, )
    name = models.CharField(max_length=32, )
    gender = models.CharField(max_length=6, choices=(('male', 'male'), ('female', 'female')), )
    company = models.CharField(max_length=32, )
    email = models.EmailField(validators=(), )
    phone = models.CharField(max_length=32, )
    address = models.TextField()
    about = models.TextField()
    registered = models.DateTimeField()
    longitude = models.DecimalField(max_digits=9, decimal_places=6, )
    latitude = models.DecimalField(max_digits=8, decimal_places=6, )
    greeting = models.TextField()


class Friend(models.Model):
    uid = models.AutoField(primary_key=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='friends', )
    id = models.IntegerField()
    name = models.CharField(max_length=32, )

    def save(self, *args, **kwargs):
        if self.pk is None and self.id is None:
            self.id = Friend.objects \
                .filter(profile=self.profile) \
                .aggregate(max_id=models.Max("project_id").get("max_id", 0) + 1)

        super().save(*args, **kwargs)


class Tag(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='tags', )
    title = models.CharField(max_length=16, )

    def __str__(self):
        return self.title
