from django.contrib import admin
from register.models import Hood, Block, Registration, History, Friend, Neighbour, AuthBlock, Thread, Message, Authorize

# Register your models here.
admin.site.register(Hood)
admin.site.register(Block)
admin.site.register(Registration)
admin.site.register(History)
admin.site.register(Friend)
admin.site.register(Neighbour)
admin.site.register(AuthBlock)
admin.site.register(Thread)
admin.site.register(Message)
admin.site.register(Authorize)

