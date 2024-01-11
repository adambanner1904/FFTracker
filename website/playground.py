from models import Club
from website import db

club = Club(name='DY Athletic')
db.session.add(club)
db.session.commit()
print('DY created')
