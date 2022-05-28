from werkzeug.exceptions import NotFound
from database import session


def getPropertyByIdService(propertyId):
    sql = """
            SELECT * FROM properties
            WHERE id = :id
        """
    result = session.execute(sql, {"id": propertyId})
    rproperty = result.mappings().first()

    if rproperty is None:
        raise NotFound("Property not found")

    return dict(rproperty)
