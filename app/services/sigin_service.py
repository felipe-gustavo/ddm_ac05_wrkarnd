from werkzeug.exceptions import BadRequest
from database import session


def signinService(dto):
    try:
        sql = """
                SELECT * FROM users
                WHERE
                    email = :email
                    AND password = :password
            """
        result = session.execute(sql, dto)
        user = result.mappings().first()

        if (user is None):
            raise BadRequest("invalid email or password")

        return {'id': user['id']}
    except Exception as err:
        print(err)
        raise BadRequest()
