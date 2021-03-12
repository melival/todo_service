from django.core.management.base import BaseCommand, CommandError
from users.models import User
from mimesis import Person


class Command(BaseCommand):
    help = "Adds some users to application."

    def _add_new_user(self):
        user = User()
        perc = Person('en')

        user.user_name = perc.surname()
        user.first_name = perc.first_name()
        user.last_name = perc.last_name()
        user.email = perc.email()

        user.save()
        return user


    def add_arguments(self, parser):
        parser.add_argument('users_count', nargs='+', type=int)

    def handle(self, *args, **options):
        for i in range(options['users_count'][0]):
            user = self._add_new_user()
            self.stdout.write(self.style.SUCCESS(f"Successfully created user #{i+1}: \n\t {user}"))

