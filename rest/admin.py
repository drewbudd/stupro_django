from django.contrib import admin
import pprint
from django.contrib.sessions.models import Session
class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return pprint.pformat(obj.get_decoded())
    _session_data.allow_tags=True
    list_display = ['expire_date', 'session_key', '_session_data']
    readonly_fields = ['_session_data']
    exclude = ['session_data']
    date_hierarchy='expire_date'
admin.site.register(Session, SessionAdmin)

