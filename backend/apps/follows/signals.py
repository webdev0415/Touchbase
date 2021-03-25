from django.dispatch import Signal

follower_created = Signal(providing_args=['follower'])
follower_removed = Signal(providing_args=['follower'])
followee_created = Signal(providing_args=['followee'])
followee_removed = Signal(providing_args=['followee'])
following_created = Signal(providing_args=['following'])
following_removed = Signal(providing_args=['following'])