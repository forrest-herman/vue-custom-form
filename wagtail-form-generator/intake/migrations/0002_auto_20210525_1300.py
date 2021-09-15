# Generated by Django 3.1.1 on 2021-05-25 17:00

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('intake', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intakepage',
            name='content',
            field=wagtail.core.fields.StreamField([('question_range', wagtail.core.blocks.StructBlock([('question', wagtail.core.blocks.CharBlock(max_length=1000)), ('range_min_value', wagtail.core.blocks.IntegerBlock(default='1', label='Lower Bound Value')), ('range_max_value', wagtail.core.blocks.IntegerBlock(default='5', label='Upper Bound Value')), ('range_min_text', wagtail.core.blocks.CharBlock(default='Low Side', label='Text for minimum end of scale', max_length=1000)), ('range_max_text', wagtail.core.blocks.CharBlock(default='High Side', label='Text for maximum end of scale', max_length=1000)), ('question_mandatory', wagtail.core.blocks.BooleanBlock(default=True, label='Make this question mandatory?', required=False))])), ('question_mc', wagtail.core.blocks.StructBlock([('question', wagtail.core.blocks.CharBlock(max_length=500)), ('mc_type', wagtail.core.blocks.ChoiceBlock(choices=[('mc_radio', 'Radio (Select One)'), ('mc_checkbox', 'Checkbox (Select Multiple)')], label='Multiple Choice Question Type')), ('choice_1', wagtail.core.blocks.CharBlock(label='Option 1', max_length=1000)), ('choice_2', wagtail.core.blocks.CharBlock(label='Option 2', max_length=1000)), ('choice_3', wagtail.core.blocks.CharBlock(label='Option 3', max_length=1000, required=False)), ('choice_4', wagtail.core.blocks.CharBlock(label='Option 4', max_length=1000, required=False)), ('choice_5', wagtail.core.blocks.CharBlock(label='Option 5', max_length=1000, required=False)), ('question_mandatory', wagtail.core.blocks.BooleanBlock(default=True, label='Make this question mandatory?', required=False))])), ('question_text', wagtail.core.blocks.StructBlock([('question', wagtail.core.blocks.CharBlock(max_length=1000)), ('validation_type', wagtail.core.blocks.ChoiceBlock(choices=[('alpha_spaces', 'Text'), ('email', 'Email'), ('numeric', 'Phone'), ('numeric', 'Number'), ('date', 'Year')], label='Field Type')), ('question_mandatory', wagtail.core.blocks.BooleanBlock(default=True, label='Make this question mandatory?', required=False))])), ('richText', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Must be unique', max_length=250, required=True)), ('title_type', wagtail.core.blocks.ChoiceBlock(choices=[('pillar', 'Pillar'), ('category', 'Category'), ('title', 'Title')], label='Title Type')), ('description', wagtail.core.blocks.RichTextBlock(required=False))]))], blank=True, null=True),
        ),
    ]
