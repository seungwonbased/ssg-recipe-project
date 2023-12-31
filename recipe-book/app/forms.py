from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class PostForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목은 필수 입력 항목입니다.')])
    content = TextAreaField(
        '내용', validators=[DataRequired('내용은 필수 입력 항목입니다.')])


class CommentForm(FlaskForm):
    content = TextAreaField(
        '내용', validators=[DataRequired('내용은 필수 입력 항목입니다.')])


class UserCreateForm(FlaskForm):
    username = StringField('사용자 이름', validators=[
                           DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호 확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])


class UserLoginForm(FlaskForm):
    username = StringField('사용자 이름', validators=[
                           DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])


class FoodForm(FlaskForm):
    # food_name = SelectField('---------- 선택하세요 ----------', choices=[])
    food_name_1 = SelectField('---------- 선택하세요 ----------', choices=[])
    food_name_2 = SelectField('---------- 선택하세요 ----------', choices=[])
    food_name_3 = SelectField('---------- 선택하세요 ----------', choices=[])
    food_name_4 = SelectField('---------- 선택하세요 ----------', choices=[])
    food_unit = StringField('단위')
    quantity_1 = StringField('수량')
    quantity_2 = StringField('수량')
    quantity_3 = StringField('수량')
    quantity_4 = StringField('수량')
