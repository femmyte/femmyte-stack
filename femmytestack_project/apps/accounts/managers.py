from django.contrib.auth.base_user import BaseUserManager

# Manager is what we called that perform creation and retreiving model in database


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        """
        create and save a user with email and password

        1. check if there's email if not raise an error
        2. normalize the email
        3. set the email and other fields to the user model
        4. set th password
        5. save the user
        6. return the user
        """

        if not email:
            raise ValueError("Email is a required field.")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        create a superuser with email and password


        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must have is_staff==True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have is_superuser==True')
        return self.create_user(email, password, **extra_fields)
