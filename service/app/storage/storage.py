from typing import Optional

from sqlalchemy.orm import Session
from .database import initialize_storage_development_mode
from .entity import User, Project, Technology


class Storage():
    def __init__(self):
        initialize_storage_development_mode()


    def get_uset_with_id(self, id: int, session: Session) -> Optional[User]:
        return session.query(User).filter(User.id == id).first()

    def get_uset_with_email(self, email: str, session: Session) -> Optional[User]:
        return session.query(User).filter(User.email == email).first()

    def add_user_entity(self, user, session: Session) -> User:
        new_user = User(username=user.username, name=user.name,  email=user.email, github_url = user.github_url,
                        linkedin_url=user.linkedin_url, oauth=user.oauth_token)
        session.add(new_user)
        return new_user

    def add_project_entity(self, project, session: Session):
        new_user = Project(title=project.title, description=project.description, start_date=project.start_date,
                           stars=project.stars, url=project.url)
        session.add(new_user)
        return new_user