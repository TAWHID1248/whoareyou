import csv
import os
from django.core.management.base import BaseCommand
from myapp.models import Person

class Command(BaseCommand):
    help = 'Import people data from CSV file'

    def handle(self, *args, **kwargs):
        # Use BASE_DIR to construct the absolute path
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_file_path = os.path.join(BASE_DIR, 'myapp', 'test.csv')  # Adjust this path

        with open(csv_file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Person.objects.create(
                    name=row['name'],
                    age=row['age'],
                    phone_number=row['phone_number'],
                    address=row['address']
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported data'))
