from django.utils.translation import ugettext_lazy as _
from admin_tools.dashboard import modules, Dashboard

class CustomIndexDashboard(Dashboard):
    def __init__(self, **kwargs):
        Dashboard.__init__(self, **kwargs)
        self.columns = 1
        self.children.append(modules.Group(
            title="",
            display="tabs",
            css_classes=['column_1', 'open'],
            children=[
                modules.ModelList(
                    title='Models',
                )
            ]
        ))
        self.children.append(
            modules.LinkList(
                title=_('Media'),
                children=[
                    {
                        'title': _('File Browser'),
                        'url': '/admin/filebrowser/browse/',
                        'external': False,
                        'description': 'Manage uploaded files',
                    }
                ],
                css_classes=['column_2', 'open'],
            )
        )
        self.children.append(
            modules.RecentActions(
                title=_('Recent Actions'),
                css_classes=['column_2', 'open'],
                limit=6)
        )
