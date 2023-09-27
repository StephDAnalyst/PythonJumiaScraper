import re
import mysql.connector
from itemadapter import ItemAdapter

class SaveToMySQLJumiaPipeline:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='hostname',
            user='your_username',
            password='your_password',
            database='your_database_name'
        )
        self.cursor = self.connection.cursor()

        # Create the necessary table if not exists
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS JumiaProdus(
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                seller_name VARCHAR(255),
                seller_score VARCHAR(255),
                followers INT,
                rating FLOAT,
                rating_count INT,
                url TEXT
            )
        """)

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # Extract the first numeric value from rating_count
        rating_count = adapter.get('rating_count')
        if rating_count:
            match = re.search(r'\d+', rating_count)
            rating_count_value = int(match.group()) if match else None
        else:
            rating_count_value = None

        # Extract the first number from the rating
        rating = adapter.get('rating', '')
        first_number = float(rating.split()[0]) if rating and rating.split()[0].replace('.', '').isdigit() else None

        # Extract followers and update
        followers = ''.join(filter(str.isdigit, adapter.get('followers', '')))
        followers_value = int(followers) if followers.isdigit() else None

        # Extract seller_score and remove '%', then convert to int
        seller_score = adapter.get('seller_score', '')
        seller_score_int = int(seller_score.replace('%', '')) if seller_score and seller_score.isdigit() else None

        # Prepare the data to be inserted into the database
        data = (
            adapter.get('name', '').strip(),
            adapter.get('seller_name', '').strip(),
            seller_score_int,
            followers_value,
            first_number,
            rating_count_value,
            adapter.get('url', '').strip()
        )

        try:
            # Execute the SQL insert statement
            self.cursor.execute("""
                INSERT INTO JumiaProdus (name, seller_name, seller_score, followers, rating, rating_count, url)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, data)
            self.connection.commit()
            print('Item successfully inserted into the database.')
        except mysql.connector.Error as err:
            print('Failed to insert item into the database:', err)

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()
