from werkzeug.exceptions import BadRequest
from database import session


def signupService(dto):
    try:
        sql = """
            INSERT INTO users (name, email, password) VALUES (:name, :email, :password)
        """
        session.execute(sql, dto)
        session.commit()
        return ''
    except Exception as err:
        print(err)
        raise BadRequest()
