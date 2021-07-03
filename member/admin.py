from django.contrib import admin

from member.models import Sign

class MemberAdmin(admin.ModelAdmin) :
    list_display = (
        "user_id",
        "password",
        "email",
        "tel",
        "name",
        "birth",
        "gender",
        "address",
        "style",
        "job"
        )
admin.site.register(Sign,MemberAdmin)