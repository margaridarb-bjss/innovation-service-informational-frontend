from django.core.exceptions import ValidationError

from wagtail.admin.panels import FieldPanel
from wagtail.models import Page, TranslatableMixin
from wagtailmetadata.models import MetadataPageMixin
from wagtail_localize.fields import SynchronizedField


class BasePage(MetadataPageMixin, Page, TranslatableMixin):

    # Editor panels configuration.
    promote_panels = [
        FieldPanel('slug'),
        FieldPanel('seo_title'),
        # FieldPanel('show_in_menus'),
        FieldPanel('search_description'),
        FieldPanel('search_image')
    ]

    override_translatable_fields = [
        SynchronizedField("slug", overridable=False),
    ]

    def full_clean(self, *args, **kwargs):
        """Override validation making 'search_description' field required."""

        errors = {}

        if not self.search_description:
            errors['search_description'] = 'This field is required'

        if errors:
            raise ValidationError(errors)

    class Meta:
        abstract = True


BasePage._meta.get_field('seo_title').verbose_name = 'Search title'
BasePage._meta.get_field('search_description').verbose_name = 'Search description'
