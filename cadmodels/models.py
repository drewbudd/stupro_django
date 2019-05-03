from django.db import models

# Create your models here.
class CADModel(models.Model):
    name = models.CharField(max_length=50)
    checked_out = models.BooleanField("Checked out")
    ceation_date = models.DateTimeField(("date imported"), auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("CADModel_detail", kwargs={"pk": self.pk})

class Marker(models.Model):
    cad_model = models.ForeignKey("CADModel", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    status = models.ForeignKey("Status", null=True, on_delete=models.SET_NULL)
    type = models.ForeignKey("Type", on_delete=models.PROTECT)
    creation_date = models.DateTimeField(("date created"), auto_now_add=True)
    coord_x = models.DecimalField(("x coordinate"), max_digits=6, decimal_places=2)
    coord_y = models.DecimalField(("y coordinate"), max_digits=6, decimal_places=2)
    coord_z = models.DecimalField(("z coordinate"), max_digits=6, decimal_places=2)
    comments = models.CharField(max_length=500)

    class Meta:
        verbose_name = ("Marker")
        verbose_name_plural = ("Markers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Marker_detail", kwargs={"pk": self.pk})

class Status(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Status")
        verbose_name_plural = ("Statuses")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Status_detail", kwargs={"pk": self.pk})

class Type(models.Model):
    name = models.CharField(max_length=100)
    

    class Meta:
        verbose_name = ("Type")
        verbose_name_plural = ("Types")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Type_detail", kwargs={"pk": self.pk})


