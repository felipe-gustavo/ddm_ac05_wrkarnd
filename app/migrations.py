from database import session


def createUserTable():
    sql = """
    CREATE TABLE IF NOT EXISTS users (
        id int not null auto_increment primary key,
        name varchar(200),
        email varchar(200),
        password varchar(200)
    );
    """
    session.execute(sql)
    session.commit()


def createPropertyTable():
    sql = """
    CREATE TABLE IF NOT EXISTS properties (
        id int not null auto_increment primary key,
        userId int,
        img varchar(200),
        title varchar(200),
        description varchar(200),
        rendValue varchar(200),
        buyValue varchar(200),
        IPTU  varchar(200),
        townhouseValue  varchar(200),
        propertyOptionals varchar(200)
    );
    """
    session.execute(sql)
    session.commit()


def __main__():
    createUserTable()
    createPropertyTable()


__main__()
