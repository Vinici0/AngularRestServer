from flask import Flask, render_template, jsonify
from selenium import webdriver
from firefox_cookie_manager import FirefoxCookieManager
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
cookie_manager = FirefoxCookieManager()

@app.route('/get_firefox', methods=['GET'])
def get_cookies_firefox():
    data_cookie = cookie_manager.obtener_cookies_firefox()
    return jsonify(data_cookie)

@app.route('/get_chrome', methods=['GET'])
def obtener_cookies_chrome():
    data_cookie = cookie_manager.obtener_cookies_chrome()
    return jsonify(data_cookie)

@app.route('/get_firefox_dominios', methods=['GET'])
def obtener_cookies_firefox_dominios():
    data_cookie = cookie_manager.obtener_cookies_firefox_dominios()
    return jsonify(data_cookie)

@app.route('/get_top_ten_paginas_visitadas', methods=['GET'])
def obtener_top_ten_paginas_visitadas():
    data_cookie = cookie_manager.obtener_top_ten_paginas_visitadas()
    return jsonify(data_cookie)

@app.route('/get_total_cookies_session_firefox', methods=['GET'])
def obtener_total_cookies_session_firefox():
    data_cookie = cookie_manager.obtener_total_cookies_session_firefox()
    return jsonify(5)

@app.route('/get_total_cookies_firefox', methods=['GET'])
def obtener_total_cookies_firefox():
    data_cookie = cookie_manager.obtener_total_cookies_firefox()
    return jsonify(data_cookie)

if __name__ == '__main__':
    # Ejecuta la aplicación Flask
    app.run()
