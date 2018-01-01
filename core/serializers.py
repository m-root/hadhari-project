from rest_framework import serializers

from .models import Account,Branch,Volunteer


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id',
            'email',
            'full_name',
            'account_type',
            'account_profile',
            'is_superuser',
            'is_staff',
            'is_active'
        )


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = (
            'id',
            'name'
        )


class VolunteerSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField()

    class Meta:
        model = Volunteer
        fields = (
            'id',
            'dob',
            'Branch',
            'picture',
            'gender',
            'next_of_kin',
            'contact_number',
            'residence',
            'address'
        )
