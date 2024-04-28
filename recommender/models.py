from django.db import models


class AnswerModel(models.Model):
    answer = models.CharField(max_length=100)
    point = models.IntegerField()

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    def __str__(self):
        return f'{self.answer}'


class QuestionModel(models.Model):
    question = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return f'{self.question}'


class PersonalInformationModel(models.Model):
    objects = None
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.question}'


class JobRecordModel(models.Model):
    objects = None
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.question}'


class EducationalRecordModel(models.Model):
    objects = None
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.question}'


class IncomeModel(models.Model):
    objects = None
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.question}'


class SkillModel(models.Model):
    objects = None
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.question}'


class AddAnswerModel(models.Model):
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE, related_name='answer_rel')
    answer = models.ForeignKey(AnswerModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.question}'
