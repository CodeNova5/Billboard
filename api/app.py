from flask import Flask, request, jsonify
import billboard

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Hello from Flask on Vercel!")

@app.route('/top-songs', methods=['GET'])
def get_top_songs():
    chart_name = request.args.get('chart', 'hot-100')
    limit = int(request.args.get('limit', 10))

    try:
        chart = billboard.ChartData(chart_name)
        songs = []
        for i in range(min(limit, len(chart))):
            song = chart[i]
            songs.append({
                'rank': i + 1,
                'title': song.title,
                'artist': song.artist
            })

        return jsonify(songs)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Vercel will look for 'handler' variable
def handler(environ, start_response):
    return app.wsgi_app(environ, start_response)

if __name__ == '__main__':
    app.run(debug=True)