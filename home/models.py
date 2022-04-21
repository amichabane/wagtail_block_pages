from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField

from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock

from website_blocks.blocks import HeroText, CardBlock, QuoteBlock, FeaturedBlock, EmaildBlock


class HomePage(Page):
    body = StreamField([
        ('HeroText', HeroText()),
        ('Cards', CardBlock()),
        ('Quotes', QuoteBlock()),
        ('Features', FeaturedBlock()),
        ('Email', EmaildBlock())
    ], null=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
