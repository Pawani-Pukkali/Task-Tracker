#python script
print("This is the run.py script.")

from app import create_app

app = create_app()
if __name__ == "__main__":

    app.run(debug=True)
    print("Starting the application...")
else:
    print("Application is not running in debug mode.")
    # Python does not use an explicit "end if" statement.
    # The end of the if block is determined by indentation.
    # So, you do not need to add anything here.
