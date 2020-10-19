from flask import render_template, redirect, flash, url_for, Blueprint, request, abort
from puppyblog.blog_posts.forms import BlogPostForm
from flask_login import login_required, current_user
from puppyblog.models import BlogPost
from puppyblog import db

blog_posts = Blueprint("blog_posts", __name__)


@blog_posts.route("/blog_posts", methods=["POST", "GET"])
@login_required
def create_blog_post():
    form = BlogPostForm()
    if form.validate_on_submit():
        blog_post = BlogPost(title=form.title.data, body=form.body.data, user_id=current_user.id)
        db.session.add(blog_post)
        db.session.commit()
        flash("your post has been sent!")
        return redirect(url_for("core.index"))
    return render_template("create_post.html", form=form)


@blog_posts.route("/<int:blog_post_id>")
def view(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    return render_template("blog_post.html", title=blog_post.title, date=blog_post.date, post=blog_post)


@blog_posts.route("/<int:blog_post_id>/update", methods=["POST", "GET"])
@login_required
def update(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    if blog_post.user_id != current_user.id:
        abort(403)
    form = BlogPostForm()
    if form.validate_on_submit():
        blog_post.title = form.title.data
        blog_post.body = form.body.data
        db.session.commit()
        flash("your post has been updated")
        return redirect(url_for("blog_posts.view", blog_post_id=blog_post_id))
    elif request.method == "GET":
        form.title.data = blog_post.title
        form.body.data = blog_post.body
    return render_template("create_post.html", form=form)


@blog_posts.route("/<int:blog_post_id>/delete", methods=["POST", "GET"])
@login_required
def delete(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    if blog_post.user_id != current_user.id:
        abort(403)
    db.session.delete(blog_post)
    db.session.commit()
    flash("your post has been deleted")
    return redirect(url_for("core.index", blog_post_id=blog_post_id))
