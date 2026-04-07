MY_OWN_SKILLS = ["webhooks", "core programming", "complex analysis", "quantum computing", "recursion", "texturing", "digital image processing", "python", "digital imaging", "exception handling", "typescript", "web development", "redux", "pandas", "systems analysis", "computer programming", "flask", "sorting", "analysis", "computer vision", "data structures", "sqlite", "image processing", "react", "computer hardware", "sql", "chinese language", "graphical user interface", "asp.net", "reading", "transformation", "object-oriented programming", "migration", "scripting", "problem solving", "algorithms", "api", "design analysis", "system analysis and design", "system design", "internet programming", "sql database", "database systems", "qiskit", "quantum gates", "hough transform", "mysql", "css", "english", "computing", "html", "database", "java", "communication", "c", "research", "Combinatorial Optimization", "Shading", "Genetic Algorithms", "Functional Programming", "Animation", "Styling", "Recreation", "REST API", "Dataset", "Data Processing", "Artificial Intelligence", "GitHub", "Programming Languages", "Git", "User Interface", "Optimization Software", "Project Performance", "Academic Papers", "Microsoft Word", "Language Skills", "JavaScript", "Programming", "Support", "Engineering", "Design", "calculus", "customer handling", "computer architecture", "computer maintenance", "air conditioning repair", "django", "ORM"]


from django.core.management.base import BaseCommand, CommandError
from apps.accounts.models.skill import Skill

class Command(BaseCommand):
    help = "Create initial Skill data"

    def handle(self, *args, **options):
        for s in MY_OWN_SKILLS:
            try:
                # Inserting new skill
                Skill.objects.get_or_create(name=s, verified=True)
            except Exception as e:
                # When insert something happened
                raise CommandError(e)