from django.core.management.base import BaseCommand
from exercises_app.update_bands import bands_still_active


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        bands_still_active()
