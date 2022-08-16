from django.contrib import admin

# Register your models here.
from .models import Family,Sender,Cabin,Camper,Letter,tx#,Photo
admin.site.register(Family)
admin.site.register(Sender)
admin.site.register(Cabin)
admin.site.register(Camper)
admin.site.register(Letter)
admin.site.register(tx)
#admin.site.register(Photo)



