def log_search(username, followers, following, posts):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    cursor.execute('INSERT INTO instagram_logs (username, followers, following, posts, timestamp) VALUES (?, ?, ?, ?, ?)', (username, followers, following, posts, timestamp))
    conn.commit()
    conn.close()