# Generated by Django 4.1.5 on 2023-01-23 13:07

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.blocks
import wagtail.contrib.forms.models
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0083_alter_page_search_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.fields.RichTextField(blank=True, verbose_name='Introduction')),
                ('success_landing_content', wagtail.fields.StreamField([('rich_text', wagtail.blocks.RichTextBlock()), ('action_link', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(label='Link text', required=True)), ('external_url', wagtail.blocks.URLBlock(label='URL', required=False)), ('new_window', wagtail.blocks.BooleanBlock(label='Open in new window', required=False)), ('internal_page', wagtail.blocks.PageChooserBlock(label='Internal Page', required=False))])), ('inset_text', wagtail.blocks.StructBlock([('body', wagtail.blocks.RichTextBlock(required=True))]))], null=True, use_json_field=True)),
                ('general_enquiry_email', models.EmailField(help_text='Message will be sent to this email when user chooses "General enquiry" option.', max_length=255, null=True)),
                ('technical_support_email', models.EmailField(help_text='Message will be sent to this email when user chooses "Technical support" option.', max_length=255, null=True)),
                ('event_media_enquiries_email', models.EmailField(help_text='Message will be sent to this email when user chooses "Event and media enquiries" option.', max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.forms.models.FormMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('clean_name', models.CharField(blank=True, default='', help_text='Safe name of the form field, the label converted to ascii_snake_case', max_length=255, verbose_name='name')),
                ('label', models.CharField(help_text='The label of the form field', max_length=255, verbose_name='label')),
                ('field_type', models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('multiselect', 'Multiple select'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time'), ('hidden', 'Hidden field')], max_length=16, verbose_name='field type')),
                ('required', models.BooleanField(default=True, verbose_name='required')),
                ('choices', models.TextField(blank=True, help_text='Comma or new line separated list of choices. Only applicable in checkboxes, radio and dropdown.', verbose_name='choices')),
                ('default_value', models.TextField(blank=True, help_text='Default value. Comma or new line separated values supported for checkboxes.', verbose_name='default value')),
                ('help_text', models.CharField(blank=True, max_length=255, verbose_name='help text')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='contact_us.contactuspage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
