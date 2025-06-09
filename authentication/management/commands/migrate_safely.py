import time
import sys
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.db import connection
import MySQLdb


class Command(BaseCommand):
    help = 'Runs migrations with retry logic for handling temporary database connection issues'

    def add_arguments(self, parser):
        parser.add_argument(
            '--max-retries',
            type=int,
            default=5,
            help='Maximum number of retry attempts'
        )
        parser.add_argument(
            '--retry-delay',
            type=int,
            default=5,
            help='Delay in seconds between retries'
        )

    def handle(self, *args, **options):
        max_retries = options['max_retries']
        retry_delay = options['retry_delay']
        
        for attempt in range(1, max_retries + 1):
            try:
                self.stdout.write(self.style.WARNING(f"Migration attempt {attempt}/{max_retries}..."))
                
                # Test database connection first
                connection.ensure_connection()
                
                # Run migrations
                call_command('migrate', '--no-input')
                
                self.stdout.write(self.style.SUCCESS("Migrations completed successfully!"))
                return
                
            except (MySQLdb.OperationalError, ConnectionError, Exception) as e:
                error_message = str(e)
                self.stdout.write(self.style.ERROR(f"Error during migration: {error_message}"))
                
                if "Access denied" in error_message:
                    self.stdout.write(self.style.ERROR(
                        "Database access denied. Please check your credentials and permissions."
                    ))
                
                if attempt < max_retries:
                    self.stdout.write(self.style.WARNING(
                        f"Retrying in {retry_delay} seconds (attempt {attempt}/{max_retries})..."
                    ))
                    time.sleep(retry_delay)
                else:
                    self.stdout.write(self.style.ERROR(
                        f"Migration failed after {max_retries} attempts."
                    ))
                    raise CommandError("Migration failed: Maximum retry attempts exceeded.") from e 