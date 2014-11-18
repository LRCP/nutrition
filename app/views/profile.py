from flask import request, render_template
from app import app, session
from flask.ext.login import login_user, current_user, login_required
from app.forms import ProfileForm

#from sqlalchemy import Column, Integer, Sequence, ForeignKey
#from sqlalchemy.orm import relationship

@app.route('/profile', methods=['GET'])
#login_required is a decorator function
@login_required
def profile_get():
    user=current_user
    form = ProfileForm(
        request.form, 
        calorie_goal=user.calorie_goal,
        protein_goal=user.protein_goal,
        carbohydrate_goal=user.carbohydrate_goal,
        fat_goal=user.fat_goal,
        birthday=user.birthday,
        weight_unit="weight_in_kilograms",
        weight=user.weight_in_kilograms,
        weight_goal=user.weight_goal,
        height_unit="height_in_meters",
        height=user.height_in_meters,
        gender=user.gender,
        activity_level=user.activity_level,
        weekly_change_level=user.get_weekly_change_level()
        )
    return render_template(
        'profile.html',
        #title is the name of the page for Profile: Nutrition
        title='Profile',   
        #make a variable in the template called form. 
        #The value of the form should be
        #equal to the variable form in the local function.
        form=form
        )


@app.route('/profile', methods=['POST'])
@login_required
def profile_post():
    form = ProfileForm(request.form)
    #print request.form


    if form.validate():

        #get the user from the database session
        user = current_user
        # do not store the results of calculations using variable defined in
        # models.py That is what models.py is for.
        user.calorie_goal = form.calorie_goal.data
        user.protein_goal = form.protein_goal.data
        #what about user.amino_acid_goals?
        #Institute of Medicine's Food and Nutrition Board
        # Essential Amino Acid    Needed per g of Protein Needed for 50g of Protein
        #     Trytophan   7mg/.007g   .35g
        #     Threonine   27mg/.027g  1.35g
        #     Isoleucine  25mg/025g   1.25g
        #     Leucine 55mg/.055g  2.76g
        #     Lysine  51mg/.051g  2.56g
        #     Methionine+Cystine  25mg/.025g  1.25g
        #     Phenylalanine+Tyrosine  47mg/.047g  2.36g
        #     Valine  32mg/.032g  1.60g
        #     Histidine   18mg/.018g  .90g
        #age of user determines multiplier of x times kg of weight
        # 1.5g per kg - infants
        # 1.1g per kg - 1-3 years
        # .95g per kg - 4-13 years
        # .85g per kg - 14-18 years
        # .80g per kg - adults
        # 1.1g per kg - pregnant and lactating women

        user.carbohydrate_goal = form.carbohydrate_goal.data
        user.fat_goal = form.fat_goal.data
        #user.nutrient_goal = form.nutrient_goal.data
        user.birthday = form.birthday.data
        user.set_weight(form.weight.data, form.weight_unit.data)
        user.set_weight_goal(form.weight_goal.data, form.weight_unit.data)
        user.set_height(form.height.data, form.height_unit.data)
        user.gender = form.gender.data 
        user.activity_level = form.activity_level.data
        user.set_weekly_weight_change(form.weekly_change_level.data)
        session.commit()
        #Here we need to save the information enterred by the User.
        #need access to the user object.
        #return redirect(url_for('profile_get'))


        return render_template(
            'profile.html',
            title='Profile',
            form=form,
            text='Either stay on your Profile or go to the Home, Foodlog or Logout Page.',

            )
    else:
        return render_template(
            'profile.html',
            title='Profile',
            form=form)
