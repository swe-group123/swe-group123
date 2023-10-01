from App.models import Admin, RegularUser, Author
from App.database import db

def get_author(author_id):
    return Author.query.get(author_id)

def get_publications_by_author(author_id):
    author = get_author(author_id)
    
    if not author:
        return None

    author_info = {
        'author_id': author.author_id,
        'Name': f"{author.title} {author.first_name} {author.last_name}",
    }

    if author.publications:
        publications = [{'title': pub.title, 'publication_date': pub.publication_date} for pub in author.publications]
        author_info['Publications'] = publications
    else:
        author_info['Publications'] = 'No Publications.'

    return [author_info]
  
def create_author(admin_id, uwi_id, title, first_name, last_name, password):
    admin = Admin.query.get(admin_id)
    
    if admin:
        return admin.create_author(uwi_id, title, first_name, last_name, password)
    return None

