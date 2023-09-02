from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=80, verbose_name='Name', blank=False)
    email = models.EmailField(max_length=200, verbose_name='Email', blank=True)
    subject = models.CharField(max_length=80, verbose_name='Subject', blank=False)
    message = models.TextField(verbose_name='Message', blank=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')

    class Meta:
        # Sort Contact records in chronological order by default
        ordering = ('created',)

    def __str__(self):
        return f"Contact from {self.name} ({self.email}) - {self.subject}"
