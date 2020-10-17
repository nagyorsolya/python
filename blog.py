class Blog:
  def __init__(self):
    self.blog_posts = []
  def add(self, blog_post):
    self.blog_posts.append(blog_post)
  def delete(self, index):
    del self.blog_posts[index-1]
  def switch(self, blog_post, index):
    index_of_original = self.blog_posts.index(blog_post)
    temp = self.blog_posts[index_of_original]
    self.blog_posts[index_of_original] = self.blog_posts[index-1]
    self.blog_posts[index-1] = temp