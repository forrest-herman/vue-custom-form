from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.api import APIField

from streams import blocks

class IntakePage(Page):
    
    # intro = models.CharField(max_length=2500)   # how to remove??

    content = StreamField(
        [
            ("question_range", blocks.QuestionRangeBlock()),
            ("question_mc", blocks.QuestionMultipleChoiceBlock()),
            ("question_text", blocks.QuestionTextFieldBlock()),
            ("richText", blocks.RichTextBlock()),
            # ("record", blocks.RecordBlock())
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [

        # FieldPanel('intro'),
        StreamFieldPanel("content"),
    ]

    api_fields = [
        APIField("title"),
        # APIField("intro"),
        APIField("content"),
    ]