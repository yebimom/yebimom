from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Initialize Regions Fixtures'

    def handle(self, *args, **options):
        self.stdout.write("hello world")
