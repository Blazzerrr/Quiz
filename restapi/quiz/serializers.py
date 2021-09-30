from rest_framework import serializers


class QuizSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=16)
    name = serializers.CharField(max_length=256)
    date_started = serializers.DateField(format="%d-%m-%Y")
    date_ended = serializers.DateField(format="%d-%m-%Y")
    description = serializers.CharField(max_length=512)


class QuestionSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=16)
    quiz_id = serializers.CharField(max_length=32)
    text = serializers.CharField(max_length=2048)
    type = serializers.CharField(max_length=1)


class AnswerSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=32)
    quiz_id = serializers.CharField(max_length=32)
    question_id = serializers.CharField(max_length=32)
    text = serializers.CharField(max_length=2048)
