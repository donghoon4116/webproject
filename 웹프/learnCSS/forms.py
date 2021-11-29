from django import forms
from learnCSS.models import Html_content, Css_content


class HtmlForm(forms.ModelForm):
    class Meta:
        model = Html_content# 사용할 모델
        fields = [ 'html']  # QuestionForm에서 사용할 Question 모델의 속성               
        labels = {
            'html_content': 'html',
        }  
        
class CssForm(forms.ModelForm):
    class Meta:
        model = Css_content 
        fields = ['css']
        labels = {
            'css_content': 'css',
        }