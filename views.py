from flask import Blueprint, render_template, request
from activities import *
import random

# create Blueprint instance for views
views = Blueprint(__name__, "views")


def get_random_activity(activity_type):

    # randomly choose an activity from imported activities dictionary
    if activity_type == 'lunch':
        activity = random.choice(list(lunch_activities.values()))
    elif activity_type == 'dinner':
        activity = random.choice(list(dinner_activities.values()))
    elif activity_type == 'drink':
        activity = random.choice(list(drink_activities.values()))

    # retrieve name, location, cost, description, and image of chosen activity
    activity_name = activity['name']
    activity_location = activity['location']
    activity_cost = activity['cost']
    activity_description = activity['description']
    activity_booking = activity['book_link']
    activity_image = activity['image']

    return activity_name, activity_location, activity_cost, activity_description, activity_image, activity_booking


# define route for the home page, which displays either a random activity or the homepage depending on whether the "Lucky" button was clicked
@views.route('/', methods=['GET', 'POST'])
def show_activity():
    # if "Lucky" button clicked
    if request.form.get('lucky-lunch') == 'Lucky Lunch':
        # set lunch activity
        activity_type = 'lunch'

        # get random lunch activity
        activity_name, activity_location, activity_cost, activity_description, activity_image, activity_booking = get_random_activity(
            activity_type)

        # display activity page with lunch info
        return render_template('lunch_activity.html', activity_name=activity_name, activity_location=activity_location, activity_cost=activity_cost, activity_description=activity_description, activity_image=activity_image, activity_booking=activity_booking)

    elif request.form.get('lucky-dinner') == 'Lucky Dinner':
        # set dinner activity
        activity_type = 'dinner'

        # get random dinner activity
        activity_name, activity_location, activity_cost, activity_description, activity_image, activity_booking = get_random_activity(
            activity_type)

        # display activity page with dinner info
        return render_template('dinner_activity.html', activity_name=activity_name, activity_location=activity_location, activity_cost=activity_cost, activity_description=activity_description, activity_image=activity_image, activity_booking=activity_booking)

    elif request.form.get('lucky-drink') == 'Lucky Drink':
        # set drink activity
        activity_type = 'drink'

        # get random drink activity
        activity_name, activity_location, activity_cost, activity_description, activity_image, activity_booking = get_random_activity(
            activity_type)

        # display activity page with drink info
        return render_template('drink_activity.html', activity_name=activity_name, activity_location=activity_location, activity_cost=activity_cost, activity_description=activity_description, activity_image=activity_image, activity_booking=activity_booking)

    # if "Lucky" button not clicked
    # display homepage
    return render_template('index.html')
