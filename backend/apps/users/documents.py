from django_elasticsearch_dsl import DocType, Index
from apps.users.models import User

# Name of the Elasticsearch index
user = Index('users')

# See Elasticsearch Indices API reference for available settings
user.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@user.doc_type
class UserDocument(DocType):
    class Meta:
        model = User

        fields = [
            'first_name',
            'last_name',
            'username',
            'profile_pic'
        ]
        ignore_signals = False
        auto_refresh = True