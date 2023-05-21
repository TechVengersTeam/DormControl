# from django.db import models
# from django.contrib.auth.models import User

# class Student(User):
#     YEAR_IN_CHOICE = [
#         (1, 1),
#         (2, 2),
#         (3, 3)
#     ]
#     # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     name = models.CharField(max_length=50, blank=False)
#     libid = models.BigIntegerField()
#     course = models.CharField(max_length=20, blank=False)
#     branch = models.CharField(max_length=20, blank=False)
#     year = models.PositiveSmallIntegerField()
#     phone = models.BigIntegerField()
#     address = models.TextField()
#     admin = models.BooleanField(default=False)

