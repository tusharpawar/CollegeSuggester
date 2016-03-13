from django.contrib import admin
from .models import *


# Register your models here.
class UniversityAdmin(admin.ModelAdmin):
	list_display=['name','region','total_institutions']

	class Meta:
		model=University

class CollegeAdmin(admin.ModelAdmin):
	list_display=['code','name','city']

	class Meta:
		model=College

class CategoryAdmin(admin.ModelAdmin):
	list_display=['code','name']

	class Meta:
		model=Category

class BranchAdmin(admin.ModelAdmin):
	list_display=['code','name']

	class Meta:
		model=Branch

class GenderAdmin(admin.ModelAdmin):
	list_display=['code','name']

	class Meta:
		model=Gender

class CutOffAdmin(admin.ModelAdmin):
	list_display=['id','cet_marks','merit_no','college','branch','category','gender','university_type']

	class Meta:
		model=CutOff


		
admin.site.register(University,UniversityAdmin)
admin.site.register(College,CollegeAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Branch,BranchAdmin)
admin.site.register(Gender,GenderAdmin)
admin.site.register(CutOff,CutOffAdmin)