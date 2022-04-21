from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField

from wagtail.core.models import Page

from website_blocks.blocks import HeroText


class HomePage(Page):
    body = StreamField([
        ('HeroText', HeroText()),
    ], null=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

