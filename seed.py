import random
from werkzeug.security import generate_password_hash
from app import create_app
from models import db, Todo, User

app = create_app()
random.seed(42)

with app.app_context():
    db.drop_all()
    db.create_all()
    for number in range(1, 21):
        user = User(username=f"demo{number}", password_hash=generate_password_hash("demo"))
        db.session.add(user)
        db.session.flush()
        for index in range(random.randint(5, 10)):
            db.session.add(Todo(
                user_id=user.id,
                title=f"Demo todo {index + 1} for {user.username}",
                priority=random.randint(1, 5),
                completed=random.choice([False, False, True]),
            ))
    db.session.commit()
    print("Seeded 20 demo users (password: demo) with 5–10 todos each.")
