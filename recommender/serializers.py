from rest_framework import serializers
from .models import PersonalInformationModel, SkillModel, IncomeModel, JobRecordModel, EducationalRecordModel


class PersonalInformationSerializer(serializers.ModelSerializer):
    question = serializers.SlugRelatedField(slug_field='question', read_only=True)
    answers = serializers.SerializerMethodField()

    class Meta:
        model = PersonalInformationModel
        fields = ['question', 'answers']

    def get_answers(self, obj):
        add_answers = obj.question.answer_rel.all()
        answers = []
        for answer in add_answers:
            answers.append({'answer': answer.answer.answer, 'point': answer.answer.point})

        return answers


class SkillSerializer(serializers.ModelSerializer):
    question = serializers.SlugRelatedField(slug_field='question', read_only=True)
    answers = serializers.SerializerMethodField()

    class Meta:
        model = SkillModel
        fields = ['question', 'answers']

    def get_answers(self, obj):
        add_answers = obj.question.answer_rel.all()
        answers = []
        for answer in add_answers:
            answers.append({'answer': answer.answer.answer, 'point': answer.answer.point})

        return answers


class IncomeSerializer(serializers.ModelSerializer):
    question = serializers.SlugRelatedField(slug_field='question', read_only=True)
    answers = serializers.SerializerMethodField()

    class Meta:
        model = IncomeModel
        fields = ['question', 'answers']

    def get_answers(self, obj):
        add_answers = obj.question.answer_rel.all()
        answers = []
        for answer in add_answers:
            answers.append({'answer': answer.answer.answer, 'point': answer.answer.point})

        return answers

class JobRecordSerializer(serializers.ModelSerializer):
    question = serializers.SlugRelatedField(slug_field='question', read_only=True)
    answers = serializers.SerializerMethodField()

    class Meta:
        model = JobRecordModel
        fields = ['question', 'answers']

    def get_answers(self, obj):
        add_answers = obj.question.answer_rel.all()
        answers = []
        for answer in add_answers:
            answers.append({'answer': answer.answer.answer, 'point': answer.answer.point})

        return answers


class EducationalRecordSerializer(serializers.ModelSerializer):
    question = serializers.SlugRelatedField(slug_field='question', read_only=True)
    answers = serializers.SerializerMethodField()

    class Meta:
        model = EducationalRecordModel
        fields = ['question', 'answers']

    def get_answers(self, obj):
        add_answers = obj.question.answer_rel.all()
        answers = []
        for answer in add_answers:
            answers.append({'answer': answer.answer.answer, 'point': answer.answer.point})

        return answers
