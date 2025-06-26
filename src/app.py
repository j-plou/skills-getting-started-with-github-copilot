"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Tennis": {
        "description": "Competitive Tennis Match",
        "schedule": "Fridays 17:00-19:00",
        "max_participants": 8,
        "participants": ["alice@mergington.edu"]
    },
    "Swimming": {
        "description": "Recreational Swimming Session",
        "schedule": "Saturdays 10:00-12:00",
        "max_participants": 12,
        "participants": ["bob@mergington.edu"]
    },
    "Graffiti": {
        "description": "Urban Graffiti Workshop",
        "schedule": "Sundays 16:00-18:00",
        "max_participants": 10,
        "participants": ["carol@mergington.edu"]
    },
    "Breakdancing": {
        "description": "Street Breakdancing Jam",
        "schedule": "Wednesdays 18:00-20:00",
        "max_participants": 15,
        "participants": ["dave@mergington.edu"]
    },
    "Chess": {
        "description": "18th Century Chess Club",
        "schedule": "Mondays 15:00-17:00",
        "max_participants": 6,
        "participants": ["eve@mergington.edu"]
    },
    "Philosophy Tea Salon": {
        "description": "Philosophical Tea Salon Discussions",
        "schedule": "Thursdays 19:00-21:00",
        "max_participants": 10,
        "participants": ["frank@mergington.edu", "eve@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities.get(activity_name)

    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student already signed up")
    
    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
