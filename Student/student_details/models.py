from django.db import models
import re


class Education(models.Model):
    course = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    percentage = models.CharField(max_length=100)

    def __str__(self):
        return self.course


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class Student(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobileno = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='None')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    address = models.TextField()
    education = models.ForeignKey(Education, on_delete=models.CASCADE,)

    def __str__(self):
        return f'{self.username} Profile'


    def check_valid_mobile_no(self):
        result = re.compile("(0|91)?[7-9][0-9]{9}")
        pattern = result.match(self.mobileno)
        if pattern == None:
            return "this is not valid mobile number"
        else:
            return self.mobileno


    def check_valid_email(self):
        if (re.match("^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$", self.email) != None):
            return self.email
        return "colud you please provide correct email "

