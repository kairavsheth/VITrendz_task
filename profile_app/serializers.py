from rest_framework import serializers

from profile_app.models import Profile, Friend, Tag


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ["id", "name"]


class ProfileSerializer(serializers.ModelSerializer):
    friends = FriendSerializer(many=True)
    tags = serializers.ListSerializer(child=serializers.CharField(source='tags.title'))

    class Meta:
        model = Profile
        fields = ["guid", "isActive", "balance", "picture", "age", "eyeColor", "name", "gender", "company", "email",
                  "phone", "address", "about", "registered", "longitude", "latitude", "friends", "tags", "greetings"]
