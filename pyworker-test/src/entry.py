from workers import WorkerEntrypoint
from wearhaus.wsgi import application
from django_cf import DjangoCF
import os

class Default(DjangoCF, WorkerEntrypoint):
    def get_app(self):
        return application