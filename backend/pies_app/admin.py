from django.contrib import admin
from pies_app.models import Order, User, Basket, Pies

admin.site.register(User)
admin.site.register(Order)
admin.site.register(Basket)
admin.site.register(Pies)

