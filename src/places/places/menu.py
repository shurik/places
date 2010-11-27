from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from admin_tools.menu import items, Menu

class CustomMenu(Menu):
    """Custom Menu for Weekend Sherpa admin site."""
    def __init__(self, **kwargs):
        super(CustomMenu, self).__init__(**kwargs)
        self.children.append(items.MenuItem(
            title=_('Dashboard'),
            url=reverse('admin:index')
        ))
        self.children.append(items.MenuItem(
            title=_('Media'),
            children=[
                items.MenuItem(title=_('FileBrowser'), url='/admin/filebrowser/browse/')
            ]
        ))
