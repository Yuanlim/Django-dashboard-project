COURSE_I_ATTENDED = [
    "Computer Programming",
    "Internet Programming Laboratory",
    "Introduction to Telecommunications",
    "Introductory Electrical Engineering Laboratory",
    "Communications Engineering",
    "Computer Networks",
    "Circuit Theory",
    "Data Structure",
    "Data Structures Lab",
    "Digital Design",
    "Digital Design Laboratory",
    "Assembly Language",
    "Electronic Circuits",
    "Electronic Circuits Laboratory",
    "Operating System Laboratory",
    "Operating Systems Applications",
    "Windows Programming",
    "Algorithms",
    "Applications Practice of Mobile Operating Systems",
    "Big Data Analytics in Practice",
    "Cloud Computing",
    "Digital Electronic Circuits",
    "Microprocessor-Based Applications",
    "Systems Programming",
    "Windows Application Programming Lab",
    "Computer Organization",
    "Database Systems",
    "Introduction to Multimedia and Computer Networks",
    "Introduction to Quantum Computing",
    "Microprocessors Laboratory",
    "Practical Projects",
    "Systems Analysis and Design",
    "Artificial Intelligence",
    "Computational Intelligence",
    "Computer Graphics",
    "Broad-band Networks",
    "Color Video Signal Processing",
    "Personal and Mobile Communications Systems",
    "Seminar on Computer and Communication Systems",
    "Communications Systems",
    "Wireless Devices Design Laboratory",
    "Computer Vision",
    "Mobile Edge Computing",
    "VLSI Design Laboratory",
    "Digital Communication Theory",
    "Digital Image Processing",
    "Thesis"
]

from django.core.management.base import BaseCommand, CommandError
from apps.accounts.models.profile_properties import Course

class Command(BaseCommand):
    help = "Create initial Course data"

    def handle(self, *args, **options):
        for s in COURSE_I_ATTENDED:
            try:
                # Inserting new skill
                Course.objects.get_or_create(name=s, verified=True)
            except Exception as e:
                # When insert something happened
                raise CommandError(e)