POSTGRES_USER = 'postgres'
POSTGRES_PASSWORD = '6037845' # os.getenv('POSTGRES_PASSWORD')
PORT = '5432'
POSTGRES_DB = 'bank_db'


DATABASE_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:{PORT}/{POSTGRES_DB}'