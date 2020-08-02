from django.contrib import admin
from .models import (
    Book_Apointment_model,
    Decline_note,
    Medical_test,
    Send_report_to_pharmacy,
    confirm_drug
)
# Register your models here.


admin.site.register(Book_Apointment_model)
admin.site.register(Decline_note)
admin.site.register(Medical_test)
admin.site.register(Send_report_to_pharmacy)
admin.site.register(confirm_drug)