import json
from io import BytesIO
import pdfkit
from django.core.files import File
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.template.loader import get_template
from records.models import UserRecord
from django.core.files.base import ContentFile

def design(cleaned_data):
    final_result = {}
    lifestyle_index = [2,3,4,5]
    lifestyle_result = 0

    for index in lifestyle_index:
        if isinstance(cleaned_data[index], list):
            count = len(cleaned_data[index])
            lifestyle_result += int(count)
        else:
            lifestyle_result += int(cleaned_data[index])
    
    legacy_index = [7,8,9]
    legacy_result = 0

    for index in legacy_index:
        if isinstance(cleaned_data[index], list):
            count = len(cleaned_data[index])
            legacy_result += int(count)
        else:
            legacy_result += int(cleaned_data[index])

    asset_index = [11,12,13,14]
    asset_result = 0
    for index in asset_index:
        if isinstance(cleaned_data[index], list):
            count = len(cleaned_data[index])
            asset_result += int(count)
        else:
            asset_result += int(cleaned_data[index])
    try:
        final_result['design_lifestyle_result'] = lifestyle_result
        final_result['design_legacy_result'] = legacy_result
        final_result['design_asset_result'] = asset_result
    except:
        pass
    return final_result

def foundation(cleaned_data):
    final_result = {}
    plans_index = [17,18,19,20,21]
    plans_result = 0

    for index in plans_index:
        if isinstance(cleaned_data[index], list):
            count = len(cleaned_data[index])
            plans_result += int(count)
        else:
            plans_result += int(cleaned_data[index])
    
    governance_index = [23,24,25,26]
    governance_result = 0

    for index in governance_index:
        if isinstance(cleaned_data[index], list):
            count = len(cleaned_data[index])
            governance_result += int(count)
        else:
            governance_result += int(cleaned_data[index])

    team_index = [28,29,30]
    team_result = 0
    for index in team_index:
        if isinstance(cleaned_data[index], list):
            count = len(cleaned_data[index])
            team_result += int(count)
        else:
            team_result += int(cleaned_data[index])
    try:
        final_result['foundation_plans_result'] = plans_result
        final_result['foundation_governance_result'] = governance_result
        final_result['foundation_team_result'] = team_result
    except:
        pass
    return final_result

def build(cleaned_data):
    final_result = {}
    risk_wise_index = [33,34,35,36]
    risk_wise_result = 0

    for index in risk_wise_index:
        if isinstance(cleaned_data[index], list):
            count = len(cleaned_data[index])
            risk_wise_result += int(count)
        else:
            risk_wise_result += int(cleaned_data[index])
    
    task_wise_index = [38,39,40,41]
    task_wise_result = 0

    for index in task_wise_index:
        if isinstance(cleaned_data[index], list):
            count = len(cleaned_data[index])
            task_wise_result += int(count)
        else:
            task_wise_result += int(cleaned_data[index])

    cash_wise_index = [43,44,45,46,47]
    cash_wise_result = 0
    for index in cash_wise_index:
        if isinstance(cleaned_data[index], list):
            count = len(cleaned_data[index])
            cash_wise_result += int(count)
        else:
            cash_wise_result += int(cleaned_data[index])
    try:
        final_result['build_risk_wise_result'] = risk_wise_result
        final_result['build_task_wise_result'] = task_wise_result
        final_result['build_cash_wise_result'] = cash_wise_result
    except:
        pass
    return final_result

@csrf_exempt
def process_data(request):
    if request.method == 'POST':
        result = json.loads(request.body)
        print(result)
        # ENABLE THIS FOR TEST DATA
