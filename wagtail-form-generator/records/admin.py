import pdfkit
from django.http import HttpResponse
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from records.models import UserRecord
from django.template.loader import get_template

# Register your models here.
class UserRecordAdmin(ModelAdmin):
    model = UserRecord
    menu_label = "User Records"
    menu_icon = "placeholder"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False

    list_display = ('name', 'email')
    actions = ('create_pdf')

    def create_pdf(self, request, queryset):
        for obj in queryset:
            template = get_template('backend/pdf.html')
            html = template.render({'data': obj.data})
            options = {
                'page-size': 'Letter',
                'encoding': "UTF-8",
            }
            pdf = pdfkit.from_string(html, False, options)
            response = HttpResponse(pdf,content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="podium.pdf"'
            self.message_user(request, "pdf generated")
            return response

modeladmin_register(UserRecordAdmin)