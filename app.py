from flask import Flask, request, render_template, redirect, url_for
from pytube import YouTube
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/download', methods=['POST'])
def download_video():
    video_link = request.form['link']
    if video_link:
        yt = YouTube(video_link)
        stream = yt.streams.get_highest_resolution()
        download_path = os.path.join(os.getcwd(), 'downloads')
        if not os.path.exists(download_path):
            os.makedirs(download_path)
        stream.download(output_path=download_path)
        return f"<h2>Download completed!! Check the 'downloads' folder.</h4><br><a href='{url_for('index')}'>Back</a>"
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
