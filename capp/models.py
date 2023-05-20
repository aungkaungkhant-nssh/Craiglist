from django.db import models



class Search(models.Model):
    search = models.CharField(max_length=300)
    created_at  = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return "{}".format(self.search)



