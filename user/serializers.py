from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'first_name', 'last_name', 'email']
        extra_kwargs = {
            'password' : {'write_only' : True}
        }

    def validate(self, data):

        ''' check if password less than 8 character '''
        if len(data['password']) < 8:
            raise serializers.ValidationError({
                'message' : 'Password must greater than 8 character'
            })

        ''' check if password & confirm password not match '''
        if data['password'] != data['password2']:
            raise serializers.ValidationError({
                'message' : 'Password must be match'
            })

        ''' delete password2 field from serializer data '''
        data.pop('password2', None)

        return data

    def create(self, validated_data):
        password = validated_data.get('password')
        user = User(**validated_data)

        # hash the user password
        user.set_password(password)
        user.save()
            
        return user

