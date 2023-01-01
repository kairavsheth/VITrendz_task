from rest_framework import serializers

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
        print(validated_data)
        tags = validated_data.pop('tags')
        friends = validated_data.pop('friends')
        instance = Profile.objects.create(**validated_data)
        for i in tags:
            Tag.objects.create(title=i, profile=instance)
        for i in friends:
            Friend.objects.create(profile=instance, **i)
        return instance
