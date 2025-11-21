# TITLE: DEVOPS SCHEMA APP
from flask import Flask, render_template, request
import pandas as pd
import functions

# Temp varibler som undelättar att köra programmet windows - DO NOT MIND
next_date :str = ''
next_class :str = 'Blir senare en lista med information'
weather_from_api : str ='' 
daily_df = 'Pandas dataframe'

# Skapa flask-app
app = Flask(__name__)

# Skapa end-point: index GET
@app.route("/")
def index():
    """
    Funktion som visar den nödvändiga informationen för att hitta till Skolan i tid.
    Samt väderlek så man vet om man behöver underställ. Se functions.py för detaljerad information.
    """
    # Datavariabler som hämtas för att printa uppdaterad information på hemsidan.
    code = str(weather_from_api[0])
    desc = functions.weather_text(code)
    icon_path = functions.get_icon(code)
    
    # Returnerar variabler med jinja till vår index-sida se tex. index.html r.47.
    return render_template(
        "index.html",
        next_class=next_class,
        desc=desc,
        weather_from_api=weather_from_api,
        icon=icon_path,
        title="EMB - Schema & väder"
    )

# Skapa end-point: Skicka till Discord GET
@app.route("/page1")
def page1():
    return render_template("page1.html", title="EMB - Skicka till Discord")


# Skapa end-point: Data till app.py från Form POST
@app.post("/page1-api")
def page1_api():
    "Input Discord Channel_ID and Authorization"

    # Get input from form. Type DEMO, SEND to send to discord.
    channel_id:str = request.form["channel_id"]
    auth_code:str = request.form["authorization_code"]

    # Variabler att skicka till Discord
    code = str(weather_from_api[0])
    desc = functions.weather_text(code)
    code = str(weather_from_api[0])
    desc = functions.weather_text(code)

    #Message to Discord med Markdown-syntax
    weather_text_info = f'\n{desc}\nMax_Temp:{weather_from_api[1]}\nMin_Temp:{weather_from_api[2]}\nTot_regn/snö:{weather_from_api[3]}'
    content:str = f"Om det här meddelandet går fram funkar all backend.\n\n**Next Class:{next_class[0]}**\n{next_class[1]}\n{next_class[2]}\n\n**Weather Forcast:**{weather_text_info}\n\n\n***Hello World, från vår App!***"
    # Villkor för DEMO-visning.
    if channel_id == 'DEMO' and auth_code == 'SEND':
        functions.post_to_DISCORD(content = content)
        message = "Meddelandet skickades till Discord-kanalen!"
    else:
        message = "Inget meddelande skickades. Fyll i formuläret korrekt."

    return render_template("page1.html", 
                            title="EMB - Sicka till Discord",
                            message=message)
  

@app.route("/page2")
def page2():
    """Funktion som visar schema från schema.pdf"""
    schema_path = './static/schema.pdf'

    return render_template("page2.html", 
                            title="SCHEMA",
                            schema=schema_path)


@app.route("/page3")
def page3():
    """Funktion som visar väder från Pandas Dataframe"""
    selected_columns = [
        "datum",
        "temperature_2m_max °C",
        "temperature_2m_min °C",
        "sunrise",
        "sunset",
        "wind_speed_10m_max m/s"
    ]
    
    available_columns = [col for col in selected_columns if col in daily_df.columns]
    filtered_df = daily_df[available_columns].copy()

    # formattering och manipulering inför print
    if "sunrise" in filtered_df.columns:
        filtered_df["sunrise"] = filtered_df["sunrise"].astype(str).str.replace(
            r".*T(\d{2}:\d{2}).*", r"\1", regex=True
        )
    if "sunset" in filtered_df.columns:
        filtered_df["sunset"] = filtered_df["sunset"].astype(str).str.replace(
            r".*T(\d{2}:\d{2}).*", r"\1", regex=True
        )

    filtered_df.rename(columns={
        "datum": "Datum",
        "temperature_2m_max °C": "Max (°C)",
        "temperature_2m_min °C": "Min (°C)",
        "sunrise": "Soluppgång",
        "sunset": "Solnedgång",
        "wind_speed_10m_max m/s": "Vindhastighet (m/s)"
    }, inplace=True)

    table_html = filtered_df.to_html(
        index=False,
        border=0,
        classes="tbl table table-striped table-hover",
        justify="center"
    ).replace(
        "<table",
        "<table style='width:90%;font-size:1rem;margin:auto;border-collapse:collapse;'"
    ).replace(
        "<th>",
        "<th style='padding:8px;border-bottom:2px solid #CCCCCC;text-align:center;color:#000000;'>"
    ).replace(
        "<td>",
        "<td style='padding:6px;text-align:center;'>"
    )

    return render_template("page3.html", 
                            title="VÄDER", 
                            table_html=table_html)


# Hanterar försök till andra endpoints än tillåtna.
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", title="EMB - 404 Sidan kunde inte hittas"), 404


if __name__ == "__main__":
    """
    Hämtar data från externa API:er och sparar denna i variabler.
    Se functions.py för detaljerad information...
    """
    next_date, next_class  = functions.get_schema()
    weather_from_api, daily_df = functions.get_weather(next_date)
    app.run(debug=True)