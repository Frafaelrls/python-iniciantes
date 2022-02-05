class User:  # blueprint
    def __init__(self, use_email, name, password, current_job_title):
        self.email = use_email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):  # function that belongs a class
        # is called "methods"
        self.password = new_password

    def change_job_title(self, new_job_title):  # "self" parameter used for
        # access data in all methods in one class
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"User {self.name} currently works as a {self.current_job_title}"
              f".You can contact them as {self.email} ")


