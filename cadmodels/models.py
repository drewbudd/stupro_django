from django.db import models

# Create your models here.
class CADModel(models.Model):
    model_name = models.CharField(max_length=50)
    checked_out = models.BooleanField(False)
    ceation_date = models.DateTimeField(_("date imported"), auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("CADModel_detail", kwargs={"pk": self.pk})

class Marker(models.Model):
    cad_model = models.ForeignKey("CADModel", on_delete=models.CASCADE)
    marker_name = models.CharField(max_length=100)
    status = models.ForeignKey("Status", on_delete=models.SET_NULL)
    type = models.ForeignKey("Type", on_delete=models.PROTECT)
    creation_date = models.DateTimeField(_("date created"), auto_now_add=False)
    coord_x = models.DecimalField(_("x coordinate"), max_digits=6, decimal_places=2)
    coord_y = models.DecimalField(_("y coordinate"), max_digits=6, decimal_places=2)
    coord_z = models.DecimalField(_("z coordinate"), max_digits=6, decimal_places=2)
    comments = models.CharField(max_length=500)

    class Meta:
        verbose_name = _("Marker")
        verbose_name_plural = _("Markers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Marker_detail", kwargs={"pk": self.pk})

class Status(models.Model):
    status_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = _("Status")
        verbose_name_plural = _("Statuses")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Status_detail", kwargs={"pk": self.pk})

class Type(models.Model):
    type_name = models.CharField(max_length=100)
    

    class Meta:
        verbose_name = _("Type")
        verbose_name_plural = _("Types")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Type_detail", kwargs={"pk": self.pk})


