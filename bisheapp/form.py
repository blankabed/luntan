from django.forms import ModelForm
from .models import user,rootuser,Announcement

class ArticleForm(ModelForm):  # 继承ModelForm类
  class Meta:
    model = user  # 具体要操作那个模型
    fields = ['user', 'password', 'phone','email'] # 允许编辑的字段
class ArticleForm2(ModelForm):  # 继承ModelForm类
  class Meta:
    model = rootuser  # 具体要操作那个模型
    fields = ['user', 'password'] # 允许编辑的字段
class ArticleForm3(ModelForm):  # 继承ModelForm类
  class Meta:
    model = Announcement  # 具体要操作那个模型
    fields = ['a_title', 'a_content'] # 允许编辑的字段
