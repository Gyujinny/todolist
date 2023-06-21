"""
Serializers for TodoItem APIs
"""
from rest_framework import serializers

from core.models import TodoItem


class TodoItemSerializer(serializers.ModelSerializer):
    """Serializer for TodoItem."""

    class Meta:
        model = TodoItem
        fields = ['user', 'title', 'description', 'duration_min', 'due_date']
        read_only_fields = ['user']

class TodoItemDetailSerializer(TodoItemSerializer):
    """Serializer for TodoItem detail."""


    class Meta(TodoItemSerializer.Meta):
        fields = TodoItemSerializer.Meta.fields

    # Necessary to override the create() method if needed
    # def create(self, validated_data):
    #     """Create a recipe."""
    #     recipe = TodoItem.objects.create(**validated_data)
    #     return recipe
    #
    # def update(self, instance, validated_data):
    #     """Update recipe."""
    #     for attr, value in validated_data.items():
    #         setattr(instance, attr, value)
    #
    #     instance.save()
    #     return instance