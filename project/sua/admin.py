from django.contrib import admin
from project.sua.models import Sua, Student, Proof, Sua_Application, SuaGroup, GSua, GSuaPublicity
from project.sua.models import Appeal


admin.site.register(Sua)
admin.site.register(Student)
admin.site.register(Proof)
admin.site.register(Sua_Application)
admin.site.register(SuaGroup)
admin.site.register(GSua)
admin.site.register(GSuaPublicity)
admin.site.register(Appeal)
