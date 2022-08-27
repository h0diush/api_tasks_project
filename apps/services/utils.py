from rest_framework import serializers


def get_tags_for_tasks(task, model_serializers: serializers.ModelSerializer):
    tags = task.tags.all()
    serializer = model_serializers(tags, many=True)
    return serializer.data
