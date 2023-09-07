# from flask import Blueprint
# from ..models import User

# users = Blueprint('users', __name__)

# @users.route("/all")
# def get_all_users():
#     response = [user.to_dict() for user in User.query.all()]
#     print(response)
#     return {"users": response }


# # Use this whenever we're sending a body along so that CSRF is always attached
# # form["csrf_token'].data = request.cookies[csrf_token]
# # Before form.validateon_submit()