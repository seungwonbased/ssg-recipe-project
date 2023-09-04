from datetime import datetime
from flask import Blueprint, render_template, request, url_for, g, flash
from werkzeug.utils import redirect
from app import db
from app.models import Post, Comment, User
from app.forms import PostForm, CommentForm
from app.views.auth_views import login_required


bp = Blueprint('post', __name__, url_prefix='/post')


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
            .join(User).outerjoin(sub_query, sub_query.c.post_id == Post.id).filter(Post.subject.ilike(search) |  # 질문제목
                                                                                    # 질문내용
                                                                                    Post.content.ilike(search) |
                                                                                    # 질문작성자
                                                                                    User.username.ilike(search) |
                                                                                    # 답변내용
                                                                                    sub_query.c.content.ilike(search) |
                                                                                    sub_query.c.username.ilike(
                                                                                        search)  # 답변작성자
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

    if request.method == 'POST' and form.validate_on_submit():
        post = Post(subject=form.subject.data,
                    content=form.content.data, create_date=datetime.now(), user=g.user)

        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('post/post_form.html', form=form)


@bp.route('/modify/<int:post_id>', methods=('GET', 'POST'))
@login_required
def modify(post_id):
    post = Post.query.get_or_404(post_id)
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
    return render_template('post/post_form.html', form=form)


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
