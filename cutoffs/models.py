from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import default

# Create your models here.

class University(models.Model):
	name=models.CharField(max_length=400, primary_key=True, unique=True)
	region=models.CharField(max_length=400,blank=True,null=True)
	total_institutions=models.IntegerField(blank=True,null=True)

	def __str__(self):
		return self.name


class College(models.Model):
	"""docstring for College"""
	code=models.IntegerField( primary_key=True,unique=True)
	name=models.CharField(max_length=400,blank=True)
	University=models.ForeignKey(University)
	total_branches=models.IntegerField(blank=True)
	city=models.CharField(max_length=400,blank=True,null=True)
	pincode=models.IntegerField(blank=True,null=True)
	"""def __init__(self, arg):
		super(College, self).__init__()
		self.arg = arg"""
	def __str__(self):
		tmp=""
		tmp+=(str)(self.code)
		tmp+=" "+self.name
		return tmp

class Branch(models.Model):
	code=models.IntegerField(primary_key=True,unique=True)
	name=models.CharField(max_length=400,blank=True,null=True)
	"""docstring for Branch"models.Modelf __init__(self, arg):
		super(Branch,models.Model.__init__()
		self.arg = arg"""
	def __str__(self):
		return (str)(self.code) + (str)(self.name)

class Category(models.Model):
	code=models.CharField(max_length=128,primary_key=True,unique=True)
	name=models.CharField(max_length=400,blank=True)

	def __str__(self):
		return (str)(self.code)+(str)(self.name)

class Gender(models.Model):
	code=models.CharField(max_length=128,primary_key=True,unique=True)
	name=models.CharField(max_length=400,blank=True)

	def __str__(self):
		return (str)(self.code)+(str)(self.name)



class CutOff(models.Model):
	UNIVERSITY_TYPE_CHOICES=(('H','Home'),
							  ('O','Other'))
								
	id=models.AutoField(primary_key=True,unique=True)
	cet_marks=models.IntegerField(blank=False)
	merit_no=models.IntegerField(blank=False)
	college=models.ForeignKey(College)
	branch=models.ForeignKey(Branch)
	category=models.ForeignKey(Category)
	gender=models.ForeignKey(Gender)
	university_type=models.CharField(choices=UNIVERSITY_TYPE_CHOICES,default="Other",max_length=128)
	"""docstring for CutOff
	def __init__(self, arg):
		super(CutOff, self).__init__()
		self.arg = arg"""
	
	def __str__(self):
		return (str)(self.id) + (str)(self.cet_marks) + (str)(self.merit_no)	
