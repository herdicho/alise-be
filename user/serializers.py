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
        
        ''' check is email unique '''
        email = data['email'].lower()
        is_email_unique = User.objects.filter(email = email).count()
        if (is_email_unique > 0):
            raise serializers.ValidationError({
                'message' : 'email not unique'
            })
        
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

        ''' lowercase the username '''
        data['username'] = data['username'].lower()

        return data

    def create(self, validated_data):
        password = validated_data.get('password')
        user = User(**validated_data)

        # hash the user password
        user.set_password(password)
        user.save()
            
        return user

