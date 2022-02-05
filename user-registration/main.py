from user import User
from post import Post
app_user_one = User("nnn@nnn.com", "Nana", "pwd", "DevOps engineer")  #
# Object for class
app_user_one.get_user_info()  # call function on variable

app_user_two = User("aaa@aaa.com", "Jon", "pwd1", "Agent")
app_user_two.get_user_info()

new_post = Post("on a secret mission today", app_user_two.name)
new_post.get_post_info()
