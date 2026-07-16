from django.db import models

class AudioMediations(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    duration = models.IntegerField()
    audio_file = models.FileField(upload_to='mediation_audios/')
    source = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=20)
    
    
    def __str__(self) :
        return self.title

# Create your models here.
