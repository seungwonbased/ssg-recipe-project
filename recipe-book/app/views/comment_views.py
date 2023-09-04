from datetime import datetime
from flask import Blueprint, url_for, request, render_template, g, flash
from werkzeug.utils import redirect
from app import db
from app.forms import CommentForm
from app.models import Post, Comment
from app.views.auth_views import login_required


bp = Blueprint('comment', __name__, url_prefix='/comment')


@bp.route('/create/<int:post_id>', methods=('POST',))
@login_required
def create(post_id):

    form = CommentForm()
    post = Post.query.get_or_404(post_id)
    if form.validate_on_submit():
        content = request.form['content']
        comment = Comment(
            content=content, create_date=datetime.now(), user=g.user)
        post.comment_set.append(comment)
        db.session.commit()
        return redirect('{}#comment_{}'.format(
            url_for('post.detail', post_id=post_id), comment.id))
    return render_template('post/post_detail.html', post=post, form=form)


@bp.route('/modify/<int:comment_id>', methods=('GET', 'POST'))
@login_required
def modify(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if g.user != comment.user:
        flash('수정 권한이 없습니다')
        return redirect(url_for('post.detail', post_id=comment.post.id))
    if request.method == "POST":
        form = CommentForm()
        if form.validate_on_submit():
            form.populate_obj(comment)
            comment.modify_date = datetime.now()  # 수정 일시 저장
            db.session.commit()
            return redirect('{}#comment_{}'.format(
                url_for('post.detail', post_id=comment.post.id), comment.id))
    else:
        form = CommentForm(obj=comment)
    return render_template('comment/comment_form.html', form=form)


@bp.route('/delete/<int:comment_id>')
@login_required
def delete(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    post_id = comment.post.id
    if g.user != comment.user:
        flash('삭제 권한이 없습니다')
    else:
        db.session.delete(comment)
        db.session.commit()
    return redirect(url_for('post.detail', post_id=post_id))


@bp.route('/like/<int:comment_id>/')
@login_required
def like(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if g.user == comment.user:
        flash('자신이 작성한 댓글에는 좋아요를 누를 수 없어요')
    else:
        comment.liker.append(g.user)
        db.session.commit()
    return redirect('{}#comment_{}'.format(
        url_for('post.detail', post_id=comment.post.id), comment.id))
