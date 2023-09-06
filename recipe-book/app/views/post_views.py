from datetime import datetime
from flask import Blueprint, render_template, request, url_for, g, flash
from werkzeug.utils import redirect
from app import db
from app.models import Post, Comment, User, Food, Image
from app.forms import PostForm, CommentForm, FoodForm
from app.views.auth_views import login_required
import math
# from app.kamis import kamis_api


bp = Blueprint('post', __name__, url_prefix='/post')
# food_data = kamis_api.get_food()


@bp.route('/list/')
def _list():
    page = request.args.get('page', type=int, default=1)
    kw = request.args.get('kw', type=str, default='')
    post_list = Post.query.order_by(Post.create_date.desc())
    if kw:
        search = '%%{}%%'.format(kw)
        sub_query = db.session.query(Comment.post_id, Comment.content, User.username) \
            .join(User, Comment.user_id == User.id).subquery()
        post_list = post_list \
            .join(User).outerjoin(sub_query, sub_query.c.post_id == Post.id).filter(Post.subject.ilike(search) |  # 질문 제목
                                                                                    # 질문 내용
                                                                                    Post.content.ilike(search) |
                                                                                    # 질문 작성자
                                                                                    User.username.ilike(search) |
                                                                                    # 답변 내용
                                                                                    sub_query.c.content.ilike(search) |
                                                                                    sub_query.c.username.ilike(
                                                                                        search)  # 답변 작성자
                                                                                    ) \
            .distinct()
    post_list = post_list.paginate(page=page, per_page=10)
    return render_template('post/post_list.html', post_list=post_list, page=page, kw=kw)


@bp.route('/detail/<int:post_id>/')
def detail(post_id):

    form = CommentForm()
    post = Post.query.get_or_404(post_id)
    return render_template('post/post_detail.html', post=post, form=form)


@bp.route('/create/', methods=('GET', 'POST'))
@login_required
def create():
    form = PostForm()
    foods = db.session.query(Food).all()
    food = FoodForm()

    if request.method == 'POST' and form.validate_on_submit():
        post = Post(subject=form.subject.data,
                    content=form.content.data, create_date=datetime.now(), user=g.user)

        post.price = calculate(food)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('post._list'))

    return render_template('post/post_form.html', form=form, food=food, foods=foods)


@bp.route('/modify/<int:post_id>', methods=('GET', 'POST'))
@login_required
def modify(post_id):
    post = Post.query.get_or_404(post_id)
    food = FoodForm()
    if g.user != post.user:
        flash('수정 권한이 없습니다')
        return redirect(url_for('post.detail', post_id=post_id))
    if request.method == 'POST':  # POST 요청
        form = PostForm()
        if form.validate_on_submit():
            form.populate_obj(post)
            post.modify_date = datetime.now()  # 수정 일시 저장
            db.session.commit()
            return redirect(url_for('post.detail', post_id=post_id))
    else:  # GET 요청
        form = PostForm(obj=post)
    return render_template('post/post_form.html', form=form, food=food)


@bp.route('/delete/<int:post_id>')
@login_required
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    if g.user != post.user:
        flash('삭제 권한이 없습니다')
        return redirect(url_for('post.detail', post_id=post_id))
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('post._list'))


@bp.route('/like/<int:post_id>/')
@login_required
def like(post_id):
    _post = Post.query.get_or_404(post_id)
    if g.user == _post.user:
        flash('자신이 작성한 글에는 좋아요를 누를 수 없어요')
    else:
        _post.liker.append(g.user)
        db.session.commit()
    return redirect(url_for('post.detail', post_id=post_id))


# def upload_file(req):
#     if 'file' not in req.files:
#         print("no file part")
#         return 'No file part'
#     file = req.files['file']

#     if file.filename == '':
#         return 'No selected file'
#     # filename = secure_filename(file.filename)

#     filepath = os.path.join("", filename)
#     file.save(filepath)

#     new_image = Image(filename=filepath)
#     db.session.add(new_image)
#     try:
#         db.session.commit()
#     except Exception as e:
#         print(e)
#         return "There was an issue uploading your image."

#     return redirect(url_for('post._list'))


def calculate(food):
    food_1 = db.session.query(Food).filter(
        Food.foodname == food.food_name_1.data).first()
    food_2 = db.session.query(Food).filter(
        Food.foodname == food.food_name_2.data).first()
    food_3 = db.session.query(Food).filter(
        Food.foodname == food.food_name_3.data).first()
    food_4 = db.session.query(Food).filter(
        Food.foodname == food.food_name_4.data).first()

    if food_1 is None:
        price_1, unit_1, quantity_1 = 0, 1, 0
    else:
        price_1, unit_1, quantity_1 = food_1.food_price, food_1.food_unit, food.quantity_1.data
    if food_2 is None:
        price_2, unit_2, quantity_2 = 0, 1, 0
    else:
        price_2, unit_2, quantity_2 = food_2.food_price, food_2.food_unit, food.quantity_2.data
    if food_3 is None:
        price_3, unit_3, quantity_3 = 0, 1, 0
    else:
        price_3, unit_3, quantity_3 = food_3.food_price, food_3.food_unit, food.quantity_3.data
    if food_4 is None:
        price_4, unit_4, quantity_4 = 0, 1, 0
    else:
        price_4, unit_4, quantity_4 = food_4.food_price, food_4.food_unit, food.quantity_4.data

    print(price_1, unit_1, quantity_1)
    print(price_2, unit_2, quantity_2)
    print(price_3, unit_3, quantity_3)
    print(price_4, unit_4, quantity_4)

    price = math.floor(((int(price_1) * int(quantity_1) / int(unit_1)) + (int(price_2) * int(quantity_2) / int(unit_2)) +
                        (int(price_3) * int(quantity_3) / int(unit_3)) + (int(price_4) * int(quantity_4) / int(unit_4))))

    return price
