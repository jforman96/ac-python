#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, flash
from api import AzerothCoreAPI
import os

# Get environment variables
title = os.getenv('TITLE', 'Default Title')
footer_text = os.getenv('FOOTER', 'Default Footer Text')
username = os.getenv('USERNAME', 'username')
password = os.getenv('PASSWORD', 'password')
webproto = os.getenv('PROTO', 'http')
api_url = os.getenv('API_URL', 'example.com')
armory_url =  os.getenv('ARMORY_URL', 'example.com')
download_link = os.getenv('DOWNLOAD_LINK', 'example.com')

api = AzerothCoreAPI(f'{webproto}://{username}:{password}@{api_url}')
app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', title=title, footer_text=footer_text)


@app.route('/armory', methods=['GET'])
def armory():
    return render_template('armory.html', title=title, footer_text=footer_text, armory_url=armory_url)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password_repeat = request.form.get('password_repeat')

        # Validate the inputs
        if not username or not password or not password_repeat:
            flash('All fields are required.')
            return render_template('register.html', title=title, footer_text=footer_text)
        if password != password_repeat:
            flash('Passwords do not match.')
            return render_template('register.html', title=title, footer_text=footer_text)

        # Create the user using SOAP API
        result = api.account("create", username, password)
        if "SOAP Error" in result:
            error_message = result.replace('SOAP Error:', '').strip()
            flash(error_message)
            return render_template('register.html', title=title, footer_text=footer_text)

        # Redirect to the success page
        return render_template('success.html', title=title, footer_text=footer_text)

    return render_template('register.html', title=title, footer_text=footer_text)


@app.route('/download', methods=['GET'])
def download():
    return redirect(download_link)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
