from django.db import models  
class Applicants(models.Model):  
    Rollno = models.CharField(max_length=20,primary_key=True)  
    Name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  
    FatherName = models.EmailField(db_column='FatherName', max_length=20, blank=True, null=True)  
    Gender = models.CharField(db_column='Gender', max_length=20, blank=True, null=True)
    DOB = models.CharField(db_column='DOB', max_length=20, blank=True, null=True) 
    BIB = models.CharField(db_column='BIB', max_length=20, blank=True, null=True)
    chipcode1=models.CharField(db_column='chipcode1', max_length=20, blank=True, null=True)
    chipcode2=models.CharField(db_column='chipcode2', max_length=20, blank=True, null=True)


    class Meta:  
        db_table = "Applicants"  