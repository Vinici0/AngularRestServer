import os
import shutil
import sqlite3
import pandas as pd
from flask_pymongo import PyMongo
class FirefoxCookieManager:
    def __init__(self):
        pass

    def obtener_cookies_firefox(self):
        data_cookies = []
        data_cookies = {
            "autenticacion_seguridad": [],
            "preferencias_usuario": [],
            "rendimiento_analisis": [],
            "publicidad_seguimiento": [],
            "funcionalidad_sitio_web": [],
            "otras": []
        }

        if os.name == "nt":
            path_to_cookies = os.path.join(os.getenv('APPDATA'), "Mozilla", "Firefox", "Profiles")
        else:
            path_to_cookies = os.path.expanduser("~/.mozilla/firefox/Profiles")

        profile_dirs = [d for d in os.listdir(path_to_cookies) if os.path.isdir(os.path.join(path_to_cookies, d))]

        if not profile_dirs:
            print("No se pudo encontrar ningún directorio de perfil de Firefox")
            return data_cookies

        for profile_dir in profile_dirs:
            temp_cookie_db = os.path.join(os.path.dirname(__file__), 'cookies.sqlite')
            cookie_db_path = os.path.join(path_to_cookies, profile_dir, 'cookies.sqlite')

            if not os.path.exists(cookie_db_path):
                continue

            shutil.copy2(cookie_db_path, temp_cookie_db)

            conn = sqlite3.connect(temp_cookie_db)
            cursor = conn.cursor()

            cursor.execute("SELECT name, value, host, path,expiry  FROM moz_cookies")
            """
            "name": El nombre de la cookie.
            "value": El valor asociado con la cookie.
            "host": El host al que pertenece la cookie.
            "path": La ruta del servidor para la cual la cookie está disponible.
            """
            for row in cursor.fetchall():
                name, value, host, path, expiry = row

                # Aquí clasificamos las cookies
                if "token" in name or "session" in name:
                    data_cookies["autenticacion_seguridad"].append({
                        "name": name,
                        "value": value,
                        "host": host,
                        "path": path,
                        "expiry": expiry
                    })
                elif "lang" in name or "preference" in name:
                    data_cookies["preferencias_usuario"].append({
                        "name": name,
                        "value": value,
                        "host": host,
                        "path": path,
                        "expiry": expiry
                    })
                elif "analytics" in name or "tracking" in name:
                    data_cookies["rendimiento_analisis"].append({
                        "name": name,
                        "value": value,
                        "host": host,
                        "path": path,
                        "expiry": expiry
                    })
                elif "advertising" in name or "ad_" in name:
                    data_cookies["publicidad_seguimiento"].append({
                        "name": name,
                        "value": value,
                        "host": host,
                        "path": path,
                        "expiry": expiry
                    })
                elif "cart" in name or "user_preference" in name:
                    data_cookies["funcionalidad_sitio_web"].append({
                        "name": name,
                        "value": value,
                        "host": host,
                        "path": path,
                        "expiry": expiry
                    })
                else:
                    data_cookies["otras"].append({
                        "name": name,
                        "value": value,
                        "host": host,
                        "path": path,
                        "expiry": expiry
                    })
            conn.close()

        return data_cookies


    """
        Numerp de dominios sin repetir
    """
    def obtener_cookies_firefox_dominios(self):
        data_cookies = []
        if os.name == "nt":
            path_to_cookies = os.path.join(os.getenv('APPDATA'), "Mozilla", "Firefox", "Profiles")
        else:
            path_to_cookies = os.path.expanduser("~/.mozilla/firefox/Profiles")

        profile_dirs = [d for d in os.listdir(path_to_cookies) if os.path.isdir(os.path.join(path_to_cookies, d))]

        if not profile_dirs:
            print("No se pudo encontrar ningún directorio de perfil de Firefox")
            return data_cookies

        for profile_dir in profile_dirs:
            temp_cookie_db = os.path.join(os.path.dirname(__file__), 'cookies.sqlite')
            cookie_db_path = os.path.join(path_to_cookies, profile_dir, 'cookies.sqlite')

            if not os.path.exists(cookie_db_path):
                continue

            shutil.copy2(cookie_db_path, temp_cookie_db)

            conn = sqlite3.connect(temp_cookie_db)
            cursor = conn.cursor()

            cursor.execute("SELECT DISTINCT host FROM moz_cookies")
            """
            "name": El nombre de la cookie.
            "value": El valor asociado con la cookie.
            "host": El host al que pertenece la cookie.
            "path": La ruta del servidor para la cual la cookie está disponible.
            """
            for row in cursor.fetchall():
                host = row
                data_cookies.append(host)
            conn.close()

        return data_cookies

    """
        Pginas mas visitadas
    """
    def obtener_top_ten_paginas_visitadas(self):
        data_pages = []

        if os.name == "nt":
            path_to_profiles = os.path.join(os.getenv('APPDATA'), "Mozilla", "Firefox", "Profiles")
        else:
            path_to_profiles = os.path.expanduser("~/.mozilla/firefox/Profiles")

        profile_dirs = [d for d in os.listdir(path_to_profiles) if os.path.isdir(os.path.join(path_to_profiles, d))]

        if not profile_dirs:
            print("No se pudo encontrar ningún directorio de perfil de Firefox")
            return data_pages

        for profile_dir in profile_dirs:
            temp_history_db = os.path.join(os.path.dirname(__file__), 'history.sqlite')
            history_db_path = os.path.join(path_to_profiles, profile_dir, 'places.sqlite')

            if not os.path.exists(history_db_path):
                continue

            shutil.copy2(history_db_path, temp_history_db)

            conn = sqlite3.connect(temp_history_db)
            cursor = conn.cursor()

            cursor.execute("SELECT url, title, visit_count FROM moz_places ORDER BY visit_count DESC LIMIT 10")

            for row in cursor.fetchall():
                url, title, visit_count = row
                data_pages.append({
                    "url": url,
                    "title": title,
                    "visit_count": visit_count
                })

            conn.close()

        return data_pages

    """
    Total de cookies de ssion almacenadas
    """

    def obtener_total_cookies_session_firefox(self):
        total_cookies = 0
        if os.name == "nt":
            path_to_cookies = os.path.join(os.getenv('APPDATA'), "Mozilla", "Firefox", "Profiles")
        else:
            path_to_cookies = os.path.expanduser("~/.mozilla/firefox/Profiles")

        profile_dirs = [d for d in os.listdir(path_to_cookies) if os.path.isdir(os.path.join(path_to_cookies, d))]

        if not profile_dirs:
            print("No se pudo encontrar ningún directorio de perfil de Firefox")
            return total_cookies

        for profile_dir in profile_dirs:
            temp_cookie_db = os.path.join(os.path.dirname(__file__), 'cookies.sqlite')
            cookie_db_path = os.path.join(path_to_cookies, profile_dir, 'cookies.sqlite')

            if not os.path.exists(cookie_db_path):
                continue

            shutil.copy2(cookie_db_path, temp_cookie_db)

            conn = sqlite3.connect(temp_cookie_db)
            cursor = conn.cursor()

            cursor.execute("SELECT name, value, host, path,expiry  FROM moz_cookies")

            for row in cursor.fetchall():
                name, value, host, path, expiry = row

                # Aquí clasificamos las cookies
                if "token" in name or "session" in name:
                    total_cookies += 1
            conn.close()

        return total_cookies

    """
    Total de todas las cookies almacenadas
    """
    def obtener_total_cookies_firefox(self):
        total_cookies = 0
        if os.name == "nt":
            path_to_cookies = os.path.join(os.getenv('APPDATA'), "Mozilla", "Firefox", "Profiles")
        else:
            path_to_cookies = os.path.expanduser("~/.mozilla/firefox/Profiles")

        profile_dirs = [d for d in os.listdir(path_to_cookies) if os.path.isdir(os.path.join(path_to_cookies, d))]

        if not profile_dirs:
            print("No se pudo encontrar ningún directorio de perfil de Firefox")
            return total_cookies

        for profile_dir in profile_dirs:
            temp_cookie_db = os.path.join(os.path.dirname(__file__), 'cookies.sqlite')
            cookie_db_path = os.path.join(path_to_cookies, profile_dir, 'cookies.sqlite')

            if not os.path.exists(cookie_db_path):
                continue

            shutil.copy2(cookie_db_path, temp_cookie_db)

            conn = sqlite3.connect(temp_cookie_db)
            cursor = conn.cursor()

            cursor.execute("SELECT name, value, host, path,expiry  FROM moz_cookies")

            for row in cursor.fetchall():
                name, value, host, path, expiry = row
                total_cookies += 1
            conn.close()

        return total_cookies
    def obtener_cookies_chrome(self):
        con2 = sqlite3.connect(r"C:\Users\VINICIO BORJA\AppData\Local\Google\Chrome\User Data\Default\Network\Cookies")
        df = pd.read_sql_query("SELECT * from cookies", con2)
        return df

