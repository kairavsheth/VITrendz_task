from django.db import models


# Create your models here.


class Profile(models.Model):
    guid = models.UUIDField(primary_key=True)
    isActive = models.BooleanField()
    balance = models.DecimalField(max_digits=7, decimal_places=2, )
    picture = models.URLField()
    age = models.IntegerField()
    eyeColor = models.CharField(max_length=16, )
    name = models.CharField(max_length=32, )
    gender = models.BooleanField(choices=((0, 'male'), (1, 'female')), )
    company = models.CharField(max_length=32, )
    email = models.EmailField(validators=(), )
    phone = models.CharField(max_length=16, validators=(), )
    address = models.TextField()
    about = models.TextField()
    registered = models.DateTimeField()
    longitude = models.DecimalField(max_digits=9, decimal_places=6, )
    latitude = models.DecimalField(max_digits=8, decimal_places=6, )
    greetings = models.TextField()


class Friend(models.Model):
    uid = models.IntegerField(primary_key=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='friends', )
    id = models.IntegerField()
    name = models.CharField(max_length=32, )

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.id = Friend.objects \
                .filter(profile=self.profile) \
                .aggregate(max_id=models.Max("project_id").get("max_id", 0) + 1)

        super().save(*args, **kwargs)


class Tag(models.Model):
    title = models.CharField(max_length=16, )


class Tag_Profile(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='tags', )
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='profiles', )
