from blog import Blog

MENU_PROMPT = "Enter 'c' to create blog, 'l' to list blogs, 'r' to read one, 'p' to create post or 'q' to quit: "
POST_TEMPLATE = """--- {} --- 

    {}
    
    """
blogs = dict()


def menu():
    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != "q":
        if selection == "c":
            ask_create_blog()
        elif selection == "l":
            print_blogs()
        elif selection == "r":
            ask_read_blog()
        elif selection == "p":
            ask_create_post()
        selection = input(MENU_PROMPT)


def print_blogs():
    for key, blog in blogs.items():
        print(f"- {blog}")


def ask_create_blog():
    blog_title = input("Enter your blog title:")
    blog_author = input("Enter your name: ")
    blogs[blog_title] = Blog(blog_title, blog_author)


def ask_read_blog():
    blog_title = input("Blog title:")
    print_posts(blogs[blog_title])


def print_posts(blog):
    for post in blog.posts:
        print_post(post)


def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))


def ask_create_post():
    blog_title = input("Enter blog title:")
    post_title = input("Enter post title: ")
    post_content = input("Enter post content: ")

    blogs[blog_title].create_post(post_title, post_content)
