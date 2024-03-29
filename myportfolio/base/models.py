from django.db import models

from wagtail.admin.panels import FieldPanel, MultiFieldPanel, PublishingPanel, InlinePanel, FieldRowPanel
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting
from wagtail.fields import RichTextField
from wagtail.models import DraftStateMixin, PreviewableMixin, RevisionMixin, TranslatableMixin
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.panels import FormSubmissionsPanel


@register_setting
class NavigationSettings(BaseGenericSetting):
    x_url = models.URLField(verbose_name="X URL", blank=True)
    github_url = models.URLField(verbose_name="Github URL", blank=True)
    mastodon_url = models.URLField(verbose_name="Mastodon URL", blank=True)
    linkedin_url = models.URLField(verbose_name="LinkedIn URL", blank=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("x_url"),
                FieldPanel("github_url"),
                FieldPanel("mastodon_url"),
                FieldPanel("linkedin_url")
            ],
            "Social settings",
        )
    ]


@register_snippet
class FooterText(
    DraftStateMixin,
    RevisionMixin,
    PreviewableMixin,
    TranslatableMixin,
    models.Model,
):
    body = RichTextField()

    panels = [
        FieldPanel("body"),
        PublishingPanel(),
    ]

    def __str__(self):
        return "Footer text"

    def get_preview_template(self, request, mode_name):
        return "base.html"

    def get_preview_context(self, request, mode_name):
        return {"footer_text": self.body}

    class Meta(TranslatableMixin.Meta):
        verbose_name_plural = "Footer Text"


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')


class FormPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('intro'),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address'),
                FieldPanel('to_address'),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]
