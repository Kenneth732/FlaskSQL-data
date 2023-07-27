import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():