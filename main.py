import pandas as pd
import numpy as np
from translate import Translator

from flask import Flask,render_template,redirect,url_for,request



pd.set_option('display.max_rows', 50000)
pd.set_option('display.max_columns', 500000)
pd.set_option('display.width', 100000)

df= pd.read_csv('C:/Users/xtoy4/Desktop/recommender system/OurData/movies.csv')

df_rating= pd.read_csv('C:/Users/xtoy4/Desktop/recommender system/OurData/ratings.csv')

df.rename(columns = {'title':''}, inplace = True)

df[''].replace(['The facts of the years of embers','the mummy','iron door','Earth','The silence of the palaces','city dreams','divine hand','Kit Kat','West Beirut','deceived'],['وقائع سنين الجمر','المومياء','باب الحديد','الأرض','صمت القصور','أحلام المدينة','يد إلهية','الكيت كات','بيروت الغربية','المخدوعون'],inplace=True)

df = pd.merge(df,df_rating, on='movieId')

ratings = pd.DataFrame(df.groupby('')['rating'].mean())

ratings['عدد التقيمات'] = df.groupby('')['rating'].count()




movie_matrix = df.pivot_table(index='userid', columns='', values='rating')

movie_name1 = 'وقائع سنين الجمر'
movie_name2 = 'المومياء'
movie_name3 = 'باب الحديد'
movie_name4 ='الأرض'
movie_name5 ='صمت القصور'
movie_name6 = 'أحلام المدينة'
movie_name7 = 'يد إلهية'
movie_name8 ='الكيت كات'
movie_name9 = 'بيروت الغربية'
movie_name10 ='المخدوعون'

JP_user_rating = movie_matrix[movie_name1]
similar_to_JP = movie_matrix.corrwith(JP_user_rating)
corr_JP1 = pd.DataFrame(similar_to_JP, columns=['Correlation'])
corr_JP1 = corr_JP1.join(ratings['عدد التقيمات'])
corr_JP1.sort_values('Correlation', inplace=True, ascending=False)


movie1= corr_JP1.select_dtypes(exclude=['float64']).iloc[1:2]
movie2= corr_JP1.select_dtypes(exclude=['float64']).iloc[2:3]




JP_user_rating = movie_matrix[movie_name2]
similar_to_JP = movie_matrix.corrwith(JP_user_rating)
corr_JP2 = pd.DataFrame(similar_to_JP, columns=['Correlation'])
corr_JP2 = corr_JP2.join(ratings['عدد التقيمات'])
corr_JP2.sort_values('Correlation', inplace=True, ascending=False)

movie3= corr_JP2.select_dtypes(exclude=['float64']).iloc[1:2]
movie4= corr_JP2.select_dtypes(exclude=['float64']).iloc[2:3]

JP_user_rating = movie_matrix[movie_name3]
similar_to_JP = movie_matrix.corrwith(JP_user_rating)
corr_JP3 = pd.DataFrame(similar_to_JP, columns=['Correlation'])
corr_JP3 = corr_JP3.join(ratings['عدد التقيمات'])
corr_JP3.sort_values('Correlation', inplace=True, ascending=False)

movie5= corr_JP3.select_dtypes(exclude=['float64']).iloc[1:2]
movie6= corr_JP3.select_dtypes(exclude=['float64']).iloc[2:3]

JP_user_rating = movie_matrix[movie_name4]
similar_to_JP = movie_matrix.corrwith(JP_user_rating)
corr_JP4 = pd.DataFrame(similar_to_JP, columns=['Correlation'])
corr_JP4 = corr_JP4.join(ratings['عدد التقيمات'])
corr_JP4.sort_values('Correlation', inplace=True, ascending=False)

movie7= corr_JP4.select_dtypes(exclude=['float64']).iloc[1:2]
movie8= corr_JP4.select_dtypes(exclude=['float64']).iloc[2:3]

JP_user_rating = movie_matrix[movie_name5]
similar_to_JP = movie_matrix.corrwith(JP_user_rating)
corr_JP5 = pd.DataFrame(similar_to_JP, columns=['Correlation'])
corr_JP5 = corr_JP5.join(ratings['عدد التقيمات'])
corr_JP5.sort_values('Correlation', inplace=True, ascending=False)

movie9= corr_JP5.select_dtypes(exclude=['float64']).iloc[1:2]
movie10= corr_JP5.select_dtypes(exclude=['float64']).iloc[2:3]

