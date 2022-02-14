from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    #if we make change in the code it will automaticlly rerun the web server

