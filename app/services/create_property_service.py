from werkzeug.exceptions import BadRequest
from database import session


def createPropertyService(userId, dto):
    try:
        sql = """
            INSERT INTO properties (
                img,
                userId,
                title,
                description,
                rendValue,
                buyValue,
                IPTU,
                townhouseValue,
                propertyOptionals
            ) VALUES (
                :img,
                :userId,
                :title,
                :description,
                :rendValue,
                :buyValue,
                :IPTU,
                :townhouseValue,
                :propertyOptionals
            )
        """
        session.execute(sql, {**dto, "userId": userId})
        session.commit()
        return ''
    except Exception as err:
        print(err)
        raise BadRequest()
