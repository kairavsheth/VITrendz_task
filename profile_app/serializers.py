from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from profile_app.models import Profile, Friend, Tag


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ["id", "name"]


class ProfileSerializer(serializers.ModelSerializer):
    friends = FriendSerializer(many=True)
    tags = serializers.ListSerializer(child=serializers.CharField())

    class Meta:
        model = Profile
        fields = '__all__'

    def create(self, validated_data):
        if not validated_data['company'].lower() in validated_data['email'].lower():
            raise ValidationError({'email': 'Email must contain company name'})

        tags = validated_data.pop('tags')
        friends = validated_data.pop('friends')
        instance = Profile.objects.create(**validated_data)
        print(instance)
        for i in tags:
            Tag.objects.create(title=i, profile=instance)
        for i in friends:
            i['profile'] = instance
            Friend.objects.create(**i)
        return instance
