from django.contrib import admin

from .models import (
    ApportionmentRules,
    DebtCollection,
    Debts,
    Apportionment,
    DebtType,
    Payment,
    UserProfile,
)

admin.site.register(ApportionmentRules)
admin.site.register(DebtCollection)
admin.site.register(Debts)
admin.site.register(Apportionment)
admin.site.register(DebtType)
admin.site.register(Payment)
admin.site.register(UserProfile)
