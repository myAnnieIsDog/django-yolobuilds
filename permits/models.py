# ##########################################################################
# """ Base Models """
# ##########################################################################
# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes.models import ContentType
# from django.db import models
# from django.utils import timezone

# from locations.models import Parcel, SiteAddress
# from profiles.models import Division, Profile

# ##########################################################################
# """ Sequence Counts """
# ##########################################################################
# class Sequence(models.Model):
#     series_title = models.CharField(max_length = 55)
#     series_prefix = models.CharField(max_length=2)
#     year = models.DateTimeField(default=timezone.now().strftime("%Y"))
#     sequence = models.CharField(max_length=4, default="0000")

#     def __str__(self) -> str:
#         return self.series  
#     # BL, BP, CE, PW, ZF, Receipt, etc.

#     def next(series): # <- series title
#         n = Sequence.objects.get(series_title=series)
#         n.year = timezone.now().strftime("%Y")
#         n.sequence = str(int(n.sequence) + 1)
#         while len(n.sequence) < 4:
#             n.sequence = f"0{n.sequence}"
#         return f"{n.series}{n.year}-{n.sequence}"


# ##########################################################################
# """ Restrictions """
# ##########################################################################
# class Tag(models.Model):      
#     tag = models.CharField(max_length=100, unique=True)
#     policy = models.TextField(max_length=255)

#     def __str__(self) -> str:
#         return self.tag   

# class Restriction(models.Model):
#     tag = models.ForeignKey(Tag, on_delete=models.PROTECT)
#     policy = models.CharField(max_length=255, null=True, blank=True)

#     lock = models.BooleanField(
#         "Lock this record?", default=False)
#     lock_related = models.BooleanField(
#         "Lock related records?", default=False)
#     alert = models.BooleanField(
#         "Popup notification on this record?", default=True)
#     alert_related = models.BooleanField(
#         "Popup notification on related records?", default=False)

#     content_type = models.ForeignKey(
#         ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey("content_type", "object_id")

#     def __str__(self) -> str:
#         return self.tag.tag
    
#     class Meta:
#         indexes = [models.Index(fields=["content_type", "object_id",],),]

  
# ##########################################################################
# """ Permit Options """
# #########################################################################
# class PermitStatus(models.Model): 
#     status = models.CharField(max_length=30, unique=True)
#     policy = models.CharField(max_length=255)
#     build = models.BooleanField(default=False)
#     occupy = models.BooleanField(default=False)

#     class Meta():
#         verbose_name = "Permit Status"
#         verbose_name_plural = "Permit Statuses"

# class Form(models.Model):
#     form = models.CharField(max_length=255)

# class AppQuestion(models.Model):
#     question = models.TextField(max_length=255)

# class PermitType(models.Model): 
#     type = models.CharField(max_length=255, unique=True)
#     policy = models.CharField(max_length=255)
#     suffix = models.CharField(max_length=7, default="Ex-R", unique=True)
#     default_fees = models.ManyToManyField("fees.FeeType", blank=True)
#     default_reviews = models.ManyToManyField("reviews.ReviewType", blank=True)
#     default_inspection = models.ManyToManyField("inspections.InspectionType", blank=True)
#     default_forms = models.ManyToManyField(Form, blank=True)
#     default_app_questions = models.ManyToManyField(AppQuestion, blank=True)

#     class Meta():
#         verbose_name = "Permit Type"
#         verbose_name_plural = "Permit Types"

    
# ##########################################################################
# """ Permit Model """
# ##########################################################################
# class Permit(models.Model):
#     division = models.CharField(max_length=55, blank=True)
#     status = models.CharField(max_length=55, blank=True)

#     number = models.CharField(max_length=55, blank=True)
#     description = models.TextField(max_length=55)
#     details = models.TextField(max_length=255)
    
#     scope = models.CharField(max_length=55, blank=True)
#     apn = models.CharField(max_length=55, blank=True)
#     address = models.CharField(max_length=55, blank=True)
#     related_permits = models.CharField(max_length=55, blank=True)
#     contacts = models.CharField(max_length=55, blank=True)
#     app_questions = models.CharField(max_length=55, blank=True)
#     forms = models.CharField(max_length=55, blank=True)
#     reviews = models.CharField(max_length=55, blank=True)
#     inspections = models.CharField(max_length=55, blank=True)
#     fees = models.CharField(max_length=55, blank=True)

#     def __str__(self) -> str:
#         return f"{self.number}"

#     class Meta():
#         ordering = ["number"]
#         verbose_name = "Permit"
#         verbose_name_plural = "Permits"


# class ContactType(models.Model):
#     description = models.TextField(max_length=255)

#     def __str__(self) -> str:
#         return self.role
    

# class Contact(models.Model):
#     record = models.ForeignKey(Permit, on_delete=models.PROTECT)
#     contact = models.ForeignKey(Profile, on_delete=models.PROTECT)
#     contact_type = models.ForeignKey(ContactType, on_delete=models.PROTECT)

#     def __str__(self) -> str:
#         return f"{self.contact} is the {self.role} on {self.record}."
    
#     class Meta():
#         ordering = ["contact"]
#         verbose_name = "Contact"
#         verbose_name_plural = "Contacts"


# ##########################################################################
# """ All Models """
# ##########################################################################
# """This list only includes models that are in their stable form."""
# all_models = (
#     Sequence,
#     Tag,
#     Restriction,
#     Form,
#     AppQuestion,
#     PermitStatus,
#     PermitType,
#     Permit,
#     ContactType,
#     Contact,
# )
# ##########################################################################
# """ End File """
# ##########################################################################