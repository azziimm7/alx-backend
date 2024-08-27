#!/usr/bin/env python3
"""
A basic Flask app
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index() -> str:
    """Display a simple html page"""
    return render_template('0-index.html')
