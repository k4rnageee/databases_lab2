import psycopg2
from config import host, user, password, db_name
from dateutil.parser import parse


def is_date(string, fuzzy=False):
    try:
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False


try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

    connection.autocommit = True

    while True:
        print("SELECT OPTION:")
        print("1. VIEW DATA")
        print("2. JOIN DATA")
        print("3. INSERT DATA")
        print("4. UPDATE DATA")
        print("5. DELETE DATA")
        print("6. DELETE FULL TABLE")
        print("7. RANDOM DATA")
        print("8. SEARCH DATA")
        print("9. EXIT")
        choice = input()

        while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7" and choice != "8" and choice != "9":
            print("SELECT CORRECT OPTION:")
            choice = input()

        if choice == "1":
            print("SELECT VIEW OPTION:")
            print("1. VIEW USER TABLE")
            print("2. VIEW SONG TABLE")
            print("3. VIEW ARTIST TABLE")
            print("4. VIEW LABEL TABLE")
            print("5. VIEW USER/SONG TABLE")
            print("6. VIEW ARTIST/SONG TABLE")
            print("7. VIEW LABEL/ARTIST TABLE")
            choice1 = input()
            while choice1 != "1" and choice1 != "2" and choice1 != "3" and choice1 != "4" and choice1 != "5" and choice1 != "6" and choice1 != "7":
                print("SELECT RIGHT OPTION")
                choice1 = input()

            if choice1 == "1":
                with connection.cursor() as cursor:
                    cursor.execute(
                        """SELECT * from "User";"""
                    )
                    dataInfo = cursor.fetchall()
                    for row in dataInfo:
                        print("user_ID = ", row[0])
                        print("nickname = ", row[1])
                        print("reg_date = ", row[2])
                        print("saved_songs = ", row[3])
                        print("subscription_type = ", row[4], "\n")

            if choice1 == "2":
                with connection.cursor() as cursor:
                    cursor.execute(
                        """SELECT * from "Song";"""
                    )
                    dataInfo = cursor.fetchall()
                    for row in dataInfo:
                        print("song_ID = ", row[0])
                        print("name = ", row[1])
                        print("auditions = ", row[2])
                        print("release_date = ", row[3], "\n")

            if choice1 == "3":
                with connection.cursor() as cursor:
                    cursor.execute(
                        """SELECT * from "Artist";"""
                    )
                    dataInfo = cursor.fetchall()
                    for row in dataInfo:
                        print("artist_ID = ", row[0])
                        print("name = ", row[1])
                        print("full_name = ", row[2])
                        print("age = ", row[3], "\n")

            if choice1 == "4":
                with connection.cursor() as cursor:
                    cursor.execute(
                        """SELECT * from "Label";"""
                    )
                    dataInfo = cursor.fetchall()
                    for row in dataInfo:
                        print("name = ", row[0])
                        print("creation_date = ", row[1])
                        print("country = ", row[2], "\n")

            if choice1 == "5":
                with connection.cursor() as cursor:
                    cursor.execute(
                        """SELECT * from "User/Song";"""
                    )
                    dataInfo = cursor.fetchall()
                    for row in dataInfo:
                        print("user_ID = ", row[0])
                        print("song_ID = ", row[1], "\n")

            if choice1 == "6":
                with connection.cursor() as cursor:
                    cursor.execute(
                        """SELECT * from "Artist/Song";"""
                    )
                    dataInfo = cursor.fetchall()
                    for row in dataInfo:
                        print("artist_ID = ", row[0])
                        print("song_ID = ", row[1], "\n")

            if choice1 == "7":
                with connection.cursor() as cursor:
                    cursor.execute(
                        """SELECT * from "Label/Artist";"""
                    )
                    dataInfo = cursor.fetchall()
                    for row in dataInfo:
                        print("label_name = ", row[0])
                        print("artist_ID = ", row[1], "\n")

        elif choice == "2":
            print("SELECT JOIN OPTION:")
            print("1. JOIN USER/SONG")
            print("2. JOIN ARTIST/SONG")
            print("3. JOIN LABEL/SONG")
            choice2 = input()
            while choice2 != "1" and choice2 != "2" and choice2 != "3":
                print("SELECT RIGHT OPTION")
                choice2 = input()

            if choice2 == "1":
                with connection.cursor() as cursor:
                    cursor.execute(
                        """SELECT q1."user_ID", nickname, reg_date, saved_songs, subscription_type, q1."song_ID", s.name,
                         auditions, release_date from 
                        (SELECT u."user_ID", nickname, reg_date, saved_songs, subscription_type, us."song_ID"
                        from "User/Song" as us INNER JOIN "User" as u on us."user_ID"=u."user_ID") q1
                        INNER JOIN "Song" as s on s."song_ID"=q1."song_ID";"""
                    )
                    dataInfo = cursor.fetchall()
                    for row in dataInfo:
                        print("user_ID = ", row[0])
                        print("nickname = ", row[1])
                        print("reg_date = ", row[2])
                        print("saved_songs = ", row[3])
                        print("subscription_type = ", row[4])
                        print("song_ID = ", row[5])
                        print("name = ", row[6])
                        print("auditions = ", row[7])
                        print("release_date = ", row[8], "\n")

            if choice2 == "2":
                with connection.cursor() as cursor:
                    cursor.execute(
                        """SELECT q1."artist_ID", q1.name, q1."full_name", age, songs_amount, q1."song_ID", s.name, auditions, 
                        release_date 
                        FROM
                        (SELECT "a"."artist_ID", "a"."name", "a".full_name, "a".age, "a"."songs_amount", "as"."song_ID"
                        from "Artist/Song" as "as" INNER JOIN "Artist" as "a" on "a"."artist_ID"="as"."artist_ID") q1
                        INNER JOIN "Song" as s on q1."song_ID"=s."song_ID";"""
                    )
                    dataInfo = cursor.fetchall()
                    for row in dataInfo:
                        print("artist_ID = ", row[0])
                        print("name = ", row[1])
                        print("full_name = ", row[2])
                        print("age = ", row[3])
                        print("songs_amount = ", row[4])
                        print("song_ID = ", row[5])
                        print("name = ", row[6])
                        print("auditions = ", row[7])
                        print("release_date = ", row[8], "\n")

            if choice2 == "3":
                with connection.cursor() as cursor:
                    cursor.execute(
                        """SELECT "label_name", "creation_date", country, "a"."artist_ID", "a".name, "full_name", age, 
                        "songs_amount" from
                        (SELECT la."label_name", "artist_ID", "creation_date", country from
                        "Label/Artist" as la INNER JOIN "Label" as l on
                        la."label_name" = l.name) q1
                        INNER JOIN "Artist" as "a" on "a"."artist_ID" = q1."artist_ID";"""
                    )
                    dataInfo = cursor.fetchall()
                    for row in dataInfo:
                        print("label_name = ", row[0])
                        print("creation_date = ", row[1])
                        print("country = ", row[2])
                        print("artist_ID = ", row[3])
                        print("name = ", row[4])
                        print("full_name = ", row[5])
                        print("age = ", row[6])
                        print("songs_amount = ", row[7], "\n")

        elif choice == "3":
            print("SELECT INSERT OPTION:")
            print("1. INSERT DATA INTO USER TABLE")
            print("2. INSERT DATA INTO ARTIST TABLE")
            print("3. INSERT DATA INTO SONG TABLE")
            print("4. INSERT DATA INTO LABEL TABLE")
            print("5. INSERT DATA INTO USER/SONG TABLE")
            print("6. INSERT DATA INTO ARTIST/SONG TABLE")
            print("7. INSERT DATA INTO LABEL/ARTIST TABLE")

            choice3 = input()
            while choice3 != "1" and choice3 != "2" and choice3 != "3" and choice3 != "4" and choice3 != "5" and choice3 != "6" and choice3 != "7":
                print("SELECT RIGHT OPTION")
                choice3 = input()

            if choice3 == "1":
                print("ENTER DATA")
                print("user_ID = ")
                user_ID_input = input()
                while not user_ID_input.isnumeric():
                    print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                    user_ID_input = input()
                print("nickname = ")
                nickname_input = input()
                print("reg_date = ")
                reg_date_input = input()
                while not is_date(reg_date_input, True):
                    print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                    reg_date_input = input()
                print("saved_songs = ")
                saved_songs_input = input()
                while not saved_songs_input.isnumeric():
                    print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                    saved_songs_input = input()
                print("subscription_type = ")
                subscription_type_input = input()
                while subscription_type_input != "free" and subscription_type_input != "premium" and subscription_type_input != "family":
                    print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                    subscription_type_input = input()
                fullQuery = f"{user_ID_input}, \'{nickname_input}\', \'{reg_date_input}\', {saved_songs_input}, \'{subscription_type_input}\'"

                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO \"User\" (\"user_ID\", nickname, \"reg_date\", \"saved_songs\", \"subscription_type\") VALUES (" + fullQuery + ");"
                    )

            if choice3 == "2":
                print("ENTER DATA")
                print("artist_ID = ")
                artist_ID_input = input()
                while not artist_ID_input.isnumeric():
                    print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                    artist_ID_input = input()
                print("name = ")
                name_input = input()
                print("full_name = ")
                full_name_input = input()
                print("age = ")
                age_input = input()
                while not age_input.isnumeric():
                    print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                    age_input = input()
                print("songs_amount = ")
                songs_amount_input = input()
                while not songs_amount_input.isnumeric():
                    print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                    songs_amount_input = input()
                fullQuery = f"{artist_ID_input}, \'{name_input}\', \'{full_name_input}\', {age_input}, {songs_amount_input}"

                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO \"Artist\" (\"artist_ID\", \"name\", \"full_name\", age, \"songs_amount\") VALUES (" + fullQuery + ");"
                    )

            if choice3 == "3":
                print("ENTER DATA")
                print("song_ID = ")
                song_ID_input = input()
                while not song_ID_input.isnumeric():
                    print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                    song_ID_input = input()
                print("name = ")
                name_input = input()
                print("auditions = ")
                auditions_input = input()
                while not auditions_input.isnumeric():
                    print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                    auditions_input = input()
                print("release_date = ")
                release_date_input = input()
                while not is_date(release_date_input, True):
                    print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                    release_date_input = input()
                fullQuery = f"{song_ID_input}, \'{name_input}\', {auditions_input}, \'{release_date_input}\'"

                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO \"Song\" (\"song_ID\", \"name\", auditions, \"release_date\") VALUES (" + fullQuery + ");"
                    )

            if choice3 == "4":
                print("ENTER DATA")
                print("name = ")
                name_input = input()
                print("creation_date = ")
                creation_date_input = input()
                while not is_date(creation_date_input, True):
                    print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                    creation_date_input = input()
                print("country = ")
                country_input = input()
                fullQuery = f"\'{name_input}\', \'{creation_date_input}\', \'{country_input}\'"

                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO \"Label\" (\"name\", \"creation_date\", country) VALUES (" + fullQuery + ");"
                    )

            if choice3 == "5":
                print("ENTER DATA")
                print("user_ID = ")
                user_ID_input = input()
                while not user_ID_input.isnumeric():
                    print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                    user_ID_input = input()
                selectQuery = "SELECT * from \"User\" WHERE \"user_ID\"=" + user_ID_input
                with connection.cursor() as cursor:
                    cursor.execute(selectQuery)
                    selectInfo = cursor.fetchall()
                while len(selectInfo) == 0:
                    print("IN PARENT TABLE THERE ARE NO ROWS WITH THE REQUIRED DATA. ENTER EXISTING DATA:")
                    user_ID_input = input()
                    while not user_ID_input.isnumeric():
                        print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                        user_ID_input = input()
                    selectQuery = "SELECT * from \"User\" WHERE \"user_ID\"=" + user_ID_input
                    with connection.cursor() as cursor:
                        cursor.execute(selectQuery)
                        selectInfo = cursor.fetchall()

                print("song_ID = ")
                song_ID_input = input()
                while not song_ID_input.isnumeric():
                    print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                    song_ID_input = input()
                selectQuery = "SELECT * from \"Song\" WHERE \"song_ID\"=" + song_ID_input
                with connection.cursor() as cursor:
                    cursor.execute(selectQuery)
                    selectInfo = cursor.fetchall()
                while len(selectInfo) == 0:
                    print("IN PARENT TABLE THERE ARE NO ROWS WITH THE REQUIRED DATA. ENTER EXISTING DATA:")
                    song_ID_input = input()
                    while not song_ID_input.isnumeric():
                        print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                        song_ID_input = input()
                    selectQuery = "SELECT * from \"Song\" WHERE \"song_ID\"=" + song_ID_input
                    with connection.cursor() as cursor:
                        cursor.execute(selectQuery)
                        selectInfo = cursor.fetchall()
                fullQuery = f"{user_ID_input}, {song_ID_input}"

                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO \"User/Song\" (\"user_ID\", \"song_ID\") VALUES (" + fullQuery + ");"
                    )

            if choice3 == "6":
                print("ENTER DATA")
                print("artist_ID = ")
                artist_ID_input = input()
                while not artist_ID_input.isnumeric():
                    print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                    artist_ID_input = input()
                selectQuery = "SELECT * from \"Artist\" WHERE \"artist_ID\"=" + artist_ID_input
                with connection.cursor() as cursor:
                    cursor.execute(selectQuery)
                    selectInfo = cursor.fetchall()
                while len(selectInfo) == 0:
                    print("IN PARENT TABLE THERE ARE NO ROWS WITH THE REQUIRED DATA. ENTER EXISTING DATA:")
                    artist_ID_input = input()
                    while not artist_ID_input.isnumeric():
                        print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                        artist_ID_input = input()
                    selectQuery = "SELECT * from \"Artist\" WHERE \"artist_ID\"=" + artist_ID_input
                    with connection.cursor() as cursor:
                        cursor.execute(selectQuery)
                        selectInfo = cursor.fetchall()

                print("song_ID = ")
                song_ID_input = input()
                while not song_ID_input.isnumeric():
                    print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                    song_ID_input = input()
                selectQuery = "SELECT * from \"Song\" WHERE \"song_ID\"=" + song_ID_input
                with connection.cursor() as cursor:
                    cursor.execute(selectQuery)
                    selectInfo = cursor.fetchall()
                while len(selectInfo) == 0:
                    print("IN PARENT TABLE THERE ARE NO ROWS WITH THE REQUIRED DATA. ENTER EXISTING DATA:")
                    song_ID_input = input()
                    while not song_ID_input.isnumeric():
                        print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                        song_ID_input = input()
                    selectQuery = "SELECT * from \"Song\" WHERE \"song_ID\"=" + song_ID_input
                    with connection.cursor() as cursor:
                        cursor.execute(selectQuery)
                        selectInfo = cursor.fetchall()

                fullQuery = f"{artist_ID_input}, {song_ID_input}"

                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO \"Artist/Song\" (\"artist_ID\", \"song_ID\") VALUES (" + fullQuery + ");"
                    )

            if choice3 == "7":
                print("ENTER DATA")
                print("label_name = ")
                label_name_input = input()
                selectQuery = "SELECT * from \"Label\" WHERE \"name\"=" + "\'" + label_name_input + "\'"
                with connection.cursor() as cursor:
                    cursor.execute(selectQuery)
                    selectInfo = cursor.fetchall()
                while len(selectInfo) == 0:
                    print("IN PARENT TABLE THERE ARE NO ROWS WITH THE REQUIRED DATA. ENTER EXISTING DATA:")
                    label_name_input = input()
                    selectQuery = "SELECT * from \"Label\" WHERE \"name\"=" + "\'" + label_name_input + "\'"
                    with connection.cursor() as cursor:
                        cursor.execute(selectQuery)
                        selectInfo = cursor.fetchall()

                print("artist_ID = ")
                artist_ID_input = input()
                while not artist_ID_input.isnumeric():
                    print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                    artist_ID_input = input()
                selectQuery = "SELECT * from \"Artist\" WHERE \"artist_ID\"=" + artist_ID_input
                with connection.cursor() as cursor:
                    cursor.execute(selectQuery)
                    selectInfo = cursor.fetchall()
                while len(selectInfo) == 0:
                    print("IN PARENT TABLE THERE ARE NO ROWS WITH THE REQUIRED DATA. ENTER EXISTING DATA:")
                    artist_ID_input = input()
                    while not artist_ID_input.isnumeric():
                        print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                        artist_ID_input = input()
                    selectQuery = "SELECT * from \"Artist\" WHERE \"artist_ID\"=" + artist_ID_input
                    with connection.cursor() as cursor:
                        cursor.execute(selectQuery)
                        selectInfo = cursor.fetchall()

                fullQuery = f"\'{label_name_input}\', {artist_ID_input}"

                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO \"Label/Artist\" (\"label_name\", \"artist_ID\") VALUES (" + fullQuery + ");"
                    )

        elif choice == "4":
            print("SELECT UPDATE OPTION:")
            print("1. UPDATE USER TABLE")
            print("2. UPDATE SONG TABLE")
            print("3. UPDATE ARTIST TABLE")
            print("4. UPDATE LABEL TABLE")
            print("5. UPDATE USER/SONG TABLE")
            print("6. UPDATE ARTIST/SONG TABLE")
            print("7. UPDATE LABEL/ARTIST TABLE")

            choice4 = input()
            while choice4 != "1" and choice4 != "2" and choice4 != "3" and choice4 != "4" and choice4 != "5" and choice4 != "6" and choice4!= "7":
                print("SELECT RIGHT OPTION")
                choice4 = input()

            fullQuery = "UPDATE "

            if choice4 == "1":
                fullQuery += "\"User\" SET "
                print("1. user_ID")
                print("2. nickname")
                print("3. reg_date")
                print("4. saved_songs")
                print("5. subscription_type")
                print("6. exit")
                count = 0
                while True:
                    print("SELECT COLUMNS TO UPDATE (PK isn't allowed to edit) :")
                    column_to_update = input()
                    if column_to_update == "6":
                        break
                    while column_to_update != "1" and column_to_update != "2" and column_to_update != "3" and column_to_update != "4" and column_to_update != "5":
                        print("SELECT ATTRIBUTE CORRECTLY:")
                        column_to_update = input()
                    while column_to_update == "1":
                        print("YOU CAN'T UPDATE PK ATTRIBUTE. SELECT ANOTHER ATTRIBUTE TO UPDATE:")
                        column_to_update = input()
                    if column_to_update == "2":
                        column_to_update = "nickname"
                    elif column_to_update == "3":
                        column_to_update = "reg_date"
                    elif column_to_update == "4":
                        column_to_update = "saved_songs"
                    elif column_to_update == "5":
                        column_to_update = "subscription_type"

                    if count != 0:
                        fullQuery += ", "
                    print("ENTER NEW VALUE:")
                    newValue = input()
                    if column_to_update == "reg_date":
                        while not is_date(newValue):
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            newValue = input()
                    elif column_to_update == "saved_songs":
                        while not newValue.isnumeric():
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            newValue = input()
                    elif column_to_update == "subscription_type":
                        while newValue != "free" and newValue != "premium" and newValue != "family":
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            newValue = input()

                    if column_to_update == "saved_songs":
                        fullQuery += "\"" + column_to_update + "\" = " + newValue
                    else:
                        fullQuery += "\"" + column_to_update + "\" = " + "\'" + newValue + "\'"
                    count += 1

                print("ENTER WHERE CONDITION: (example \"user_ID\" = 111111 or \"nickname\" ='qwerty')")
                whereCondition = input()
                fullQuery += " WHERE " + whereCondition + ";"

                with connection.cursor() as cursor:
                    cursor.execute(fullQuery)

            if choice4 == "2":
                fullQuery += "\"Song\" SET "
                print("1. song_ID")
                print("2. name")
                print("3. auditions")
                print("4. release_date")
                print("5. exit")
                count = 0
                while True:
                    print("SELECT COLUMNS TO UPDATE (PK isn't allowed to edit) :")
                    column_to_update = input()
                    if column_to_update == "5":
                        break
                    while column_to_update != "1" and column_to_update != "2" and column_to_update != "3" and column_to_update != "4":
                        print("SELECT ATTRIBUTE CORRECTLY:")
                        column_to_update = input()
                    while column_to_update == "1":
                        print("YOU CAN'T UPDATE PK ATTRIBUTE. SELECT ANOTHER ATTRIBUTE TO UPDATE:")
                        column_to_update = input()
                    if column_to_update == "2":
                        column_to_update = "name"
                    elif column_to_update == "3":
                        column_to_update = "auditions"
                    elif column_to_update == "4":
                        column_to_update = "release_date"

                    if count != 0:
                        fullQuery += ", "
                    print("ENTER NEW VALUE:")
                    newValue = input()
                    if column_to_update == "release_date":
                        while not is_date(newValue):
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            newValue = input()
                    elif column_to_update == "auditions":
                        while not newValue.isnumeric():
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            newValue = input()

                    if column_to_update == "auditions":
                        fullQuery += "\"" + column_to_update + "\" = " + newValue
                    else:
                        fullQuery += "\"" + column_to_update + "\" = " + "\'" + newValue + "\'"
                    count += 1

                print("ENTER WHERE CONDITION: (example \"song_ID\" = 111 or \"name\" = 'Sky')")
                whereCondition = input()
                fullQuery += " WHERE " + whereCondition + ";"

                with connection.cursor() as cursor:
                    cursor.execute(fullQuery)

            if choice4 == "3":
                fullQuery += "\"Artist\" SET "
                print("1. artist_ID")
                print("2. name")
                print("3. full_name")
                print("4. age")
                print("5. songs_amount")
                print("6. exit")
                count = 0
                while True:
                    print("SELECT COLUMNS TO UPDATE (PK isn't allowed to edit) :")
                    column_to_update = input()
                    if column_to_update == "6":
                        break
                    while column_to_update != "1" and column_to_update != "2" and column_to_update != "3" and column_to_update != "4" and column_to_update != "5":
                        print("SELECT ATTRIBUTE CORRECTLY:")
                        column_to_update = input()
                    while column_to_update == "1":
                        print("YOU CAN'T UPDATE PK ATTRIBUTE. SELECT ANOTHER ATTRIBUTE TO UPDATE:")
                        column_to_update = input()
                    if column_to_update == "2":
                        column_to_update = "name"
                    elif column_to_update == "3":
                        column_to_update = "full_name"
                    elif column_to_update == "4":
                        column_to_update = "age"
                    elif column_to_update == "5":
                        column_to_update = "songs_amount"

                    if count != 0:
                        fullQuery += ", "
                    print("ENTER NEW VALUE:")
                    newValue = input()
                    if column_to_update == "age":
                        while not newValue.isnumeric():
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            newValue = input()
                    elif column_to_update == "songs_amount":
                        while not newValue.isnumeric():
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            newValue = input()

                    if column_to_update == "age" or column_to_update == "songs_amount":
                        fullQuery += "\"" + column_to_update + "\" = " + newValue
                    else:
                        fullQuery += "\"" + column_to_update + "\" = " + "\'" + newValue + "\'"
                    count += 1

                print("ENTER WHERE CONDITION: (example \"artist_ID\" = 11 or \"name\"='Scarlxrd')")
                whereCondition = input()
                fullQuery += " WHERE " + whereCondition + ";"

                with connection.cursor() as cursor:
                    cursor.execute(fullQuery)

            if choice4 == "4":
                fullQuery += "\"Label\" SET "
                print("1. name")
                print("2. creation_date")
                print("3. country")
                print("4. exit")
                count = 0
                while True:
                    print("SELECT COLUMNS TO UPDATE (PK isn't allowed to edit) :")
                    column_to_update = input()
                    if column_to_update == "4":
                        break
                    while column_to_update != "1" and column_to_update != "2" and column_to_update != "3":
                        print("SELECT ATTRIBUTE CORRECTLY:")
                        column_to_update = input()
                    while column_to_update == "1":
                        print("YOU CAN'T UPDATE PK ATTRIBUTE. SELECT ANOTHER ATTRIBUTE TO UPDATE:")
                        column_to_update = input()
                    if column_to_update == "2":
                        column_to_update = "creation_date"
                    elif column_to_update == "3":
                        column_to_update = "country"

                    if count != 0:
                        fullQuery += ", "
                    print("ENTER NEW VALUE:")
                    newValue = input()
                    if column_to_update == "creation_date":
                        while not is_date(newValue):
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            newValue = input()

                    fullQuery += "\"" + column_to_update + "\" = " + "\'" + newValue + "\'"
                    count += 1

                print("ENTER WHERE CONDITION: (example \"contry\" = \'USA\')")
                whereCondition = input()
                fullQuery += " WHERE " + whereCondition + ";"

                with connection.cursor() as cursor:
                    cursor.execute(fullQuery)

            if choice4 == "5":
                fullQuery += "\"User/Song\" SET "
                print("1. user_ID")
                print("2. song_ID")
                print("3. exit")
                count = 0
                while True:
                    print("SELECT COLUMNS TO UPDATE :")
                    column_to_update = input()
                    if column_to_update == "3":
                        break
                    while column_to_update != "1" and column_to_update != "2":
                        print("SELECT ATTRIBUTE CORRECTLY:")
                        column_to_update = input()
                    if column_to_update == "1":
                        column_to_update = "user_ID"
                    elif column_to_update == "2":
                        column_to_update = "song_ID"

                    if count != 0:
                        fullQuery += ", "
                    print("ENTER NEW VALUE:")
                    newValue = input()
                    while not newValue.isnumeric():
                        print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                        newValue = input()

                    selectQuery = "SELECT * from "
                    if column_to_update == "user_ID":
                        selectQuery += "\"User\" WHERE \"user_ID\"=" + newValue
                    else:
                        selectQuery += "\"Song\" WHERE \"song_ID\"=" + newValue
                    with connection.cursor() as cursor:
                        cursor.execute(selectQuery)
                        selectInfo = cursor.fetchall()
                    while len(selectInfo) == 0:
                        print("IN PARENT TABLE THERE ARE NO ROWS WITH THE REQUIRED DATA. ENTER EXISTING DATA:")
                        newValue = input()
                        while not newValue.isnumeric():
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            newValue = input()
                        selectQuery = "SELECT * from "
                        if column_to_update == "user_ID":
                            selectQuery += "\"User\" WHERE \"user_ID\"=" + newValue
                        else:
                            selectQuery += "\"Song\" WHERE \"song_ID\"=" + newValue
                        with connection.cursor() as cursor:
                            cursor.execute(selectQuery)
                            selectInfo = cursor.fetchall()

                    fullQuery += "\"" + column_to_update + "\" = " + newValue
                    count += 1

                print("ENTER WHERE CONDITION: (example \"user_ID\" = 111111)")
                whereCondition = input()
                fullQuery += " WHERE " + whereCondition + ";"

                with connection.cursor() as cursor:
                    cursor.execute(fullQuery)

            if choice4 == "6":
                fullQuery += "\"Artist/Song\" SET "
                print("1. artist_ID")
                print("2. song_ID")
                print("3. exit")
                count = 0
                while True:
                    print("SELECT COLUMNS TO UPDATE :")
                    column_to_update = input()
                    if column_to_update == "3":
                        break
                    while column_to_update != "1" and column_to_update != "2":
                        print("SELECT ATTRIBUTE CORRECTLY:")
                        column_to_update = input()
                    if column_to_update == "1":
                        column_to_update = "artist_ID"
                    elif column_to_update == "2":
                        column_to_update = "song_ID"

                    if count != 0:
                        fullQuery += ", "
                    print("ENTER NEW VALUE:")
                    newValue = input()
                    while not newValue.isnumeric():
                        print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                        newValue = input()

                    selectQuery = "SELECT * from "
                    if column_to_update == "artist_ID":
                        selectQuery += "\"Artist\" WHERE \"artist_ID\"=" + newValue
                    else:
                        selectQuery += "\"Song\" WHERE \"song_ID\"=" + newValue
                    with connection.cursor() as cursor:
                        cursor.execute(selectQuery)
                        selectInfo = cursor.fetchall()
                    while len(selectInfo) == 0:
                        print("IN PARENT TABLE THERE ARE NO ROWS WITH THE REQUIRED DATA. ENTER EXISTING DATA:")
                        newValue = input()
                        while not newValue.isnumeric():
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            newValue = input()
                        selectQuery = "SELECT * from "
                        if column_to_update == "artist_ID":
                            selectQuery += "\"Artist\" WHERE \"artist_ID\"=" + newValue
                        else:
                            selectQuery += "\"Song\" WHERE \"song_ID\"=" + newValue
                        with connection.cursor() as cursor:
                            cursor.execute(selectQuery)
                            selectInfo = cursor.fetchall()

                    fullQuery += "\"" + column_to_update + "\" = " + newValue
                    count += 1

                print("ENTER WHERE CONDITION: (example \"artist_ID\" = 111)")
                whereCondition = input()
                fullQuery += " WHERE " + whereCondition + ";"

                with connection.cursor() as cursor:
                    cursor.execute(fullQuery)

            if choice4 == "7":
                fullQuery += "\"Label/Artist\" SET "
                print("1. label_name")
                print("2. artist_ID")
                print("3. exit")
                count = 0
                while True:
                    print("SELECT COLUMNS TO UPDATE :")
                    column_to_update = input()
                    if column_to_update == "3":
                        break
                    while column_to_update != "1" and column_to_update != "2":
                        print("SELECT ATTRIBUTE CORRECTLY:")
                        column_to_update = input()
                    if column_to_update == "1":
                        column_to_update = "label_name"
                    elif column_to_update == "2":
                        column_to_update = "artist_ID"

                    if count != 0:
                        fullQuery += ", "
                    print("ENTER NEW VALUE:")
                    newValue = input()
                    if column_to_update == "artist_ID":
                        while not newValue.isnumeric():
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            newValue = input()

                    selectQuery = "SELECT * from "
                    if column_to_update == "artist_ID":
                        selectQuery += "\"Artist\" WHERE \"artist_ID\"=" + newValue
                    else:
                        selectQuery += "\"Label\" WHERE \"name\"=" + "\'" + newValue + "\'"
                    with connection.cursor() as cursor:
                        cursor.execute(selectQuery)
                        selectInfo = cursor.fetchall()
                    while len(selectInfo) == 0:
                        print("IN PARENT TABLE THERE ARE NO ROWS WITH THE REQUIRED DATA. ENTER EXISTING DATA:")
                        newValue = input()
                        if column_to_update == "artist_ID":
                            while not newValue.isnumeric():
                                print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                                newValue = input()
                        selectQuery = "SELECT * from "
                        if column_to_update == "artist_ID":
                            selectQuery += "\"Artist\" WHERE \"artist_ID\"=" + newValue
                        else:
                            selectQuery += "\"Label\" WHERE \"name\"=" + "\'" + newValue + "\'"
                        with connection.cursor() as cursor:
                            cursor.execute(selectQuery)
                            selectInfo = cursor.fetchall()

                    if column_to_update == "artist_ID":
                        fullQuery += "\"" + column_to_update + "\" = " + newValue
                    else:
                        fullQuery += "\"" + column_to_update + "\" = " + "\'" + newValue + "\'"
                    count += 1

                print("ENTER WHERE CONDITION: (example \"artist_ID\" = 111)")
                whereCondition = input()
                fullQuery += " WHERE " + whereCondition + ";"

                with connection.cursor() as cursor:
                    cursor.execute(fullQuery)

        elif choice == "5":
            print("SELECT DELETE OPTION:")
            print("1. DELETE FROM USER TABLE")
            print("2. DELETE FROM ARTIST TABLE")
            print("3. DELETE FROM SONG TABLE")
            print("4. DELETE FROM LABEL TABLE")
            print("5. DELETE FROM USER/SONG TABLE")
            print("6. DELETE FROM ARTIST/SONG TABLE")
            print("7. DELETE FROM LABEL/ARTIST TABLE")

            choice5 = input()
            while choice5 != "1" and choice5 != "2" and choice5 != "3" and choice5 != "4" and choice5 != "5" and choice5 != "6" and choice5 != "7":
                print("SELECT RIGHT OPTION")
                choice5 = input()

            if choice5 == "1":
                print("1. user_ID")
                print("2. nickname")
                print("3. reg_date")
                print("4. saved_songs")
                print("5. subscription_type")

                print("ENTER WHERE CONDITION: (example \"user_ID\" = 111111111)")
                whereCondition = input()

                fullQuery = "SELECT * from \"User\" WHERE " + whereCondition + ";"
                with connection.cursor() as cursor:
                    cursor.execute(fullQuery)
                    dataInfo = cursor.fetchall()
                    for row in dataInfo:
                        fullQuery = "DELETE from \"User/Song\" WHERE \"user_ID\"=" + str(row[0]) + ";"
                        cursor.execute(fullQuery)

                fullQuery = "DELETE from \"User\" WHERE " + whereCondition + ";"
                with connection.cursor() as cursor:
                    cursor.execute(fullQuery)

            if choice5 == "2":
                print("1. artist_ID")
                print("2. name")
                print("3. full_name")
                print("4. age")
                print("5. songs_amount")

                print("ENTER WHERE CONDITION: (example \"artist_ID\" = 111)")
                whereCondition = input()

                fullQuery = "SELECT * from \"Artist\" WHERE " + whereCondition + ";"
                with connection.cursor() as cursor:
                    cursor.execute(fullQuery)
                    dataInfo = cursor.fetchall()
                    for row in dataInfo:
                        fullQuery = "DELETE from \"Artist/Song\" WHERE \"artist_ID\"=" + str(row[0]) + ";"
                        cursor.execute(fullQuery)
                        fullQuery = "DELETE from \"Label/Artist\" WHERE \"artist_ID\"=" + str(row[0]) + ";"
                        cursor.execute(fullQuery)

                fullQuery = "DELETE from \"Artist\" WHERE " + whereCondition + ";"
                with connection.cursor() as cursor:
                    cursor.execute(fullQuery)

            if choice5 == "3":
                print("1. song_ID")
                print("2. name")
                print("3. auditions")
                print("4. release_date")

                print("ENTER WHERE CONDITION: (example \"song_ID\" = 111)")
                whereCondition = input()

                fullQuery = "SELECT * from \"Song\" WHERE " + whereCondition + ";"
                with connection.cursor() as cursor:
                    cursor.execute(fullQuery)
                    dataInfo = cursor.fetchall()
                    for row in dataInfo:
                        fullQuery = "DELETE from \"Artist/Song\" WHERE \"song_ID\"=" + str(row[0]) + ";"
                        cursor.execute(fullQuery)
                        fullQuery = "DELETE from \"User/Song\" WHERE \"song_ID\"=" + str(row[0]) + ";"
                        cursor.execute(fullQuery)

                fullQuery = "DELETE from \"Song\" WHERE " + whereCondition + ";"
                with connection.cursor() as cursor:
                    cursor.execute(fullQuery)

            if choice5 == "4":
                print("1. name")
                print("2. creation_date")
                print("3. country")

                print("ENTER WHERE CONDITION: (example \"country\" = 'Jamaica')")
                whereCondition = input()

                fullQuery = "SELECT * from \"Label\" WHERE " + whereCondition + ";"
                with connection.cursor() as cursor:
                    cursor.execute(fullQuery)
                    dataInfo = cursor.fetchall()
                    for row in dataInfo:
                        fullQuery = "DELETE from \"Label/Artist\" WHERE \"label_name\"=" + "\'" + str(row[0]) + "\'" + ";"
                        cursor.execute(fullQuery)

                fullQuery = "DELETE from \"Label\" WHERE " + whereCondition + ";"
                with connection.cursor() as cursor:
                    cursor.execute(fullQuery)

            if choice5 == "5":
                print("1. user_ID")
                print("2. song_ID")

                print("ENTER WHERE CONDITION: (example \"user_ID\" = 111111)")
                whereCondition = input()

                fullQuery = "DELETE from \"User/Song\" WHERE " + whereCondition + ";"
                with connection.cursor() as cursor:
                    cursor.execute(fullQuery)

            if choice5 == "6":
                print("1. artist_ID")
                print("2. song_ID")

                print("ENTER WHERE CONDITION: (example \"artist_ID\" = 111)")
                whereCondition = input()

                fullQuery = "DELETE from \"Artist/Song\" WHERE " + whereCondition + ";"
                with connection.cursor() as cursor:
                    cursor.execute(fullQuery)

            if choice5 == "7":
                print("1. label_name")
                print("2. artist_ID")

                print("ENTER WHERE CONDITION: (example \"artist_ID\" = 111)")
                whereCondition = input()

                fullQuery = "DELETE from \"Label/Artist\" WHERE " + whereCondition + ";"
                with connection.cursor() as cursor:
                    cursor.execute(fullQuery)

        elif choice == "6":
            print("SELECT TABLE:")
            print("1. USER TABLE")
            print("2. SONG TABLE")
            print("3. ARTIST TABLE")
            print("4. LABEL TABLE")
            print("5. USER/SONG TABLE")
            print("6. ARTIST/SONG TABLE")
            print("7. LABEL/ARTIST TABLE")

            choice6 = input()
            while choice6 != "1" and choice6 != "2" and choice6 != "3" and choice6 != "4" and choice6 != "5" and choice6 != "6" and choice6 != "7":
                print("SELECT RIGHT OPTION")
                choice6 = input()

            fullQuery = "TRUNCATE TABLE "
            if choice6 == "1":
                fullQuery += "\"User\" CASCADE;"
            elif choice6 == "2":
                fullQuery += "\"Song\" CASCADE;"
            elif choice6 == "3":
                fullQuery += "\"Artist\" CASCADE;"
            elif choice6 == "4":
                fullQuery += "\"Label\" CASCADE;"
            elif choice6 == "5":
                fullQuery += "\"User/Song\";"
            elif choice6 == "6":
                fullQuery += "\"Artist/Song\";"
            elif choice6 == "7":
                fullQuery += "\"Label/Artist\";"

            with connection.cursor() as cursor:
                cursor.execute(fullQuery)

        elif choice == "7":
            n = 1
            print("SELECT RANDOM OPTION:")
            print("1.RANDOM USER TABLE")
            print("2.RANDOM SONG TABLE")
            print("3.RANDOM ARTIST TABLE")
            print("4.RANDOM LABEL TABLE")
            print("5. RANDOM USER/SONG TABLE")
            print("6. RANDOM ARTIST/SONG TABLE")
            print("7. RANDOM LABEL/ARTIST TABLE")

            choice7 = input()
            while choice7 != "1" and choice7 != "2" and choice7 != "3" and choice7 != "4" and choice7 != "5" and choice7 != "6" and choice7 != "7":
                print("SELECT RIGHT OPTION")
                choice7 = input()

            if choice7 == "1":
                print("ENTER N:")
                n = input()
                nStart = 1
                with connection.cursor() as cursor:
                    cursor.execute("SELECT MAX(\"user_ID\") FROM \"User\"")
                    nStart = cursor.fetchone()
                nStart = nStart[0]
                nEnd = nStart + int(n)
                nStart += 1
                nStartStr = str(nStart)
                nEndStr = str(nEnd)
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO \"User\"(\"user_ID\")"
                        "SELECT * FROM generate_series(" + nStartStr + ", " + nEndStr + ") as int"
                    )

                    cursor.execute(
                        "UPDATE \"User\""
                        "SET nickname=chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) ||"
                        "chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) || "
                        "chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int)"
                        "WHERE \"nickname\" IS NULL;"
                    )

                    cursor.execute(
                        "UPDATE \"User\""
                        "SET \"reg_date\"=trunc(random()*30)::int + 1 || '.' || trunc(random()*11)::int + 1 || '.' ||"
                        "trunc(random()*4)::int + 2018"
                        "WHERE \"reg_date\" IS NULL;"
                    )

                    cursor.execute(
                        "UPDATE \"User\""
                        "SET \"saved_songs\"=trunc(random()*2000)::int "
                        "WHERE \"saved_songs\" IS NULL;"
                    )

                    cursor.execute(
                        "UPDATE \"User\""
                        "SET \"subscription_type\"=chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int)"
                        "WHERE \"subscription_type\" IS NULL;"
                    )

            elif choice7 == "2":
                print("ENTER N:")
                n = input()
                nStart = 1
                with connection.cursor() as cursor:
                    cursor.execute("SELECT MAX(\"song_ID\") FROM \"Song\"")
                    nStart = cursor.fetchone()
                nStart = nStart[0]
                nEnd = nStart + int(n)
                nStart += 1
                nStartStr = str(nStart)
                nEndStr = str(nEnd)
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO \"Song\"(\"song_ID\")"
                        "SELECT * FROM generate_series(" + nStartStr + "," + nEndStr + ") as int"
                    )

                    cursor.execute(
                        "UPDATE \"Song\""
                        "SET name=chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) ||"
                        "chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) || "
                        "chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int)"
                        "WHERE \"name\" IS NULL;"
                    )

                    cursor.execute(
                        "UPDATE \"Song\""
                        "SET \"release_date\"=trunc(random()*30)::int + 1 || '.' || trunc(random()*11)::int + 1 || '.' ||"
                        "trunc(random()*12)::int + 2010"
                        "WHERE \"release_date\" IS NULL;"
                    )

                    cursor.execute(
                        "UPDATE \"Song\""
                        "SET \"auditions\"=trunc(random()*2000000000)::int "
                        "WHERE \"auditions\" IS NULL;"
                    )

            elif choice7 == "3":
                print("ENTER N:")
                n = input()
                nStart = 1
                with connection.cursor() as cursor:
                    cursor.execute("SELECT MAX(\"artist_ID\") FROM \"Artist\"")
                    nStart = cursor.fetchone()
                nStart = nStart[0]
                nEnd = nStart + int(n)
                nStart += 1
                nStartStr = str(nStart)
                nEndStr = str(nEnd)
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO \"Artist\"(\"artist_ID\")"
                        "SELECT * FROM generate_series(" + nStartStr + "," + nEndStr + ") as int"
                    )

                    cursor.execute(
                        "UPDATE \"Artist\""
                        "SET name=chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) ||"
                        "chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) || "
                        "chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int)"
                        "WHERE \"name\" IS NULL;"
                    )

                    cursor.execute(
                        "UPDATE \"Artist\""
                        "SET full_name=chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) ||"
                        "chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) || "
                        "chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int)"
                        "WHERE \"full_name\" IS NULL;"
                    )

                    cursor.execute(
                        "UPDATE \"Artist\""
                        "SET \"age\"=trunc(15+random()*50)::int "
                        "WHERE \"age\" IS NULL;"
                    )

                    cursor.execute(
                        "UPDATE \"Artist\""
                        "SET \"songs_amount\"=trunc(random()*300)::int "
                        "WHERE \"songs_amount\" IS NULL;"
                    )

            elif choice7 == "4":
                print("ENTER N:")
                n = input()
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO \"Label\"(\"name\")"
                        "SELECT chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) ||"
                        "chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int)"
                        "|| chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) || "
                        "chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) ||"
                        "chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) ||"
                        "chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) ||"
                        "chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int)"
                        "FROM generate_series(1," + n + ")"
                    )

                    cursor.execute(
                        "UPDATE \"Label\""
                        "SET country=chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) ||"
                        "chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) || "
                        "chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int)"
                        "WHERE \"country\" IS NULL;"
                    )

                    cursor.execute(
                        "UPDATE \"Label\""
                        "SET \"creation_date\"=trunc(random()*30)::int + 1 || '.' || trunc(random()*11)::int + 1 || '.' ||"
                        "trunc(random()*92)::int + 1930"
                        "WHERE \"creation_date\" IS NULL;"
                    )

            elif choice7 == "5":
                print("ENTER N:")
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO \"User/Song\""
                        "SELECT * FROM"
                        "(SELECT \"user_ID\" FROM \"User\" ORDER BY random() LIMIT 5) a1,"
                        "(SELECT \"song_ID\" FROM \"Song\" ORDER BY random() LIMIT 6) b1 "
                        "ORDER BY random()"
                    )

            elif choice7 == "6":
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO \"Artist/Song\""
                        "SELECT * FROM"
                        "(SELECT \"artist_ID\" FROM \"Artist\" ORDER BY random() LIMIT 5) a1,"
                        "(SELECT \"song_ID\" FROM \"Song\" ORDER BY random() LIMIT 6) b1 "
                        "ORDER BY random()"
                    )

            elif choice7 == "7":
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO \"Label/Artist\""
                        "SELECT * FROM"
                        "(SELECT \"name\" FROM \"Label\" ORDER BY random() LIMIT 5) a1,"
                        "(SELECT \"artist_ID\" FROM \"Artist\" ORDER BY random() LIMIT 6) b1 "
                        "ORDER BY random()"
                    )

        elif choice == "8":
            print("1. USER TABLE")
            print("2. SONG TABLE")
            print("3. ARTIST TABLE")
            print("4. LABEL TABLE")
            print("5. USER/SONG TABLE")
            print("6. ARTIST/SONG TABLE")
            print("7. LABEL/ARTIST TABLE")
            print("8. EXIT")

            fullQuery = "SELECT * FROM "
            values = ["a1", "b1", "c1", "d1", "a2", "b2", "c2"]
            index = 0
            count = 0

            while True:
                print("SELECT TABLE:")
                choice8 = input()
                while choice8 != "1" and choice8 != "2" and choice8 != "3" and choice8 != "4" and choice8 != "5" and choice8 != "6" and choice8 != "7" and choice8 != "8":
                    print("SELECT RIGHT OPTION")
                    choice8 = input()

                if choice8 == "8":
                    break

                elif choice8 == "1":
                    print("1. user_ID")
                    print("2. nickname")
                    print("3. reg_date")
                    print("4. saved_songs")
                    print("5. subscription_type")

                    print("SELECT ATTRIBUTE:")
                    choice8_1 = input()
                    while choice8_1 != "1" and choice8_1 != "2" and choice8_1 != "3" and choice8_1 != "4" and choice8_1 != "5":
                        print("SELECT RIGHT OPTION")
                        choice8_1 = input()

                    if choice8_1 == "1":
                        print("ENTER START:")
                        choice8_1_start = input()
                        while not choice8_1_start.isnumeric():
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            choice8_1_start = input()
                        print("ENTER END:")
                        choice8_1_end = input()
                        while not choice8_1_end.isnumeric():
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            choice8_1_end = input()

                        if index == 7:
                            index = 0
                        if count != 0:
                            fullQuery += ", "
                        fullQuery += "(SELECT * FROM \"User\" where \"user_ID\" BETWEEN " + choice8_1_start + " AND " + choice8_1_end + ") " + values[index]
                        index += 1
                        count += 1

                    elif choice8_1 == "2":
                        print("ENTER LIKE EXPRESSION:")
                        choice8_1 = input()

                        if index == 7:
                            index = 0
                        if count != 0:
                            fullQuery += ", "
                        fullQuery += "(SELECT * FROM \"User\" where \"User\".\"nickname\" LIKE \'" + choice8_1 + "\') " + values[index]
                        index += 1
                        count += 1

                    elif choice8_1 == "4":
                        print("ENTER START:")
                        choice8_1_start = input()
                        while not choice8_1_start.isnumeric():
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            choice8_1_start = input()
                        print("ENTER END:")
                        choice8_1_end = input()
                        while not choice8_1_end.isnumeric():
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            choice8_1_end = input()

                        if index == 7:
                            index = 0
                        if count != 0:
                            fullQuery += ", "
                        fullQuery += "(SELECT * FROM \"User\" where \"saved_songs\" BETWEEN " + choice8_1_start + " AND " + choice8_1_end + ") " + \
                                     values[index]
                        index += 1
                        count += 1

                    elif choice8_1 == "3":
                        print("ENTER LIKE EXPRESSION:")
                        choice8_1 = input()

                        if index == 7:
                            index = 0
                        if count != 0:
                            fullQuery += ", "
                        fullQuery += "(SELECT * FROM \"User\" where \"User\".\"reg_date\" LIKE \'" + choice8_1 + "\') " + values[index]
                        index += 1
                        count += 1

                    elif choice8_1 == "5":
                        print("ENTER LIKE EXPRESSION:")
                        choice8_1 = input()

                        if index == 7:
                            index = 0
                        if count != 0:
                            fullQuery += ", "
                        fullQuery += "(SELECT * FROM \"User\" where \"User\".\"subscription_type\" LIKE \'" + choice8_1 + "\') " + values[index]
                        index += 1
                        count += 1

                elif choice8 == "2":
                    print("1. song_ID")
                    print("2. name")
                    print("3. auditions")
                    print("4. release_date")

                    print("SELECT ATTRIBUTE:")
                    choice8_2 = input()
                    while choice8_2 != "1" and choice8_2 != "2" and choice8_2 != "3" and choice8_2 != "4":
                        print("SELECT RIGHT OPTION")
                        choice8_2 = input()

                    if choice8_2 == "1":
                        print("ENTER START:")
                        choice8_2_start = input()
                        while not choice8_2_start.isnumeric():
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            choice8_2_start = input()
                        print("ENTER END:")
                        choice8_2_end = input()
                        while not choice8_2_end.isnumeric():
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            choice8_2_end = input()

                        if index == 7:
                            index = 0
                        if count != 0:
                            fullQuery += ", "
                        fullQuery += "(SELECT * FROM \"Song\" where \"song_ID\" BETWEEN " + choice8_2_start + " AND " + choice8_2_end + ") " + values[index]
                        index += 1
                        count += 1

                    elif choice8_2 == "2":
                        print("ENTER LIKE EXPRESSION:")
                        choice8_2 = input()

                        if index == 7:
                            index = 0
                        if count != 0:
                            fullQuery += ", "
                        fullQuery += "(SELECT * FROM \"Song\" where \"Song\".\"name\" LIKE \'" + choice8_2 + "\') " + values[index]
                        index += 1
                        count += 1

                    elif choice8_2 == "3":
                        print("ENTER START:")
                        choice8_2_start = input()
                        while not choice8_2_start.isnumeric():
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            choice8_2_start = input()
                        print("ENTER END:")
                        choice8_2_end = input()
                        while not choice8_2_end.isnumeric():
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            choice8_2_end = input()

                        if index == 7:
                            index = 0
                        if count != 0:
                            fullQuery += ", "
                        fullQuery += "(SELECT * FROM \"Song\" where \"auditions\" BETWEEN " + choice8_2_start + " AND " + choice8_2_end + ") " + \
                                     values[index]
                        index += 1
                        count += 1

                    elif choice8_2 == "4":
                        print("ENTER LIKE EXPRESSION:")
                        choice8_2 = input()

                        if index == 7:
                            index = 0
                        if count != 0:
                            fullQuery += ", "
                        fullQuery += "(SELECT * FROM \"Song\" where \"Song\".\"release_date\" LIKE \'" + choice8_2 + "\') " + values[index]
                        index += 1
                        count += 1

                elif choice8 == "3":
                    print("1. artist_ID")
                    print("2. name")
                    print("3. full_name")
                    print("4. age")
                    print("5. songs_amount")

                    print("SELECT ATTRIBUTE:")
                    choice8_3 = input()
                    while choice8_3 != "1" and choice8_3 != "2" and choice8_3 != "3" and choice8_3 != "4" and choice8_3 != "5":
                        print("SELECT RIGHT OPTION")
                        choice8_3 = input()

                    if choice8_3 == "1":
                        print("ENTER START:")
                        choice8_3_start = input()
                        while not choice8_3_start.isnumeric():
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            choice8_3_start = input()
                        print("ENTER END:")
                        choice8_3_end = input()
                        while not choice8_3_end.isnumeric():
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            choice8_3_end = input()

                        if index == 7:
                            index = 0
                        if count != 0:
                            fullQuery += ", "
                        fullQuery += "(SELECT * FROM \"Artist\" where \"artist_ID\" BETWEEN " + choice8_3_start + " AND " + choice8_3_end + ") " + values[index]
                        index += 1
                        count += 1

                    elif choice8_3 == "2":
                        print("ENTER LIKE EXPRESSION:")
                        choice8_3 = input()

                        if index == 7:
                            index = 0
                        if count != 0:
                            fullQuery += ", "
                        fullQuery += "(SELECT * FROM \"Artist\" where \"Artist\".\"name\" LIKE \'" + choice8_3 + "\') " + values[index]
                        index += 1
                        count += 1

                    elif choice8_3 == "3":
                        print("ENTER LIKE EXPRESSION:")
                        choice8_3 = input()

                        if index == 7:
                            index = 0
                        if count != 0:
                            fullQuery += ", "
                        fullQuery += "(SELECT * FROM \"Artist\" where \"Artist\".\"full_name\" LIKE \'" + choice8_3 + "\') " + values[index]
                        index += 1
                        count += 1

                    elif choice8_3 == "4":
                        print("ENTER START:")
                        choice8_2_start = input()
                        while not choice8_2_start.isnumeric():
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            choice8_2_start = input()
                        print("ENTER END:")
                        choice8_2_end = input()
                        while not choice8_2_end.isnumeric():
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            choice8_2_end = input()

                        if index == 7:
                            index = 0
                        if count != 0:
                            fullQuery += ", "
                        fullQuery += "(SELECT * FROM \"Artist\" where \"Artist\".\"age\" BETWEEN " + choice8_2_start + " AND " + choice8_2_end + ") " + values[index]
                        index += 1
                        count += 1

                    elif choice8_3 == "5":
                        print("ENTER START:")
                        choice8_2_start = input()
                        while not choice8_2_start.isnumeric():
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            choice8_2_start = input()
                        print("ENTER END:")
                        choice8_2_end = input()
                        while not choice8_2_end.isnumeric():
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            choice8_2_end = input()

                        if index == 7:
                            index = 0
                        if count != 0:
                            fullQuery += ", "
                        fullQuery += "(SELECT * FROM \"Artist\" where \"Artist\".\"songs_amount\" BETWEEN " + choice8_2_start + " AND " + choice8_2_end + ") " + values[index]
                        index += 1
                        count += 1

                elif choice8 == "4":
                    print("1. name")
                    print("2. creation_date")
                    print("3. country")

                    print("SELECT ATTRIBUTE:")
                    choice8_4 = input()
                    while choice8_4 != "1" and choice8_4 != "2" and choice8_4 != "3":
                        print("SELECT RIGHT OPTION")
                        choice8_4 = input()

                    print("ENTER LIKE EXPRESSION:")
                    if choice8_4 == "1":
                        choice8_4 = input()
                        if index == 7:
                            index = 0
                        if count != 0:
                            fullQuery += ", "
                        fullQuery += "(SELECT * FROM \"Label\" where \"Label\".\"name\" LIKE \'" + choice8_4 + "\') " + values[index]
                        index += 1
                        count += 1

                    elif choice8_4 == "2":
                        choice8_4 = input()
                        if index == 7:
                            index = 0
                        if count != 0:
                            fullQuery += ", "
                        fullQuery += "(SELECT * FROM \"Label\" where \"Label\".\"creation_date\" LIKE \'" + choice8_4 + "\') " + values[index]
                        index += 1
                        count += 1

                    elif choice8_4 == "3":
                        choice8_4 = input()
                        if index == 7:
                            index = 0
                        if count != 0:
                            fullQuery += ", "
                        fullQuery += "(SELECT * FROM \"Label\" where \"Label\".\"country\" LIKE \'" + choice8_4 + "\') " + values[index]
                        index += 1
                        count += 1

                elif choice8 == "5":
                    print("1. user_ID")
                    print("2. song_ID")

                    print("SELECT ATTRIBUTE:")
                    choice8_5 = input()
                    while choice8_5 != "1" and choice8_5 != "2":
                        print("SELECT RIGHT OPTION")
                        choice8_5 = input()

                    if choice8_5 == "1":
                        print("ENTER START:")
                        choice8_5_start = input()
                        while not choice8_5_start.isnumeric():
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            choice8_5_start = input()
                        print("ENTER END:")
                        choice8_5_end = input()
                        while not choice8_5_end.isnumeric():
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            choice8_5_end = input()
                        if index == 7:
                            index = 0
                        if count != 0:
                            fullQuery += ", "
                        fullQuery += "(SELECT * FROM \"User/Song\" where \"User/Song\".\"user_ID\" BETWEEN " + choice8_5_start + " AND " + choice8_5_end + ") " + values[index]
                        index += 1
                        count += 1

                    elif choice8_5 == "2":
                        print("ENTER START:")
                        choice8_5_start = input()
                        while not choice8_5_start.isnumeric():
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            choice8_5_start = input()
                        print("ENTER END:")
                        choice8_5_end = input()
                        while not choice8_5_end.isnumeric():
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            choice8_5_end = input()
                        if index == 7:
                            index = 0
                        if count != 0:
                            fullQuery += ", "
                        fullQuery += "(SELECT * FROM \"User/Song\" where \"User/Song\".\"song_ID\" BETWEEN " + choice8_5_start + " AND " + choice8_5_end + ") " + values[index]
                        index += 1
                        count += 1

                elif choice8 == "6":
                    print("1. artist_ID")
                    print("2. song_ID")

                    print("SELECT ATTRIBUTE:")
                    choice8_6 = input()
                    while choice8_6 != "1" and choice8_6 != "2":
                        print("SELECT RIGHT OPTION")
                        choice8_6 = input()

                    if choice8_6 == "1":
                        print("ENTER START:")
                        choice8_6_start = input()
                        while not choice8_6_start.isnumeric():
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            choice8_6_start = input()
                        print("ENTER END:")
                        choice8_6_end = input()
                        while not choice8_6_end.isnumeric():
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            choice8_6_end = input()
                        if index == 7:
                            index = 0
                        if count != 0:
                            fullQuery += ", "
                        fullQuery += "(SELECT * FROM \"Artist/Song\" where \"Artist/Song\".\"artist_ID\" BETWEEN " + choice8_6_start + " AND " + choice8_6_end + ") " + values[index]
                        index += 1
                        count += 1

                    elif choice8_6 == "2":
                        print("ENTER START:")
                        choice8_6_start = input()
                        while not choice8_6_start.isnumeric():
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            choice8_6_start = input()
                        print("ENTER END:")
                        choice8_6_end = input()
                        while not choice8_6_end.isnumeric():
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            choice8_6_end = input()
                        if index == 7:
                            index = 0
                        if count != 0:
                            fullQuery += ", "
                        fullQuery += "(SELECT * FROM \"Artist/Song\" where \"Artist/Song\".\"song_ID\" BETWEEN " + choice8_6_start + " AND " + choice8_6_end + ") " + values[index]
                        index += 1
                        count += 1

                elif choice8 == "7":
                    print("1. label_name")
                    print("2. artist_ID")

                    print("SELECT ATTRIBUTE:")
                    choice8_7 = input()
                    while choice8_7 != "1" and choice8_7 != "2":
                        print("SELECT RIGHT OPTION")
                        choice8_7 = input()

                    if choice8_7 == "1":
                        print("ENTER LIKE EXPRESSION:")
                        choice8_7 = input()
                        if index == 7:
                            index = 0
                        if count != 0:
                            fullQuery += ", "
                        fullQuery += "(SELECT * FROM \"Label/Artist\" where \"Label/Artist\".\"label_name\" LIKE \'" + choice8_7 + "\') " + values[index]
                        index += 1
                        count += 1

                    elif choice8_7 == "2":
                        print("ENTER START:")
                        choice8_7_start = input()
                        while not choice8_7_start.isnumeric():
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            choice8_7_start = input()
                        print("ENTER END:")
                        choice8_7_end = input()
                        while not choice8_7_end.isnumeric():
                            print("WRONG DATA TYPE. ENTER CORRECT DATA:")
                            choice8_7_end = input()
                        if index == 7:
                            index = 0
                        if count != 0:
                            fullQuery += ", "
                        fullQuery += "(SELECT * FROM \"Label/Artist\" where \"Label/Artist\".\"artist_ID\" BETWEEN " + choice8_7_start + " AND " + choice8_7_end + ") " + values[index]
                        index += 1
                        count += 1

            count = 0
            with connection.cursor() as cursor:
                cursor.execute(fullQuery)
                dataInfo = cursor.fetchall()
                for row in dataInfo:
                    print(row)

        elif choice == "9":
            break

except Exception() as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
