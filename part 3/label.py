import sqlite3
import pdfkit


con = sqlite3.connect('database.db')


def create_db():
    """ Removes the labels table and creates it """
    con.execute('DROP TABLE IF EXISTS labels;')
    con.execute('''CREATE TABLE labels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        is_printed BOOLEAN
    );''')


def generate_pdf_with_labels():
    # Select data not marked as printed
    ret = con.execute('''
        SELECT id, name FROM labels WHERE is_printed IS NULL or is_printed != 1;
    ''')
    data = ret.fetchall()

    # Construct a string with all the entries
    text = ''
    for d in data:
        text += f'<br>{d[0]} for {d[1]}'

    # Overwrite the same pdf
    pdfkit.from_string(text, 'output.pdf')

    # Mark the entries as printed
    for d in data:
        con.execute("UPDATE labels SET is_printed = ? WHERE id = ?", (1, d[0],))
    con.commit()

if __name__ == '__main__':
    # 1. Create our database
    # create_db()
    # 2. Find a way to insert some data in the database
    # 3. Generate a pdf
    generate_pdf_with_labels()

con.close()
