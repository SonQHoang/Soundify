@posts.route('/new', methods=['GET', 'POST'])
def create_new_post():
    form = PostForm()
    form.author.choices = [(user.id, user.username) for user in User.query.all()]

    if form.validate_on_submit():
        selected_user = User.query.get(form.data["author"])

        audio_file = form.data['audio_file']
        audio_file.filename = get_unique_filename(audio_file.filename)
        upload = upload_file_to_s3(audio_file)

        if "url" not in upload:
            return {"errors": upload}

        new_post = Post(
            caption=form.data["caption"],
            audio_file=upload["url"],  # Update to the S3 URL returned by the upload function
            post_date=date.today(),
            user=selected_user
        )

        db.session.add(new_post)
        db.session.commit()

        return {"resPost": new_post.to_dict()}

    print(form.errors)
    return {"errors": form.errors}
