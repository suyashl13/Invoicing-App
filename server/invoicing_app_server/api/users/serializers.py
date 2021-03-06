from rest_framework.serializers import ModelSerializer
from .models import CustomUser, OTPSession


class CustomUserSerializer(ModelSerializer):
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        super_user_status = validated_data.pop('is_superuser', None)
        instance = self.Meta.model(**validated_data)

        if super_user_status:
            instance.is_superuser = False
        instance.save()

        if password is not None:
            instance.set_password(raw_password=password)
        instance.save()

        return instance

    def update(self, instance, validated_data):
        super_user_status = validated_data.pop('is_superuser', None)

        if super_user_status:
            instance.is_superuser = False

        instance.save()

        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(raw_password=value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'is_email_verified')


class OTPSessionSerializer(ModelSerializer):
    class Meta:
        model = OTPSession
        fields = '__all__'
