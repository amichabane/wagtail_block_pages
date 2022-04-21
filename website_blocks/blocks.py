
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class HeroText(blocks.StructBlock):
    title = blocks.RichTextBlock(default="Title", required=False)
    description = blocks.RichTextBlock(default="Description", required=False)
    button = blocks.CharBlock(default="Button", required=False)

    class Meta:
        template = 'website_blocks/hero_text.html'
        icon = 'image'

