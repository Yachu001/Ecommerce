from django import template

register = template.Library()

@register.simple_tag(name= 'get_status')
def get_staus(status):
    status = status-1
    status_array =['Confirmed','Processed','Delivered','Rejected']
    return status_array[status]