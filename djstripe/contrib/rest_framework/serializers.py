# -*- coding: utf-8 -*-
"""
.. module:: dj-stripe.contrib.rest_framework.serializers.

    :synopsis: dj-stripe - Serializers to be used with the dj-stripe REST API.

.. moduleauthor:: Philippe Luickx (@philippeluickx)

"""

from __future__ import unicode_literals

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from djstripe.models import Subscription


class SubscriptionSerializer(ModelSerializer):
    """A serializer used for the Subscription model."""

    class Meta(object):
        """Model class options."""

        model = Subscription
        fields = "__all__"


class CreateSubscriptionSerializer(serializers.Serializer):
    """A serializer used to create a Subscription."""

    stripe_token = serializers.CharField(max_length=200)
    api_key = serializers.CharField(max_length=200, required=False)
    plan = serializers.CharField(max_length=50)
    account = serializers.CharField(max_length=100, required=False)
    charge_immediately = serializers.NullBooleanField(required=False)
    tax_percent = serializers.DecimalField(
        required=False,
        max_digits=5,
        decimal_places=2,
    )


class DeleteSubscriptionSerializer(serializers.Serializer):
    """A serializer used to create a Subscription."""

    plan = serializers.CharField(max_length=50, required=False)


class CreateChargeSerializer(serializers.Serializer):
    """A serializer used to create a customer charge."""

    stripe_token = serializers.CharField(max_length=200)
    api_key = serializers.CharField(max_length=200, required=False)
    amount = serializers.DecimalField(
        max_digits=5,
        decimal_places=2,
    )
