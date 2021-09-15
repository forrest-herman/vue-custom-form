"""Streamfields live in here"""

# from typing_extensions import Required
from wagtail.core import blocks

class RichTextBlock(blocks.StructBlock):
    """Select the name of your category"""
    title = blocks.CharBlock(max_length=250, help_text='Must be unique', required=True)
    title_type = blocks.ChoiceBlock(label="Title Type", choices=[('pillar','Pillar'),('category','Category'),('title','Title')], required=True)
    description = blocks.RichTextBlock(required=False)

    class Meta: # noqa
        # template = "streams/category.html"
        icon = "edit"
        label = "Text Field"


class QuestionRangeBlock(blocks.StructBlock):
    """Questions with a rating or range answer"""
    question = blocks.CharBlock(max_length=1000)
    range_min_value = blocks.IntegerBlock(default="1", label="Lower Bound Value")
    range_max_value = blocks.IntegerBlock(default="5", label="Upper Bound Value")
    range_min_text = blocks.CharBlock(max_length=1000, default="Low Side", label="Text for minimum end of scale")
    range_max_text = blocks.CharBlock(max_length=1000, default="High Side", label="Text for maximum end of scale")

    question_mandatory = blocks.BooleanBlock(label="Make this question mandatory?", default=True, required=False)

    class Meta: # noqa
        # template = "streams/question_scale.html"
        icon = "edit"
        label = "Question - Range Selection"


class QuestionMultipleChoiceBlock(blocks.StructBlock):
    """Select the name of your category"""
    question = blocks.CharBlock(max_length=500)
    mc_type = blocks.ChoiceBlock(label="Multiple Choice Question Type", choices=[('mc_radio','Radio (Select One)'),('mc_checkbox','Checkbox (Select Multiple)')], required=True)
    choice_1 = blocks.CharBlock(max_length=1000, label="Option 1")
    choice_2 = blocks.CharBlock(max_length=1000, label="Option 2")
    choice_3 = blocks.CharBlock(max_length=1000, label="Option 3", required=False)
    choice_4 = blocks.CharBlock(max_length=1000, label="Option 4", required=False)
    choice_5 = blocks.CharBlock(max_length=1000, label="Option 5", required=False)

    question_mandatory = blocks.BooleanBlock(label="Make this question mandatory?", default=True, required=False)

    class Meta: # noqa
        # template = "streams/question_multiple.html"
        icon = "edit"
        label = "Question - Multiple Choice"


class QuestionTextFieldBlock(blocks.StructBlock):
    """Questions with a rating or range answer"""
    question = blocks.CharBlock(max_length=1000)
    validation_type = blocks.ChoiceBlock(label="Field Type", choices=[('alpha_spaces','Text'),('email','Email'),('numeric','Phone'),('numeric','Number'),('date','Year')], default="alpha", required=True)

    question_mandatory = blocks.BooleanBlock(label="Make this question mandatory?", default=True, required=False)

    class Meta: # noqa
        # template = "streams/question_scale.html"
        icon = "edit"
        label = "Question - Text Field"











# class RecordBlock(blocks.StructBlock):
#     """Select the name of your category"""
#     record= blocks.CharBlock(max_length=250)

#     class Meta: # noqa
#         # template = "streams/category.html"
#         icon = "edit"
#         label = "Record"





# class QuestionMultipleChoiceBlock(blocks.StructBlock):
#     """Select the name of your category"""
#     question = blocks.CharBlock(max_length=500)
#     choice_1 = blocks.CharBlock(max_length=1000, label="Option 1")
#     choice_2 = blocks.CharBlock(max_length=1000, label="Option 2")
#     choice_3 = blocks.CharBlock(max_length=1000, label="Option 3", required=False)
#     choice_4 = blocks.CharBlock(max_length=1000, label="Option 4", required=False)
#     choice_5 = blocks.CharBlock(max_length=1000, label="Option 5", required=False)

#     class Meta: # noqa
#         # template = "streams/question_multiple.html"
#         icon = "edit"
#         label = "Question - Radio"


# class QuestionCheckChoicesBlock(blocks.StructBlock):
#     """Select the name of your category"""
#     question = blocks.CharBlock(max_length=500)
#     choice_1 = blocks.CharBlock(max_length=1000, label="Option 1")
#     choice_2 = blocks.CharBlock(max_length=1000, label="Option 2")
#     choice_3 = blocks.CharBlock(max_length=1000, label="Option 3", required=False)
#     choice_4 = blocks.CharBlock(max_length=1000, label="Option 4", required=False)
#     choice_5 = blocks.CharBlock(max_length=1000, label="Option 5", required=False)

#     class Meta: # noqa
#         # template = "streams/question_multiple.html"
#         icon = "edit"
#         label = "Question - Checkbox"


# class IntroBlock(blocks.StructBlock):
#     """Select the name of your category"""
#     title = blocks.CharBlock(max_length=250)
#     description = blocks.RichTextBlock()

#     class Meta: # noqa
#         # template = "streams/category.html"
#         icon = "edit"
#         label = "Intro"
 
# class TitleBlock(blocks.StructBlock):
#     """Select the name of your category"""
#     title = blocks.CharBlock(max_length=250)
#     description_p1 = blocks.CharBlock(max_length=1000, label="Description Paragraph 1", required=False)
#     description_p2 = blocks.CharBlock(max_length=1000, label="Description Paragraph 2", required=False)
#     description_p3 = blocks.CharBlock(max_length=1000, label="Description Paragraph 3", required=False)

#     class Meta: # noqa
#         # template = "streams/category.html"
#         icon = "edit"
#         label = "Title"

# class CategoryBlock(blocks.StructBlock):
#     """Select the name of your category"""
#     category= blocks.CharBlock(max_length=250)
#     description= blocks.CharBlock(max_length=1000)

#     class Meta: # noqa
#         # template = "streams/category.html"
#         icon = "edit"
#         label = "Category"