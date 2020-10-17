from blog_post import BlogPost
from blog import Blog

blog = Blog()
blog_post_1 = BlogPost('Orsi', 'első', 'első', 'ma')
blog_post_2 = BlogPost('Geri', 'második', 'második', 'ma')
blog_post_3 = BlogPost('Ibi', 'harmadik', 'harmadik', 'ma')
blog.add(blog_post_1)
blog.add(blog_post_2)
blog.add(blog_post_3)
# print(blog)
# print(blog_post_2.cime)
blog_post_4 = BlogPost('Jozsi', 'negyedik', 'negyedik', 'ma')
blog.add(blog_post_4)
# print(len(blog.blog_posts))
# print(blog.blog_posts[3].cime)
# print(len(blog.blog_posts))
# blog.delete(4)
# print(len(blog.blog_posts))

blog.switch(blog_post_1,4)
print(blog.blog_posts[0].cime)