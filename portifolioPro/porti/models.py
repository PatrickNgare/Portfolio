from django.db import models
from django.core.validators import URLValidator




class Tag(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name
        
class Portifolio(models.Model):
    title=models.CharField(max_length=70)
    details=models.TextField()
    giturl=models.TextField(validators=[URLValidator()])
    deployedurl=models.TextField(validators=[URLValidator()])
    porttags=models.ManyToManyField(Tag)
    port_image=models.ImageField(upload_to= 'portifolio/', null=True,blank=True)


    @classmethod
    def all_projects(cls):
        
        projects=cls.objects.all()
        return projects
    

    # @classmethod
    # def single_project(cls):
    #     projects=cls.objects.get(id)
    #     return projects



    def __str__(self):
        return self.title




