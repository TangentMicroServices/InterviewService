from rest_framework import serializers
from api.models import Category, Question


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    questions = serializers.HyperlinkedRelatedField(many=True, view_name="question-detail", read_only=True)

    class Meta:
        model = Category
        fields = ('url', 'pk', 'name', 'description', 'questions')


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('url', 'pk', 'name', 'answer', 'sequence', 'rows', 'category')
