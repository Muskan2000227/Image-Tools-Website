from django.contrib import admin
from imageapp.models import person,FAQ,myreview
from imageapp.models import contactme,register
from imageapp.models import Help
from imageapp.models import article
from imageapp.models import editor


# Register your models here.
admin.site.register(person)
admin.site.register(FAQ)
admin.site.register(myreview)
admin.site.register(Help)
admin.site.register(contactme)
admin.site.register(register)
admin.site.register(article)
admin.site.register(editor)