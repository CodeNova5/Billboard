from flask import Flask, request, jsonify
import billboard

app = Flask(__name__)

@app.route('/top-songs', methods=['GET'])
def get_top_songs():
    # Get parameters from the request
    chart_name = request.args.get('chart', 'hot-100')  # Default to 'hot-100'
    limit = int(request.args.get('limit', 10))  # Default to top 10 songs

    try:
        # Fetch the specified chart
        chart = billboard.ChartData(chart_name)

        # Get the top songs based on the limit
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

if __name__ == '__main__':
    app.run(debug=True)
