import sys

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import StaffLevel

class Command(BaseCommand):
    help = 'Used to create a default StaffLevels.'

    def __init__(self, *args, **kwargs):
        user = StaffLevel(levelName="user", levelInt=-1)
        superuser = StaffLevel(levelName="superuser", levelInt=0)
        user.save()
        superuser.save()

    def execute(self, *args, **options):
        self.stdin = options.get('stdin', sys.stdin)  # Used for testing
        return super().execute(*args, **options)
