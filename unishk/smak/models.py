from django.db import models

class Fakulteti(models.Model):
    
    emertimi = models.CharField(max_length=250,unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-updated']
    def __str__(self):
        return self.emertimi

class Departamenti(models.Model):
    emertimi = models.CharField(max_length=250,unique=True)
    fakulteti = models.ForeignKey(Fakulteti,
                             on_delete=models.CASCADE,
                             related_name='iperketfakultetit')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-updated']
    def __str__(self):
        return self.emertimi

class Programi(models.Model):
    emertimi = models.CharField(max_length=500,unique=True)
    departamenti = models.ForeignKey(Departamenti,
                             on_delete=models.CASCADE,
                             related_name='iperketdepartamentit')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-updated']
        indexes = [
            models.Index(fields=['-emertimi']),
        ]
    def __str__(self):
        return self.emertimi
    