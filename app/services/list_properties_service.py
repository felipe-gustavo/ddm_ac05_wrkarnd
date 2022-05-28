from flask import jsonify
from database import session


def listPropertiesService():
    sql = """
            SELECT * FROM properties
        """
    result = session.execute(sql)

    return jsonify([
        dict(row)
        for row in result.mappings().all()
    ])