#         result = {'welcome': 'read', 
# 'Design': 'read', 
#     'Lifestyle': 'read', 
#         'To what level is your business able to run without you?': '5', 
#         'How stable and sustainable is your lifestyle spending?': '4', 
#         'How prepared are you financially for retirement?': '5', 
#         'Have you done the work to plan your lifestyle needs into retirement (or when you have moved into a work-optional lifestyle).': '1', 
#     'Legacy': 'read', 
#         'Do you have a clear definition of what success looks like for your business?': '5', 
#         'How do you intend that the wealth and experience you are creating will benefit your community and your family? Check all that apply': ['I see myself in the future mentoring young entrepreneurs', 'I would like to create an endowment to a college or hospital in the community'], 
#         'Who has been involved in helping with your legacy planning to date?': ['Lawyer', 'Accountant'], 
#     'Asset': 'read', 
#         'Do you have a clear understanding of the valuation drivers for business in your industry?': '2', 
#         'Are you confident with the method of creating a valuation for your business?': '4', 
#         'Is your business is on track to achieve the valuation it is capable of?': '4', 
#         'How far has your business grown toward becoming an asset?': '4', 
# 'Foundation': 'read', 
#     'Plans': 'read', 
#         'Is your existing corporate structure appropriate to your current levels of success?': '2', 
#         'Beyond being employees, have your immediate family members been incorporated into your tax planning?': '4', 
#         'How prepared are you in exit planning for your business?': '2', 
#         'How comprehensive is your current financial plan?': '4', 
#         'I and my immediate family own the following percentage of my company:': '2', 
#     'Governance': 'read', 
#         'Do you have one person designated (yourself or a senior partner) as the "person responsible" for business oversight and effective communication with your team of advisors?': '2', 
#         'How relevant and impactful is your financial plan?': '2', 
#         'Do you measure and evaluate the implementation of my plan?': '2', 
#         'How well do you understand and value the process and discipline of a written plan?': '2', 
#     'Team': 'read', 
#         'How important is your team of lawyer, account, wealth strategist etc?': '2', 
#         "What is your ongoing ability to rely on this team's expertise?": '4', 
#         'Beyond the one or two year financial window, do you have members of your team working on the long view of leveraging the wealth generated by your business?': '4', 
# 'Build': 'read', 
#     'Risk Wise': 'read', 
#         'When contemplating exit scenarios have you considered involuntary eventualities such as illness, disability or death?': '4', 
#         'How often do you re-assess your current risk?': '4', 
#         'How would you rate your understanding of where you and your household stand related to risk and return?': '5', 
#         'I have the following  diversification of my wealth in choose (all that apply): not diversified, ecompassing 5-8 classes. Checklist of asset types 4 choices of real estate, 3 choices private equity, 3 types of insurance, stocks and bonds 3 types GICs etc': '4',
#     'Tax Wise': 'read', 
#         'Have you considered or implemented one or more of the following: holding company, family trust, real estate corporation, estate freeze.': '4', 
#         'What is your approach to tax management?': '4', 
#         'Are your affairs are set up to ensure you are able to take advantage of the Lifetime Capital Gains Exemption (LCGE)?': '5', 
#         'How well does your current tax planning prepare for the transition of your business valuation into your personal finances?': '1', 
#     'Cash Wise': 'read', 
#         'What is your current level of business cash?': '5', 
#         'What is your strategy for using any cash in excess of current needs?': '5', 
#         'How easy is it for you to articulate your plan for funding your retirement?': '5', 
#         'What is your strategy for investing?': '4', 
#          'As you worked through the questionnaire which of these nine pillars did you feel were most urgent?': '5'}
#         print(result, "DATA FROM FRONTEND")
        name = result['Name']
        email = result['Email']
        business_name = result['Business Name']
        year_of_incorp = result['Years of Incorporation']
        age = result['Age']
        marital_status = result['Marital Status']
        number_of_children = result['Number of Children']
        phone = result['Phone']
        user_record = UserRecord(name=name, 
            email=email, business_name=business_name, marital_status=marital_status,
            year_of_incorp=year_of_incorp, age=age, number_of_children=number_of_children,
            phone=phone, data=result)

 
        # result.pop('welcome')
        result.pop('Name')
        result.pop('Email')
        result.pop('Business Name')
        result.pop('Years of Incorporation')
        result.pop('Age')
        result.pop('Marital Status')
        result.pop('Number of Children')
        result.pop('Phone')

        cleaned_data = list(result.values())
        overall_result_dict = {}
        pdf_data = {}

        overall_result_dict = design(cleaned_data)
        overall_result_dict.update(foundation(cleaned_data))
        overall_result_dict.update(build(cleaned_data))

        for_process_to_pdf = sorted(overall_result_dict.items(), key=lambda item: item[1])

        for key, value in for_process_to_pdf[0:3]:
            pdf_data[key] = value
        
        template = get_template('pdf.html')
        html = template.render({'data': pdf_data})
        options = {
            'page-size': 'Letter',
            'encoding': "UTF-8",
        }
        pdf = pdfkit.from_string(html, False, options)
        filename = 'podium.pdf'
        content = ContentFile(pdf)
        user_record.pdf.save(filename, content)

        response = HttpResponse(pdf,content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="podium.pdf"'
        stuff = JsonResponse({'data': pdf_data}, safe=False)
        print(JsonResponse({'data': pdf_data}, safe=False), "JSON DATA")
        
        return stuff
