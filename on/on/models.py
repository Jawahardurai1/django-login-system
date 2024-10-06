from django.db import models

class login(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=12)  # Consider using a larger length or hashed password



# Uncomment and modify as needed
# class Register(models.Model):
#     usernames = models.CharField(max_length=200)
#     password = models.CharField(max_length=128)  # Use hashed passwords, for better security
#     confirm_password = models.CharField(max_length=128)  # Renamed for clarity
#     email = models.EmailField()  # Use EmailField for better validation

#     def __str__(self):
#         return self.usernames
