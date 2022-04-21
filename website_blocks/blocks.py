from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class HeroText(blocks.StructBlock):
    title = blocks.RichTextBlock(default="Title", required=False)
    description = blocks.RichTextBlock(default="Description", required=False)
    button = blocks.CharBlock(default="Button", required=False)
    image=ImageChooserBlock()

    class Meta:
        template = 'website_blocks/hero_text.html'
        icon = 'image'


class CardBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False, help_text="Add your title")
    text = blocks.RichTextBlock(required=False, help_text="Add your title")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=False)),
                ("title", blocks.CharBlock(required=False, max_length=40)),
                ("text", blocks.TextBlock(required=False, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False,
                                               help_text="If the button page above is selected, that will be used first.")),
            ]
        )
    )

    class Meta:  # noqa
        template = "website_blocks/card_block.html"
        icon = "placeholder"


class QuoteBlock(blocks.StructBlock):

    text = blocks.RichTextBlock(required=False, help_text="Add your text")
    image=ImageChooserBlock()
    username=blocks.CharBlock(required=False,help_text="Add Your Username")
    job=blocks.CharBlock(required=False,help_text="Add Your Job")

    class Meta:  # noqa
        template = "website_blocks/quote_block.html"
        icon = "placeholder"


class FeaturedBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=False, help_text="Add Your title")
    features=blocks.ListBlock(
        blocks.StructBlock([
            ("text", blocks.RichTextBlock(required=False, help_text="Add your text")),
            ("image",ImageChooserBlock()),
            ("subtitle" ,blocks.CharBlock(required=False, help_text="Add Your Username"))
    ]
    )
    )
    class Meta:  # noqa
        template = "website_blocks/featured.html"
        icon = "placeholder"


class EmaildBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=False, help_text="Add Your title")
    description = blocks.RichTextBlock(required=False, help_text="Add your text")
    subtexte=blocks.RichTextBlock(required=False,help_text="Add Your SubText")

    class Meta:  # noqa
        template = "website_blocks/Email.html"
        icon = "placeholder"