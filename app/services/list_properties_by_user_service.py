from flask import jsonify
from database import session


def listPropertiesByUserService(userId):
    sql = """
            SELECT * FROM properties
            WHERE userId = :userId
        """
    result = session.execute(sql, {"userId": userId})

    return jsonify([
        dict(row)
        for row in result.mappings().all()
    ])
