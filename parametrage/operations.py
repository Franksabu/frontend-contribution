from django.contrib.auth.models import User
from django.db import transaction, IntegrityError

# from django.utils import timezone
import datetime


class OperationsHelpers:

    def execute_action(request, action, form):
        """
        Setting the user on create, update, validate
        """
        try:
            with transaction.atomic():
                obj = form.save(commit=False)
                user = User.objects.get(pk=request.user.id)  # get current user
                dateTimeNow = datetime.datetime.now()

                if action == "create":
                    obj.user_create = user

                if action == "validate":
                    obj.date_validate = dateTimeNow
                    obj.user_validate = user

                obj.save()

        except IntegrityError as e:
            return str(e)  # Autre erreur

        return ""
