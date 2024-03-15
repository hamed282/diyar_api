from django.db import models


class EvaluationModel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField()
    nationality = models.CharField(max_length=30)
    birthdate = models.IntegerField()
    male = models.BooleanField()
    female = models.BooleanField()
    married = models.BooleanField()
    children_number = models.IntegerField()
    # children_age =
    # education =
    IELTS_test = models.BooleanField()
    # work_experiences =

    partner_first_name = models.CharField(max_length=30)
    partner_last_name = models.CharField(max_length=30)
    partner_phone_number = models.CharField(max_length=30)
    partner_email = models.EmailField(max_length=100)
    partner_nationality = models.CharField(max_length=30)
    partner_birthdate = models.IntegerField()
    # partner_education =
    partner_IELTS_test = models.BooleanField()
    # partner_work_experiences =

    owner_license = models.BooleanField()
    rejection_history = models.BooleanField()
    rejection_history_info = models.TextField()
    tourist_visa_status = models.BooleanField()
    has_relatives = models.BooleanField()
    relative = models.CharField(max_length=30)
    customer_interaction_method = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Evaluation'
        verbose_name_plural = 'Evaluation'


class ChildrenAgeModel(models.Model):
    user = models.ForeignKey(EvaluationModel, on_delete=models.CASCADE)
    child_age = models.IntegerField()

    class Meta:
        verbose_name = 'Children Age'
        verbose_name_plural = 'Children Age'


class EducationModel(models.Model):
    user = models.ForeignKey(EvaluationModel, on_delete=models.CASCADE)
    university = models.CharField(max_length=100)
    r = models.CharField(max_length=100)
    l = models.CharField(max_length=100)
    d = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Education'


class WorkExperiencesModel(models.Model):
    user = models.ForeignKey(EvaluationModel, on_delete=models.CASCADE)
    sh = models.CharField(max_length=100)
    s = models.CharField(max_length=100)
    m = models.CharField(max_length=100)
    b = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Work Experiences'
        verbose_name_plural = 'Work Experiences'


class PartnerEducationModel(models.Model):
    user = models.ForeignKey(EvaluationModel, on_delete=models.CASCADE)
    university = models.CharField(max_length=100)
    r = models.CharField(max_length=100)
    l = models.CharField(max_length=100)
    d = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Partner Education'
        verbose_name_plural = 'Partner Education'


class PartnerWorkExperiencesModel(models.Model):
    user = models.ForeignKey(EvaluationModel, on_delete=models.CASCADE)
    sh = models.CharField(max_length=100)
    s = models.CharField(max_length=100)
    m = models.CharField(max_length=100)
    b = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Partner Work Experiences'
        verbose_name_plural = 'Partner Work Experiences'
