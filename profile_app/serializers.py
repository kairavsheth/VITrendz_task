from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from profile_app.models import Profile, Friend, Tag


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ["id", "name"]


def ProfileSerializer(_fields):
    class _ProfileSerializer(serializers.ModelSerializer):
        if _fields == '__all__' or 'friends' in _fields:
            friends = FriendSerializer(many=True)
        if _fields == '__all__' or 'tags' in _fields:
            tags = serializers.ListSerializer(child=serializers.CharField())

        class Meta:
            model = Profile
            fields = _fields

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
    return _ProfileSerializer
