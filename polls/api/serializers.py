from rest_framework import serializers

from .models import Poll, Question, Choice

class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ['id', 'text']  # XXX map id to choice number somehow?

class QuestionSerializer(serializers.ModelSerializer):

    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'question_type', 'choices']  # XXX can we change id to question_id in the output?

class PollSerializer(serializers.ModelSerializer):

    questions = QuestionSerializer(many=True)

    class Meta:
        model = Poll
        fields = ['id', 'title', 'description', 'start_date', 'end_date', 'questions']
