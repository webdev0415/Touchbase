from . import models

def is_hash_taken(hash):
    return True if models.ToushLink.objects.filter(short_url=hash).exists() else False