JP_user_rating = movie_matrix[movie_name6]
similar_to_JP = movie_matrix.corrwith(JP_user_rating)
corr_JP6 = pd.DataFrame(similar_to_JP, columns=['Correlation'])
corr_JP6 = corr_JP6.join(ratings['عدد التقيمات'])
corr_JP6.sort_values('Correlation', inplace=True, ascending=False)

movie11= corr_JP6.select_dtypes(exclude=['float64']).iloc[1:2]
movie12= corr_JP6.select_dtypes(exclude=['float64']).iloc[2:3]

JP_user_rating = movie_matrix[movie_name7]
similar_to_JP = movie_matrix.corrwith(JP_user_rating)
corr_JP7 = pd.DataFrame(similar_to_JP, columns=['Correlation'])
corr_JP7 = corr_JP7.join(ratings['عدد التقيمات'])
corr_JP7.sort_values('Correlation', inplace=True, ascending=False)

movie13= corr_JP7.select_dtypes(exclude=['float64']).iloc[1:2]
movie14= corr_JP7.select_dtypes(exclude=['float64']).iloc[2:3]

JP_user_rating = movie_matrix[movie_name8]
similar_to_JP = movie_matrix.corrwith(JP_user_rating)
corr_JP8 = pd.DataFrame(similar_to_JP, columns=['Correlation'])
corr_JP8 = corr_JP8.join(ratings['عدد التقيمات'])
corr_JP8.sort_values('Correlation', inplace=True, ascending=False)

movie15= corr_JP8.select_dtypes(exclude=['float64']).iloc[1:2]
movie16= corr_JP8.select_dtypes(exclude=['float64']).iloc[2:3]

JP_user_rating = movie_matrix[movie_name9]
similar_to_JP = movie_matrix.corrwith(JP_user_rating)
corr_JP9 = pd.DataFrame(similar_to_JP, columns=['Correlation'])
corr_JP9 = corr_JP9.join(ratings['عدد التقيمات'])
corr_JP9.sort_values('Correlation', inplace=True, ascending=False)

movie17= corr_JP9.select_dtypes(exclude=['float64']).iloc[1:2]
movie18= corr_JP9.select_dtypes(exclude=['float64']).iloc[2:3]

JP_user_rating = movie_matrix[movie_name10]
similar_to_JP = movie_matrix.corrwith(JP_user_rating)
corr_JP10 = pd.DataFrame(similar_to_JP, columns=['Correlation'])
corr_JP10 = corr_JP10.join(ratings['عدد التقيمات'])
corr_JP10.sort_values('Correlation', inplace=True, ascending=False)

movie19= corr_JP10.select_dtypes(exclude=['float64']).iloc[1:2]
movie20= corr_JP10.select_dtypes(exclude=['float64']).iloc[2:3]

app = Flask (__name__)
@app.route("/")
def home():

    return render_template('index.html',m1=movie_name1,m2=movie_name2,m3=movie_name3,m4=movie_name4,m5=movie_name5,m6=movie_name6,m7=movie_name7,m8=movie_name8,m9=movie_name9,m10=movie_name10)



@app.route('/movie')
def about():



    return render_template('movie.html',m=movie_name1,r1=movie1,r2=movie2)

@app.route('/movieA')
def movieA():

    return render_template('movie1.html',m=movie_name2,r1=movie3,r2=movie4)
@app.route('/movieB')
def movieB():

    return render_template('movie2.html',m=movie_name3,r1=movie5,r2=movie6)
@app.route('/movieC')
def movieC():

    return render_template('movie3.html',m=movie_name4,r1=movie7,r2=movie8)
@app.route('/movieD')
def movieD():

    return render_template('movie4.html',m=movie_name5,r1=movie9,r2=movie10)
@app.route('/movieE')
def movieE():

    return render_template('movie5.html',m=movie_name6,r1=movie11,r2=movie12)
@app.route('/movieF')
def movieF():

    return render_template('movie6.html',m=movie_name7,r1=movie13,r2=movie14)
@app.route('/movieJ')
def movieJ():

    return render_template('movie7.html',m=movie_name8,r1=movie15,r2=movie16)
@app.route('/movieH')
def movieH():

    return render_template('movie8.html',m=movie_name9,r1=movie17,r2=movie18)
@app.route('/movieI')
def movieI():

    return render_template('movie9.html',m=movie_name10,r1=movie19,r2=movie20)
if __name__=="__main__":
    app.run()













